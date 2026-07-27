"""Pydantic 数据契约（输入/输出），字段使用驼峰命名对齐前端。

数据库列为 snake_case（expiry_date、created_at），但 Java 版开启了
map-underscore-to-camel-case，前端期望 expiryDate、createdAt 等驼峰字段。
这里通过 alias 实现蛇形->驼峰映射，输出时统一使用别名。
"""
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


def to_camel(snake: str) -> str:
    parts = snake.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


class CamelModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,   # 既接受蛇形也接受驼峰
        from_attributes=True,    # 支持从 ORM 对象构造
    )


class CertificateBase(CamelModel):
    domain: str
    expiry_date: date = Field(alias="expiryDate")
    creator: str
    modifier: str


class CertificateCreate(CertificateBase):
    """创建请求体。creator/modifier 由调用方传入，缺失时默认为 system。"""

    creator: str = "system"
    modifier: str = "system"


class CertificateUpdate(CamelModel):
    """更新请求体，部分字段可选。"""

    domain: Optional[str] = None
    expiry_date: Optional[date] = Field(default=None, alias="expiryDate")
    modifier: str = "system"


class CertificateOut(CamelModel):
    id: int
    domain: str
    expiry_date: date
    creator: str
    created_at: datetime
    modifier: str
    modified_at: datetime

    def to_dict(self) -> dict:
        """输出驼峰命名的字典，时间格式与 Java 版一致（无时区，T 分隔）。"""
        return {
            "id": self.id,
            "domain": self.domain,
            "expiryDate": self.expiry_date.isoformat(),
            "creator": self.creator,
            "createdAt": self.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
            "modifier": self.modifier,
            "modifiedAt": self.modified_at.strftime("%Y-%m-%dT%H:%M:%S"),
        }


class PageData(CamelModel):
    """分页数据，对齐 MyBatis-Plus 的 IPage 结构。"""

    records: List[dict]
    total: int
    size: int
    current: int
    pages: int
