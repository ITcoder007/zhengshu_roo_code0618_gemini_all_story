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
