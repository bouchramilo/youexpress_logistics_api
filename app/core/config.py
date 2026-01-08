from pydantic import Field
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # Database
    db_host: str = Field(default="db", alias="DB_HOST")
    db_port: int = Field(default=5432, alias="DB_PORT")
    db_name: str = Field(default="youexpress_db", alias="DB_NAME")
    db_user: str = Field(default="user", alias="DB_USER")
    db_password: str = Field(default="password", alias="DB_PASSWORD")

    # Application
    secret_key: str = Field(default="your-secret-key-here", alias="SECRET_KEY")
    debug: bool = Field(default=True, alias="DEBUG")

    # API
    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")

    class Config:
        env_file = ".env"
        populate_by_name = True  # Permet d'utiliser les alias

    @property
    def database_url(self) -> str:
        # Use DATABASE_URL if set (e.g., from docker-compose), else construct from fields
        return os.getenv("DATABASE_URL") or f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
