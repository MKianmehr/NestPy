from typing import Callable, TypeVar
from enum import Enum
import types

# Define a generic TypeVar for type safety, preserving the function signature
F = TypeVar('F', bound=Callable)


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"


def route(method: HTTPMethod) -> Callable[[str], Callable[[F], F]]:
    """
    Factory function to create a route decorator for a specific HTTP method.

    Args:
        method (HTTPMethod): The HTTP method for the route (e.g., GET, POST).

    Returns:
        Callable[[str], Callable[[F], F]]: A decorator that takes a path and decorates a function
                                           with the route configuration.
    """
    def decorator_factory(path: str) -> Callable[[F], F]:
        """
        A decorator for defining a route with a given HTTP method and path.

        Args:
            path (str): The path for the route.

        Returns:
            Callable[[F], F]: The decorated function with route configuration metadata.
        """
        def decorator(func: F) -> F:
            # Ensure the decorator is applied only to functions
            if not isinstance(func, types.FunctionType):
                raise TypeError(
                    f"@{method.name} decorator can only be applied to functions, not to '{type(func).__name__}'.")

            # Attach route configuration to the function
            func._route_config = (path, method.value)
            return func
        return decorator

    return decorator_factory


# Define HTTP route decorators
Get = route(HTTPMethod.GET)
Post = route(HTTPMethod.POST)
Put = route(HTTPMethod.PUT)
Delete = route(HTTPMethod.DELETE)
Patch = route(HTTPMethod.PATCH)
Options = route(HTTPMethod.OPTIONS)
