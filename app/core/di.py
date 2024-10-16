import inspect
from typing import Dict, Type, Any
from enum import Enum
import logging

# Set up logging for better diagnostics
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ServiceScope(Enum):
    SINGLETON = "singleton"
    TRANSIENT = "transient"


class ServiceContainer:
    # The dictionary to hold registered services
    _services: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def register(cls, key: str, provider: Type, scope: ServiceScope = ServiceScope.SINGLETON) -> None:
        """
        Registers a service with the DI container.

        Args:
            key (str): The key to register the service with.
            provider (Type): The class type of the provider.
            scope (ServiceScope): The scope of the service, either SINGLETON or TRANSIENT.

        Raises:
            ValueError: If the service key is already registered.
        """
        if key in cls._services:
            raise ValueError(
                f"Service '{key}' is already registered in the DI container.")

        cls._services[key] = {
            "provider": provider,
            "scope": scope,
            "instance": None  # Used for SINGLETON instances
        }
        logger.info(f"Service '{key}' registered with scope '{scope.name}'.")

    @classmethod
    def get(cls, key: str) -> Any:
        """
        Gets a service instance from the DI container.

        Args:
            key (str): The key of the service to retrieve.

        Returns:
            Any: An instance of the requested service.

        Raises:
            ValueError: If the service is not registered.
        """
        if key not in cls._services:
            raise ValueError(
                f"Service '{key}' is not registered in the DI container.")

        service_info = cls._services[key]
        return cls._get_instance(service_info)

    @classmethod
    def resolve(cls, cls_type: Type) -> Any:
        """
        Resolves a class type by automatically injecting its dependencies.

        Args:
            cls_type (Type): The class type to resolve.

        Returns:
            Any: An instance of the resolved class type.

        Raises:
            ValueError: If any required dependency is not registered.
        """
        logger.info(f"Resolving dependencies for '{cls_type.__name__}'.")
        signature = inspect.signature(cls_type.__init__)
        dependencies = cls._get_dependencies(signature)

        return cls_type(**dependencies)

    @classmethod
    def _get_instance(cls, service_info: Dict[str, Any]) -> Any:
        """
        Retrieves or creates an instance of the service based on its scope.

        Args:
            service_info (Dict[str, Any]): The service metadata containing provider, scope, and instance.

        Returns:
            Any: An instance of the requested service.
        """
        if service_info["scope"] == ServiceScope.SINGLETON:
            if service_info["instance"] is None:
                service_info["instance"] = cls.resolve(
                    service_info["provider"])
            return service_info["instance"]

        elif service_info["scope"] == ServiceScope.TRANSIENT:
            return cls.resolve(service_info["provider"])

    @classmethod
    def _get_dependencies(cls, signature: inspect.Signature) -> Dict[str, Any]:
        """
        Retrieves dependencies for a given class constructor.

        Args:
            signature (inspect.Signature): The signature of the class constructor.

        Returns:
            Dict[str, Any]: A dictionary of resolved dependencies.

        Raises:
            ValueError: If a required dependency is not registered in the DI container.
        """
        dependencies = {}
        for name, param in signature.parameters.items():
            if name == "self" or param.annotation == inspect.Parameter.empty:
                continue

            dependency_key = param.annotation.__name__
            if dependency_key not in cls._services:
                raise ValueError(
                    f"Dependency '{dependency_key}' is not registered in the DI container.")

            dependencies[name] = cls.get(dependency_key)
            logger.info(
                f"Injected dependency '{dependency_key}' for parameter '{name}'.")

        return dependencies
