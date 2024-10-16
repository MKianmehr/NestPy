# from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self) -> None:
        self.db_url = "settings.DATABASE_URL"
        logger.info(
            f"UserService initialized with database URL: {self.db_url}")

    def create_user(self, username: str) -> dict:
        # Example of using the config in a service
        user = {"username": username}
        logger.info(f"User '{username}' created.")
        return user
