# modules/users/user_module.py

from app.core.decorators import Module
from app.modules.users.user_controller import UserController
from app.modules.users.user_service import UserService


@Module(controllers=[UserController], providers=[UserService])
class UserModule:
    """
    Module for user-related features, encapsulating the controller and service.
    """
    pass
