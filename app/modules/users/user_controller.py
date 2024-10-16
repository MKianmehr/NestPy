# modules/users/user_controller.py

from app.core.decorators import Controller, Get, Post
from app.modules.users.user_service import UserService
from typing import Dict


@Controller(prefix="/user")
class UserController:
    """
    Controller for handling user-related API endpoints.
    """

    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    @Get("/me")
    def get_me(self) -> Dict[str, str]:
        """
        Endpoint to retrieve current user's info.

        Returns:
            Dict[str, str]: Information about the current user.
        """
        return {"username": "john_doe"}

    @Post("/")
    def create_user(self, username: str) -> Dict[str, str]:
        """
        Endpoint to create a new user.

        Args:
            username (str): The username of the user to be created.

        Returns:
            Dict[str, str]: The created user.
        """
        return self.user_service.create_user(username)
