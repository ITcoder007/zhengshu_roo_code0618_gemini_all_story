# 证书管理后端（Python / FastAPI）

Spring Boot（`../backend`）后端的 Python 等价实现，REST 接口与数据格式保持兼容，
并修复了原 Java 版的两个问题：分页 `total/pages` 恒为 0、创建时审计字段缺失导致 500。

## 技术栈

- FastAPI 0.115（Web 框架）
- SQLAlchemy 2.0（ORM）
- PyMySQL（MySQL 驱动）
- Pydantic 2（数据校验）
- Uvicorn（ASGI 服务器）
- pytest + httpx（测试，默认使用 SQLite 内存库，无需 MySQL）

## 目录结构（DDD 风格，对齐 Java 版分层）

```
backend_python/
├── app/
│   ├── main.py                              # FastAPI 入口、CORS、健康检查
│   ├── config.py                            # 配置（环境变量）
│   ├── database.py                          # SQLAlchemy 引擎/会话
│   ├── models.py                            # ORM 模型 Certificate
│   ├── result.py                            # 统一响应信封 Result
│   ├── schemas.py                           # Pydantic 输入输出契约（驼峰命名）
│   ├── application/certificate_service.py   # 应用服务（业务编排）
│   ├── infrastructure/certificate_repository.py  # 仓储（数据库访问 + 审计填充）
│   └── interfaces/certificate_controller.py # REST 控制器
├── tests/
│   ├── conftest.py                          # pytest 夹具（SQLite 内存库）
│   └── test_certificate.py                  # 接口端到端测试
├── requirements.txt
└── README.md
```

## 快速开始

```bash
cd backend_python
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 运行测试（使用 SQLite 内存库，无需 MySQL）
pytest -v

# 启动开发服务（连接 MySQL，默认 localhost:3306，库 cert_claude_code0624_roo）
uvicorn app.main:app --host 0.0.0.0 --port 8081
```

- Swagger 文档：`http://localhost:8081/api/docs`
- 健康检查：`http://localhost:8081/api/health`

## 配置（环境变量）

| 变量            | 默认值                              | 说明                |
| --------------- | ----------------------------------- | ------------------- |
| `DB_HOST`       | `localhost`                         | MySQL 主机          |
| `DB_PORT`       | `3306`                              | MySQL 端口          |
| `DB_USER`       | `root`                              | MySQL 用户          |
| `DB_PASSWORD`   | `root`                              | MySQL 密码          |
| `DB_NAME`       | `cert_claude_code0624_roo`          | 数据库名            |
| `DATABASE_URL`  | （由上述拼装的 MySQL URL）          | 覆盖整条连接字符串  |
| `APP_HOST`      | `0.0.0.0`                           | 监听地址            |
| `APP_PORT`      | `8081`                              | 监听端口            |

> 注：用 `uvicorn` CLI 启动时，端口以 `--port` 参数为准；环境变量 `APP_PORT`
> 适用于以 `python -c "import uvicorn; uvicorn.run(...)"` 方式启动的场景。

## REST API（前缀 `/api/certificates`，与 Java 版一致）

| 方法     | 路径                  | 说明                          |
| -------- | --------------------- | ----------------------------- |
| `GET`    | `/?page=&size=`       | 分页列表（`records/total/size/current/pages`） |
| `GET`    | `/{id}`               | 详情，不存在时 `data:null`    |
| `POST`   | `/`                   | 创建，自动填充审计时间        |
| `PUT`    | `/{id}`               | 更新，自动刷新 `modifiedAt`   |
| `DELETE` | `/{id}`               | 删除                          |

统一响应格式：`{"code":200,"message":"成功","data":...}`

字段使用驼峰命名（`expiryDate`、`createdAt`、`modifiedAt`），与前端约定一致。
