
from typing import Callable, Type, TypeVar
from app.core.di import ServiceContainer, ServiceScope

T = TypeVar('T')


def Injectable(scope: ServiceScope = ServiceScope.SINGLETON) -> Callable[[Type[T]], Type[T]]:
    """
    A decorator for registering classes as services in a dependency injection container.

    Args:
        scope (ServiceScope): The lifecycle scope of the service. Options are SINGLETON or TRANSIENT.

    Returns:
        Callable[[Type[T]], Type[T]]: A class decorator that registers the given class with the specified scope.
    """
    def decorator(cls: Type[T]) -> Type[T]:
        if not isinstance(cls, type):
            raise TypeError(
                "The @Injectable decorator should be applied to a class.")

        # Register the class in the ServiceContainer with the specified scope
        ServiceContainer.register(cls.__name__, cls, scope.value)

        return cls

    return decorator
