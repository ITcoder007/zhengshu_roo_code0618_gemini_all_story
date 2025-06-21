# 5. 外部API (External APIs)

## 5.1 证书颁发机构(CA)接口
- **Let's Encrypt API**:
  - 功能: 自动签发免费SSL证书
  - 认证方式: ACME协议
  - 限流: 50次/周/域名

- **DigiCert API**:
  - 功能: 签发商业SSL证书
  - 认证方式: OAuth2.0
  - 错误码: 
    - 400: 无效请求
    - 429: 请求过多