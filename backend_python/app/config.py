"""应用配置。可通过环境变量覆盖默认值。"""
import os


def _env(key: str, default: str) -> str:
    return os.getenv(key, default)


# 数据库配置（默认对齐 Java 版 application.yml）
DB_HOST = _env("DB_HOST", "localhost")
DB_PORT = _env("DB_PORT", "3306")
DB_USER = _env("DB_USER", "root")
DB_PASSWORD = _env("DB_PASSWORD", "root")
DB_NAME = _env("DB_NAME", "cert_claude_code0624_roo")

# 运行端口与 context-path 与 Java 版保持一致
APP_HOST = _env("APP_HOST", "0.0.0.0")
APP_PORT = int(_env("APP_PORT", "8081"))
API_PREFIX = "/api"

# 仅当未设置 DATABASE_URL 时按上面的 MySQL 配置拼装；测试可注入 SQLite URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4",
)
