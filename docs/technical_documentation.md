# Technical Documentation - Certificate Lifecycle Management System
 
## 1. Project Overview
 
The Certificate Lifecycle Management System is a web-based application designed to streamline the management and monitoring of SSL/TLS certificates. The primary goal is to prevent service disruptions caused by expired certificates by providing a centralized platform for tracking certificate metadata, monitoring their validity, and managing their entire lifecycle.
 
### 1.1 Purpose and Goals
 
- **Prevent Certificate Expiration:** Eliminate service outages caused by unexpected SSL/TLS certificate expiration.
- **Centralized Management:** Offer a single dashboard to view, track, and manage all certificates across multiple domains.
- **Automated Monitoring:** Reduce the manual effort required to check certificate status.
- **Asset Visibility:** Provide a clear and concise overview of all certificate assets and their health status.
 
### 1.2 Key Features
 
- **Certificate CRUD:** Full support for creating, reading, updating, and deleting certificate metadata.
- **Audit Trails:** Automatically track changes with fields for `creator`, `createdAt`, `modifier`, and `modifiedAt`.
- **Asset Dashboard:** A user-friendly interface to display a list of all certificates, their domain, issuer, validity, and current status.
 
## 2. Backend Architecture
 
The backend is a monolithic application built with Java and the Spring Boot framework. It follows the principles of Domain-Driven Design (DDD) to ensure a clean and maintainable codebase.
 
### 2.1 Technology Stack
 
| Category          | Technology        | Version      | Purpose                                      |
|-------------------|-------------------|--------------|----------------------------------------------|
| **Language**      | Java              | 1.8          | Core backend business logic                  |
| **Framework**     | Spring Boot       | 2.7.18       | Rapid application development                |
| **Build Tool**    | Maven             |              | Dependency management and project build      |
| **Data Access**   | MyBatis-Plus      | 3.5.6        | Simplified database CRUD operations          |
| **Database**      | MySQL             | 8.0.33       | Data persistence for certificate information |
 
### 2.2 Project Structure
 
The backend code is organized into four main packages, reflecting the layers of Domain-Driven Design:
 
```
/backend/src/main/java/com/example/certificate/
|-- /domain         # Domain Layer: Contains the core business logic and entities, such as the Certificate model.
|-- /application    # Application Layer: Orchestrates domain objects to perform application-specific tasks.
|-- /infrastructure # Infrastructure Layer: Handles technical concerns like database access and external services.
|-- /interfaces     # Interfaces Layer: Exposes the application's functionality via RESTful APIs.
```
 
### 2.3 Main Components

- **CertificateController:** The main entry point for all API requests related to certificates. It handles HTTP requests and delegates to the `CertificateService`.
- **CertificateService:** The application service that orchestrates the business logic for certificate management.
- **CertificateRepository:** The repository responsible for all database operations related to the `Certificate` entity.
- **Certificate (Entity):** The core domain model representing a certificate's metadata.

## 3. Frontend Architecture

The frontend is a single-page application (SPA) built with Vue.js. It is responsible for rendering the user interface and interacting with the backend via RESTful API calls.

### 3.1 Technology Stack

| Category          | Technology        | Version      | Purpose                                      |
|-------------------|-------------------|--------------|----------------------------------------------|
| **Framework**     | Vue.js            | 3.x          | Building the user interface                  |
| **Build Tool**    | Vite              |              | Fast development and optimized builds        |
| **Language**      | TypeScript        | ~5.8.3       | Type safety and improved developer experience|
| **HTTP Client**   | Axios             | ^1.10.0      | Making API requests to the backend           |
| **Routing**       | Vue Router        | ^4.5.1       | Managing client-side routing                 |
| **Testing**       | Jest              | ^29.7.0      | Unit and component testing                   |

### 3.2 Project Structure

The frontend code is organized into the following directories:

```
/frontend/src/
|-- /components     # Reusable Vue components.
|-- /views          # Main page components, such as the CertificateList.
|-- /services       # API service modules for communicating with the backend.
|-- /router         # Client-side routing configuration.
```

### 3.3 Main Components

- **CertificateList.vue:** The main view component that displays the list of certificates and handles user interactions such as adding, editing, and deleting certificates.
- **api.ts:** The service module that configures the Axios client and defines functions for making API calls to the backend.
- **router/index.ts:** The routing configuration file that maps URL paths to their corresponding view components.

## 4. API Endpoints

The backend provides a RESTful API for managing certificates. All endpoints are prefixed with `/certificates`.

### 4.1 Create Certificate

- **Endpoint:** `POST /certificates`
- **Description:** Adds a new certificate to the system.
- **Request Body:**
  ```json
  {
    "domain": "example.com",
    "expiryDate": "2025-12-31"
  }
  ```
- **Response (200 OK):** The newly created certificate object.

### 4.2 List Certificates

- **Endpoint:** `GET /certificates`
- **Description:** Retrieves a paginated list of all certificates.
- **Query Parameters:**
  - `page` (optional, default: 1): The page number to retrieve.
  - `size` (optional, default: 10): The number of certificates per page.
- **Response (200 OK):** A paginated list of certificate objects.

### 4.3 Get Certificate by ID

- **Endpoint:** `GET /certificates/{id}`
- **Description:** Retrieves a single certificate by its unique ID.
- **Path Parameter:**
  - `id`: The ID of the certificate to retrieve.
- **Response (200 OK):** The requested certificate object.
- **Response (404 Not Found):** If the certificate with the specified ID does not exist.

### 4.4 Update Certificate

- **Endpoint:** `PUT /certificates/{id}`
- **Description:** Updates the details of an existing certificate.
- **Path Parameter:**
  - `id`: The ID of the certificate to update.
- **Request Body:**
  ```json
  {
    "domain": "updated-example.com",
    "expiryDate": "2026-01-15"
  }
  ```
- **Response (200 OK):** The updated certificate object.
- **Response (404 Not Found):** If the certificate with the specified ID does not exist.

### 4.5 Delete Certificate

- **Endpoint:** `DELETE /certificates/{id}`
- **Description:** Deletes a certificate from the system.
- **Path Parameter:**
  - `id`: The ID of the certificate to delete.
- **Response (200 OK):** A success message.
- **Response (404 Not Found):** If the certificate with the specified ID does not exist.

## 5. Database Schema

The application uses a MySQL database to store certificate information. The schema is defined as follows:

### 5.1 `certificates` Table

```sql
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



