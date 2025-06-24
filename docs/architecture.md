
# 证书生命周期管理系统 架构文档 - v1.0 (最终完整版)

| 日期 | 版本 | 描述 | 作者 |
| :--- | :------ | :---------- | :----- |
| 2025-06-19 | 1.0 | 最终版本，包含所有已确认的设计和API全部细节。 | Winston (Architect) |

## 1. 高层级架构

### 1.1 技术摘要
本系统将采用一个基于Java的**单体（Monolithic）后端**和一个独立的**Vue.js前端**，并通过**REST API**进行通信。整体部署在**单个服务器**上，数据库采用**MySQL**。架构遵循**领域驱动设计（DDD）**原则，以确保业务逻辑的清晰和未来的可扩展性。项目将存放于一个**Monorepo**仓库中，以便于统一管理和本地开发。

### 1.2 高层级概述
根据PRD中的技术假设，我们确定了以下核心架构决策：
* **仓库结构**: Monorepo，用于简化开发和调试流程。
* **服务架构**: 单体架构，这对于MVP阶段来说可以最大化开发效率，同时内部采用DDD分层以保证代码质量。

### 1.3 高层级项目图
```mermaid
graph TD
    A[用户] -->|浏览器| B(前端应用 - Vue.js);
    B -->|REST API 调用| C{后端服务 (Spring Boot)};
    C -->|JDBC| D[(MySQL数据库)];

    subgraph "服务器 (Linux VPS)"
        direction LR
        C;
        D;
    end
````

### 1.4 架构与设计模式

- **领域驱动设计 (DDD)**: 作为核心架构模式，指导我们构建清晰的领域层、应用层和基础设施层。
- **RESTful API**: 作为前后端通信的标准。
- **统一响应体模式**: 所有API返回的数据都将封装在一个标准结构中，包含状态码、消息和数据本身。
- **仓库模式 (Repository Pattern)**: 在基础设施层使用，用于将数据访问逻辑与领域模型解耦。

## 2. 技术栈

### 2.1 云基础设施

- **[建议]** 对于MVP阶段，为了控制成本和简化部署，我建议将前后端和数据库统一部署在**一台云服务器（Linux VPS）**上。

### 2.2 技术栈详情表

|   |   |   |   |
|---|---|---|---|
|**类别**|**技术选型**|**版本**|**用途**|
|**后端语言**|Java|JDK 8|核心后端业务逻辑开发。|
|**后端框架**|Spring Boot|2.7.x|快速构建企业级后端应用。|
|**后端构建**|Maven|(最新稳定版)|项目依赖管理与构建。|
|**数据访问**|MybatisPlus|3.5.x|简化数据库CRUD操作。|
|**前端框架**|Vue.js|3.x|构建用户界面。|
|**前端测试**|Jest|(最新稳定版)|前端单元测试与TDD。|
|**数据库**|MySQL|8.0|持久化存储证书数据。|
|**API规范**|Swagger (OpenAPI)|3.0.x|API文档的定义与展示。|
|**开发模式**|TDD (测试驱动开发)|N/A|保证代码质量的开发方法。|

## 3. 数据模型 (Data Models)

### 3.1 Certificate (证书实体)

- **用途**: 代表系统所管理的核心资产，即一张SSL证书的元数据。
- **关键属性**: `id`, `domain`, `expiryDate`, `creator`, `createdAt`, `modifier`, `modifiedAt`。

## 4. 系统组件 (Components)

- **前端应用 (Frontend Application)**: Vue.js应用，负责UI渲染和用户交互。
- **后端应用 (Backend Application)**: Spring Boot单体应用，负责API、业务逻辑和数据持久化，内部遵循DDD分层。

## 5. 外部API (External APIs)

根据产品需求文档，本项目MVP阶段**不依赖任何外部第三方API**。

## 6. REST API 规格 (可读版)

### 6.1 API端点总览

|   |   |   |   |   |
|---|---|---|---|---|
|**HTTP方法**|**路径**|**说明**|**请求体/参数**|**主要响应状态码**|
|`POST`|`/api/certificates`|添加新证书|`CertificateInput` JSON|201, 400|
|`GET`|`/api/certificates`|获取证书列表（分页+搜索）|`page`, `size`, `sortBy`|200|
|`GET`|`/api/certificates/{id}`|获取单个证书详情|`id` (路径参数)|200, 404|
|`PUT`|`/api/certificates/{id}`|更新证书信息|`id`, `CertificateInput` JSON|200, 400, 404|
|`DELETE`|`/api/certificates/{id}`|删除证书|`id` (路径参数)|200 (或204), 404|

### 6.2 API详细说明

#### **6.2.1 创建新证书**

- **URL:** `/api/certificates`
- **方法:** `POST`
- **描述:** 用于提交一个新的证书元数据。
- **请求体:**
    
    JSON
    
    ```
    {
      "domain": "new-example.com",
      "expiryDate": "2025-12-31"
    }
    ```
    
- **响应成功 (201 Created):**
    
    JSON
    
    ```
    {
      "code": 201,
      "message": "创建成功",
      "data": {
        "id": 2,
        "domain": "new-example.com",
        "expiryDate": "2025-12-31",
        "creator": "user_a",
        "createdAt": "2025-06-19T18:30:00",
        "modifier": "user_a",
        "modifiedAt": "2025-06-19T18:30:00"
      }
    }
    ```
    

#### **6.2.2 获取证书列表（含搜索）**

- **URL:** `/api/certificates`
- **方法:** `GET`
- **描述:** 返回证书列表，支持分页、排序和域名模糊搜索。
- **请求参数:**
    - `page`: `integer` - 页码，默认0。
    - `size`: `integer` - 每页记录数，默认10。
    - `sortBy`: `string` - 排序字段，默认`expiryDate`。
    - `sortOrder`: `string` - 排序方向，`asc`或`desc`，默认`asc`。
    - `search`: `string` - 域名模糊搜索关键词，可选。
- **响应成功 (200 OK):**
    
    JSON
    
    ```
    {
      "code": 200,
      "message": "查询成功",
      "data": {
        "content": [
          {
            "id": 1,
            "domain": "example.com",
            "expiryDate": "2025-08-20",
            "creator": "user_a",
            "createdAt": "2025-06-18T10:00:00",
            "modifier": "user_a",
            "modifiedAt": "2025-06-18T10:00:00"
          }
        ],
        "totalElements": 1,
        "totalPages": 1,
        "size": 10,
        "number": 0
      }
    }
    ```
    

#### **6.2.3 获取单个证书详情**

- **URL:** `/api/certificates/{id}`
- **方法:** `GET`
- **描述:** 返回指定ID的证书详细信息。
- **响应成功 (200 OK):**
    
    JSON
    
    ```
    {
      "code": 200,
      "message": "查询成功",
      "data": {
        "id": 1,
        "domain": "example.com",
        "expiryDate": "2025-08-20",
        "creator": "user_a",
        "createdAt": "2025-06-18T10:00:00",
        "modifier": "user_a",
        "modifiedAt": "2025-06-18T10:00:00"
      }
    }
    ```
    
- **响应失败 (404 Not Found):**
    
    JSON
    
    ```
    {
      "code": 404,
      "message": "证书不存在",
      "data": null
    }
    ```
    

#### **6.2.4 更新证书信息**

- **URL:** `/api/certificates/{id}`
- **方法:** `PUT`
- **描述:** 更新一个已存在的证书元数据。
- **请求体:**
    
    JSON
    
    ```
    {
      "domain": "updated-example.com",
      "expiryDate": "2026-01-15"
    }
    ```
    
- **响应成功 (200 OK):**
    
    JSON
    
    ```
    {
      "code": 200,
      "message": "更新成功",
      "data": {
        "id": 1,
        "domain": "updated-example.com",
        "expiryDate": "2026-01-15",
        "creator": "user_a",
        "createdAt": "2025-06-18T10:00:00",
        "modifier": "user_b",
        "modifiedAt": "2025-06-19T18:35:00"
      }
    }
    ```
    

#### **6.2.5 删除证书**

- **URL:** `/api/certificates/{id}`
- **方法:** `DELETE`
- **描述:** 删除一个指定的证书。
- **响应成功 (200 OK):**
    
    JSON
    
    ```
    {
      "code": 200,
      "message": "删除成功",
      "data": "ID为1的证书已被删除"
    }
    ```
    

## 7. 数据库表结构 (Database Schema)

SQL

```
CREATE TABLE `certificates` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `domain` VARCHAR(255) NOT NULL COMMENT '证书域名',
  `expiry_date` DATE NOT NULL COMMENT '过期日期',
  `creator` VARCHAR(255) NOT NULL COMMENT '创建人',
  `created_at` DATETIME NOT NULL COMMENT '创建时间',
  `modifier` VARCHAR(255) NOT NULL COMMENT '修改人',
  `modified_at` DATETIME NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_domain` (`domain`) COMMENT '域名唯一约束'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='证书元数据表';
```

## 8. 源代码结构 (Source Tree)

Plaintext

```
/certificate-manager-monorepo
|
|-- /backend                   # 后端Spring Boot应用
|   |-- /src
|   |   |-- /main/java/com/example/certman
|   |   |   |-- /domain         # 领域层
|   |   |   |-- /application    # 应用层
|   |   |   |-- /infrastructure # 基础设施层
|   |   |   `-- /interfaces     # 接口层
|   `-- pom.xml
|
|-- /frontend                  # 前端Vue应用
|   |-- /src
|   |   |-- /components
|   |   |-- /views
|   |   `-- /services
|   `-- package.json
|
`-- README.md
```
