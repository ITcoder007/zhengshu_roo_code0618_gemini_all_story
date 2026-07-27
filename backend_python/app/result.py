"""统一返回信封，对齐 Java 版 Result：{code, message, data}。"""
from typing import Any, Optional

from pydantic import BaseModel


class Result(BaseModel):
    code: int = 200
    message: str = "成功"
    data: Optional[Any] = None

    @classmethod
    def success(cls, data: Any = None, message: str = "成功") -> "Result":
        return cls(code=200, message=message, data=data)

    @classmethod
    def error(cls, message: str = "失败", code: int = 500) -> "Result":
        return cls(code=code, message=message, data=None)
