"""pytest 公共夹具：用 SQLite 内存数据库替代 MySQL，测试无需外部依赖。

策略：
1. 在导入 app 之前设置 DATABASE_URL=sqlite，使全局 engine 指向内存库。
2. 每个测试函数获得一个全新的内存 engine + SessionLocal，
   并通过 dependency_overrides 注入，保证请求与测试共享同一 engine。
3. 不再依赖全局 engine 的连接清理，彻底隔离。
"""
import os

# 必须在导入 app 之前设置，使全局 engine 使用 SQLite 内存库
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import create_engine  # noqa: E402
from sqlalchemy.orm import sessionmaker  # noqa: E402
from sqlalchemy.pool import StaticPool  # noqa: E402

from app.database import Base, get_db  # noqa: E402
from app.main import app  # noqa: E402


def _make_memory_engine():
    return create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )


@pytest.fixture()
def client():
    """每个测试一个独立内存库，请求与测试共享同一 engine。"""
    engine = _make_memory_engine()
    Base.metadata.create_all(bind=engine)
    TestSession = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

    def _override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
