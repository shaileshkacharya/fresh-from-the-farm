from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Fresh From The Farm API"
    environment: str = "development"
    debug: bool = True
    secret_key: str
    jwt_secret: str
    database_url: str
    redis_url: str

    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
