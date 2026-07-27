"""FastAPI 应用入口。

启动：uvicorn app.main:app --host 0.0.0.0 --port 8081
Swagger 文档：http://localhost:8081/api/docs
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import API_PREFIX
from app.database import Base, engine
from app.interfaces.certificate_controller import router as certificate_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 开发期自动建表（已存在的表不会被重建）；生产可关闭
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="证书管理后端 (Python)",
    description="Spring Boot 后端的 Python (FastAPI) 等价实现，接口保持兼容。",
    version="1.0.0",
    docs_url=f"{API_PREFIX}/docs",
    openapi_url=f"{API_PREFIX}/openapi.json",
    lifespan=lifespan,
)

# CORS：允许前端开发服务器访问，对齐 Java 版 CorsConfig
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(certificate_router)


@app.get(f"{API_PREFIX}/health")
def health():
    from app.result import Result

    return Result.success(data={"status": "UP"})
