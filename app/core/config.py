# from pydantic import BaseSettings, Field
# import logging


# class Settings(BaseSettings):
#     """
#     Application configuration settings, leveraging Pydantic for parsing environment variables.
#     """

#     # Application settings
#     APP_NAME: str = "NestPy-FastAPI Application"
#     APP_VERSION: str = "1.0.0"

#     # Environment settings
#     # Options: development, production, testing
#     ENVIRONMENT: str = Field("development", env="ENVIRONMENT")

#     # Server settings
#     HOST: str = Field("0.0.0.0", env="HOST")
#     PORT: int = Field(8000, env="PORT")

#     # Database settings
#     # Expected to be set in the environment
#     DATABASE_URL: str = Field(..., env="DATABASE_URL")

#     # JWT and Security settings (Example)
#     SECRET_KEY: str = Field("supersecretkey", env="SECRET_KEY")
#     ALGORITHM: str = Field("HS256", env="ALGORITHM")
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
#         30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

#     # Logging settings
#     LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")

#     class Config:
#         env_file = ".env"  # Specify where the environment variables are loaded from


# # Create a settings instance to use throughout the application
# settings = Settings()

# # Configure logging
# logging.basicConfig(
#     level=settings.LOG_LEVEL,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
