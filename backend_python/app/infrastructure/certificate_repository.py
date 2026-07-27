"""证书仓储：封装数据库访问与审计字段自动填充。

相比 Java 版，这里修正了两个问题：
1. 自动填充 created_at / modified_at（Java 版缺失导致创建 500）。
2. 真实计算分页 total/pages（Java 版分页拦截器未配置导致恒为 0）。
"""
from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Certificate


class CertificateRepository:
    def __init__(self, db: Session):
        self.db = db

    def _by_id(self, cert_id: int) -> Optional[Certificate]:
        return self.db.get(Certificate, cert_id)

    def get_by_id(self, cert_id: int) -> Optional[Certificate]:
        return self._by_id(cert_id)

    def list_page(self, current: int, size: int) -> Tuple[List[Certificate], int]:
        """分页查询：返回 (记录列表, 总数)。"""
        total = self.db.scalar(select(func.count()).select_from(Certificate)) or 0
        offset = (current - 1) * size
        stmt = (
            select(Certificate)
            .order_by(Certificate.id.desc())
            .offset(offset)
            .limit(size)
        )
        records = list(self.db.scalars(stmt).all())
        return records, total

    def create(self, cert: Certificate) -> Certificate:
        """插入，自动填充审计时间。"""
        now = datetime.now()
        cert.created_at = now
        cert.modified_at = now
        if not cert.credential_id:
            cert.credential_id = "default-credential"
        self.db.add(cert)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        self.db.refresh(cert)
        return cert

    def update(self, cert_id: int, data: dict) -> Optional[Certificate]:
        """按 id 更新，自动刷新 modified_at/modifier。"""
        cert = self._by_id(cert_id)
        if cert is None:
            return None
        for key in ("domain", "expiry_date", "modifier"):
            if data.get(key) is not None:
                setattr(cert, key, data[key])
        cert.modified_at = datetime.now()
        self.db.commit()
        self.db.refresh(cert)
        return cert

    def delete(self, cert_id: int) -> bool:
        cert = self._by_id(cert_id)
        if cert is None:
            return False
        self.db.delete(cert)
        self.db.commit()
        return True
