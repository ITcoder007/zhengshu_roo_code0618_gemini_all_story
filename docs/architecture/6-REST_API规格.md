# 6. REST API规格 (API Specifications)

## 6.1 证书资源接口
### GET /api/certificates
- 功能: 获取证书列表
- 参数:
  - `status`: 过滤状态(active/expired)
  - `page`: 分页页码
- 响应示例:
```json
{
  "data": [
    {
      "id": "cert_123",
      "domain": "example.com",
      "expiryDate": "2025-12-31"
    }
  ],
  "total": 1
}
```

### POST /api/certificates
- 功能: 创建新证书
- 请求体:
```json
{
  "domain": "new.example.com",
  "validityDays": 90
}