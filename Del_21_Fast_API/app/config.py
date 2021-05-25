from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    PROJECT_DESCRIPTION: str = Field(..., env="PROJECT_DESCRIPTION")
    VERSION: str = Field(..., env="VERSION")
    API_V1_STR: str = Field(..., env="API_V1_STR")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7dni
    ALGORITHM: str = "HS256"

    class Config:
        case_sensitive = True


settings = Settings()
