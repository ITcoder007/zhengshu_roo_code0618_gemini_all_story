"""SQLAlchemy ORM 模型，与数据库表 certificates 对齐。

使用 from app.database 引入的 SA-Version；Integer 在 MySQL 下映射为 BIGINT
（足够容纳现有数据），在 SQLite 下原生支持自增，避免 BigInteger 在 SQLite
不生成 AUTOINCREMENT 的兼容问题。
"""
from sqlalchemy import Column, Date, DateTime, Integer, String

from app.database import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(255), nullable=False, unique=True)
    expiry_date = Column(Date, nullable=False)
    creator = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    modifier = Column(String(255), nullable=False)
    modified_at = Column(DateTime, nullable=False)
    # 数据库中该列为 NOT NULL，但业务接口未暴露，创建时给默认值
    credential_id = Column(String(255), nullable=False, default="default-credential")
