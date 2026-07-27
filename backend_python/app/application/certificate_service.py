"""证书应用服务：业务编排，调用仓储完成增删改查。"""
import math
from typing import List

from sqlalchemy.orm import Session

from app.infrastructure.certificate_repository import CertificateRepository
from app.models import Certificate
from app.schemas import CertificateCreate, CertificateUpdate


class CertificateService:
    def __init__(self, db: Session):
        self.repo = CertificateRepository(db)

    def list_page(self, current: int = 1, size: int = 10):
        if current < 1:
            current = 1
        if size < 1:
            size = 10
        records, total = self.repo.list_page(current, size)
        pages = math.ceil(total / size) if total else 0
        return {
            "records": [self._to_dict(r) for r in records],
            "total": total,
            "size": size,
            "current": current,
            "pages": pages,
        }

    def get_by_id(self, cert_id: int):
        cert = self.repo.get_by_id(cert_id)
        return self._to_dict(cert) if cert else None

    def create(self, payload: CertificateCreate):
        cert = Certificate(
            domain=payload.domain,
            expiry_date=payload.expiry_date,
            creator=payload.creator,
            modifier=payload.modifier,
        )
        saved = self.repo.create(cert)
        return self._to_dict(saved)

    def update(self, cert_id: int, payload: CertificateUpdate):
        data = payload.model_dump(exclude_unset=True, by_alias=False)
        cert = self.repo.update(cert_id, data)
        return self._to_dict(cert) if cert else None

    def delete(self, cert_id: int) -> bool:
        return self.repo.delete(cert_id)

    @staticmethod
    def _to_dict(cert: Certificate) -> dict:
        return {
            "id": cert.id,
            "domain": cert.domain,
            "expiryDate": cert.expiry_date.isoformat(),
            "creator": cert.creator,
            "createdAt": cert.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
            "modifier": cert.modifier,
            "modifiedAt": cert.modified_at.strftime("%Y-%m-%dT%H:%M:%S"),
        }
