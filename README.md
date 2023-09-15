# Corporate Asset Tracking System

**Project Description:**

The Corporate Asset Tracking System is a Django web application designed to efficiently manage and track corporate assets distributed to employees within organizations. This comprehensive system simplifies the management of a wide range of assets, including phones, tablets, laptops, and various equipment. By streamlining asset tracking, the system enhances accountability, reduces losses, and ensures the smooth operation of corporate asset management.


## Table of Contents
1. [Authentication](#authentication)
2. [Company Registration and Authentication](#company-registration-and-authentication)
   - [Company Registration](#1-company-registration)
   - [Company Login](#2-company-login)
3. [Employee Management](#employee-management)
   - [Add Employee](#3-add-employee)
   - [List Employees](#4-list-employees)
4. [Device Management](#device-management)
   - [Add Device](#5-add-device)
   - [List Devices](#6-list-devices)
5. [Device Log and Return](#device-log-and-return)
   - [Add Device Log Entry](#7-add-device-log-entry)
   - [Return Device](#8-return-device)


## Company Registration and Authentication

### 1. Company Registration

- **Endpoint:** `/company/register/`
- **Description:** Register a new company account.
- **HTTP Method:** `POST`
```
{
    "email": "company@example.com",
    "password": "your-password",
    "company_name": "Company Name"
}
```

### 2. Company Login

- **Endpoint:** `/company/login/`
- **Description:** Log in to an existing company account.
- **HTTP Method:** `POST`
```
{
  "token": "your-auth-token"
}
```

## Employee Management

### 3. Add Employee

- **Endpoint:** `/employee/add/`
- **Description:** Add a new employee to your company.
- **HTTP Method:** `POST`
```
{
  "first_name": "John",
  "last_name": "Doe",
  "contact_email": "johndoe@example.com"
}
```
- **Example Response:**
```
{
  "message": "Employee added successfully."
}
```

### 4. List Employees

- **Endpoint:** `/employee/list/`
- **Description:** Retrieve a list of all employees within your company.
- **HTTP Method:** `GET`
- **Example Response:**
```
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "contact_email": "johndoe@example.com",
    "company": 1
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "contact_email": "janesmith@example.com",
    "company": 1
  }
]
```

## Device Management

### 5. Add Device

- **Endpoint:** `/device/add/`
- **Description:** Add a new device to your company's assets.
- **HTTP Method:** `POST`
-  **Example Request:**
```
POST /device/add/
Authorization: Token <your-auth-token>
Content-Type: application/json

{
  "serial_number": "D12345",
  "name": "Laptop",
  "description": "Dell Latitude E7450",
  "condition": "Good"
}
```
- **Example Response:**
```
{
  "message": "Device added successfully."
}
```

### 6. List Devices

- **Endpoint:** `/device/list/`
- **Description:** Retrieve a list of all devices owned by your company.
- **HTTP Method:** `GET`
-  **Example Request:**
```
GET /device/list/
Authorization: Token <your-auth-token>
```
- **Example Response:**
```
[
  {
    "id": 101,
    "serial_number": "D12345",
    "name": "Laptop",
    "description": "Dell Latitude E7450",
    "condition": "Good"
  },
  {
    "id": 102,
    "serial_number": "P98765",
    "name": "Phone",
    "description": "iPhone 12",
    "condition": "Excellent"
  }
]
```
## Device Log and Return

### 7. Add Device Log Entry

- **Endpoint:** `/device/log/add/`
- **Description:** Add a log entry for a device when it is assigned to an employee.
- **HTTP Method:** `POST`
- **Example Request:**
```
POST /device/log/add/
Authorization: Token <your-auth-token>
Content-Type: application/json

{
  "device_id": 101,
  "employee_id": 1,
  "condition": "Good"
}
```
- **Example Response:**
```
{
  "message": "Device log entry added successfully."
}
```

### 8. Return Device

- **Endpoint:** `/device/log/return/`
- **Description:** Mark a device as returned by an employee and update the log entry.
- **HTTP Method:** `POST`
- **Example Request:**
```
POST /device/log/return/
Authorization: Token <your-auth-token>
Content-Type: application/json
{
  "id": 1",
  "returned_condition": "GOOD"
}
```
- **Example Response:**
```
{
  "message": "Device returned successfully."
}
```
