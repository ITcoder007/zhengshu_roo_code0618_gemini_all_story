# 项目初始化指南

## 项目结构
本项目采用Monorepo结构，包含:
- `backend`: Spring Boot 2.7.x后端应用
- `frontend`: Vue 3.x前端应用

## 环境要求
- JDK 11+
- Node.js 16+
- Maven 3.6+
- npm 8+

## 安装依赖
### 后端
```bash
cd backend
mvn install
```

### 前端
```bash
cd frontend
npm install
```

## 启动项目
### 后端
```bash
cd backend
mvn spring-boot:run
```

### 前端
```bash
cd frontend
npm run dev
```

## 开发说明
- 后端默认运行在: http://localhost:8080
- 前端默认运行在: http://localhost:3000