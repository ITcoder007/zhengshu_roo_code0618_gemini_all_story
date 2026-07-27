"""证书 REST 控制器，路由前缀 /api/certificates，对齐 Java 版。"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.certificate_service import CertificateService
from app.database import get_db
from app.result import Result
from app.schemas import CertificateCreate, CertificateUpdate

router = APIRouter(prefix="/api/certificates", tags=["certificates"])


@router.get("")
def list_certificates(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    """分页列表。对齐前端调用 ?page=&size=。"""
    service = CertificateService(db)
    data = service.list_page(current=page, size=size)
    return Result.success(data=data)


@router.get("/{cert_id}")
def get_certificate(cert_id: int, db: Session = Depends(get_db)):
    service = CertificateService(db)
    data = service.get_by_id(cert_id)
    # Java 版对不存在的 id 返回 data:null；这里保持兼容
    return Result.success(data=data)


@router.post("")
def create_certificate(payload: CertificateCreate, db: Session = Depends(get_db)):
    service = CertificateService(db)
    try:
        data = service.create(payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="域名已存在")
    return Result.success(data=data)


@router.put("/{cert_id}")
def update_certificate(
    cert_id: int, payload: CertificateUpdate, db: Session = Depends(get_db)
):
    service = CertificateService(db)
    try:
        data = service.update(cert_id, payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="域名已存在")
    if data is None:
        raise HTTPException(status_code=404, detail="证书不存在")
    return Result.success(data=data)


@router.delete("/{cert_id}")
def delete_certificate(cert_id: int, db: Session = Depends(get_db)):
    service = CertificateService(db)
    ok = service.delete(cert_id)
    if not ok:
        raise HTTPException(status_code=404, detail="证书不存在")
    return Result.success(message="删除成功")
