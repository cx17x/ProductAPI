from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        # DSN
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=r"D:\ProductAPI_now\src\.env")


settings = Settings()
# print(settings.DATABASE_URL)

# .env
# DB_HOST=localhost
# DB_PORT=5432
# DB_USER=postgres
# DB_PASS=1234
# DB_NAME=mydb