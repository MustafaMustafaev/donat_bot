from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    YOOKASSA_SHOP_ID: str
    YOOKASSA_SECRET_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()



