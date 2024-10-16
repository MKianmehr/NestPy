from fastapi import APIRouter
from typing import Callable, List, Type, TypeVar
from app.core.di import ServiceContainer
from inspect import isclass

# Define a generic TypeVar for better type safety
T = TypeVar("T")


def Module(controllers: List[Type] = None, providers: List[Type] = None) -> Callable[[Type[T]], Type[T]]:
    """
    A decorator for defining a module that encapsulates controllers and providers for a cohesive unit in a FastAPI application.

    Args:
        controllers (List[Type]): A list of controller classes to register within the module.
        providers (List[Type]): A list of provider classes to register with the dependency injection container.

    Returns:
        Callable[[Type[T]], Type[T]]: A class decorator that adds a FastAPI APIRouter instance containing 
                                      the routes from the specified controllers and attaches it to the module.
    """
    controllers = controllers or []
    providers = providers or []

    # Validate inputs
    if not all(isclass(controller) for controller in controllers):
        raise TypeError("All items in the controllers list must be classes.")
    if not all(isclass(provider) for provider in providers):
        raise TypeError("All items in the providers list must be classes.")

    def decorator(module_cls: Type[T]) -> Type[T]:
        # Create an APIRouter instance
        router = APIRouter()

        # Register providers with the DI container
        for provider in providers:
            ServiceContainer.register(provider.__name__, provider)

        # Register controllers and add their routes to the APIRouter
        for controller in controllers:
            controller_instance = ServiceContainer.resolve(controller)

            # Validate that the controller has a prefix attribute
            prefix = getattr(controller_instance, "_prefix", None)
            if prefix is None:
                raise AttributeError(
                    f"Controller {controller.__name__} must have a '_prefix' attribute defined.")

            # Iterate over the controller methods to register the routes
            for attr_name in dir(controller_instance):
                attr = getattr(controller_instance, attr_name)
                if callable(attr) and hasattr(attr, "_route_config"):
                    path, method = attr._route_config

                    # Construct the full path for the route
                    full_path = f"{prefix}{path}"

                    # Register the route with the APIRouter
                    router.add_api_route(
                        full_path,
                        attr,
                        methods=[method],
                        summary=getattr(attr, "__doc__", "").strip().split(
                            "\n")[0] if attr.__doc__ else None
                    )

        # Attach the router to the module class
        module_cls.router = router
        return module_cls

    return decorator
