# NestPy Project

**NestPy** is a Python-based project inspired by NestJS, aiming to create a modular, maintainable, and dependency-injected backend architecture using **FastAPI**. This project leverages custom decorators, a dependency injection container, and the powerful features of FastAPI to provide an experience similar to NestJS in Python.

## Features

- **Custom Dependency Injection Container** (`ServiceContainer`) to handle service registration, singleton, and transient scopes.
- **Decorator-based approach** to build and organize services, controllers, and modules.
- **Integration with FastAPI's `Depends`** for clean and modular dependency injection.
- **Modular Architecture** similar to NestJS, supporting scalable development.

## Project Structure

- `app/`
  - `core/`
    - `di.py`: The dependency injection container implementation.
    - `decorators/`: Custom decorators like `@Controller`, `@Module`, etc.
  - `modules/`: Example modules, each containing controllers, services, and other necessary components.

## Getting Started

### Prerequisites

- **Python 3.11+**
- **FastAPI**: Install FastAPI with the following command:

  ```sh
  pip install fastapi uvicorn
  ```

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/MKianmehr/NestPy.git
   cd nestpy
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

### Running the Project

To run the project with **Uvicorn**:

```sh
uvicorn main:app --reload
```

### Example Usage

Define a service and register it in the `ServiceContainer`:

```python
from app.core.di import ServiceContainer, Injectable, ServiceScope

@Injectable(scope=ServiceScope.SINGLETON)
class UserService:
    def __init__(self):
        self.users = [{"username": "john_doe"}, {"username": "jane_doe"}]

    def get_users(self):
        return self.users
```

Integrate the service with a FastAPI endpoint:

```python
from fastapi import Depends, FastAPI
from app.core.di import resolve_dependency

app = FastAPI()

@app.get("/users/")
def get_users(user_service: UserService = Depends(resolve_dependency(UserService))):
    return user_service.get_users()
```

### Dependency Injection

`ServiceContainer` provides a way to manage the lifecycle of services:

- **Singleton Scope** (`ServiceScope.SINGLETON`): A single instance of the service is created and shared.
- **Transient Scope** (`ServiceScope.TRANSIENT`): A new instance is created for each request.

Use the `@Injectable` decorator to register services:

```python
@Injectable(scope=ServiceScope.TRANSIENT)
class ReportService:
    def generate_report(self):
        return "Report generated"
```

### Using Custom Decorators

Custom decorators are used to replicate NestJS-like syntax for controllers and modules:

```python
from app.core.decorators import Controller, Get

@Controller(prefix="/user")
class UserController:
    def __init__(self, user_service: UserService = Depends(resolve_dependency(UserService))):
        self.user_service = user_service

    @Get("/")
    def get_users(self):
        return self.user_service.get_users()
```

### Modular Architecture

You can group related controllers and services into modules using the `@Module` decorator:

```python
from app.core.decorators import Module

@Module(controllers=[UserController], providers=[UserService])
class UserModule:
    pass
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### Issues

If you encounter any issues, please open an issue on the [GitHub repository](https://github.com/MKianmehr/NestPy/issues).

## License

This project is licensed under the MIT License.

