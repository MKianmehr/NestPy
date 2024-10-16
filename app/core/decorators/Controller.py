from typing import Callable, Type, Optional


def Controller(prefix: str = "", description: Optional[str] = None) -> Callable[[Type], Type]:
    """
    A decorator to define a controller for handling API endpoints.

    This decorator adds a prefix to all routes within the class, grouping them logically under the same path.

    Args:
        prefix (str): The prefix to be used for all routes defined in the class (e.g., "/user").
        description (Optional[str]): Optional description for the controller, useful for documentation purposes.

    Returns:
        Callable[[Type], Type]: A class decorator that adds the specified prefix and metadata to the class.
    """
    def decorator(cls: Type) -> Type:
        if not isinstance(cls, type):
            raise TypeError(
                "The @Controller decorator should be applied to a class.")

        # Attach prefix and optional description to the class
        cls._prefix = prefix
        cls._description = description

        return cls

    return decorator
