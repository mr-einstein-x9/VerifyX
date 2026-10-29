from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "VerifyX"
    ENV: str = "development"
    DATABASE_URL: str = "postgresql+asyncpg://verifyx:verifyx_dev_password@localhost:5433/verifyx"
    TEST_DATABASE_URL: str = (
        "postgresql+asyncpg://verifyx:verifyx_dev_password@localhost:5433/verifyx_test"
    )

    JWT_SECRET: str = "dev_secret_key_change_me_to_at_least_32_bytes_long_random_hex"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    REDIS_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
