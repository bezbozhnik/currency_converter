from typing import Any

from pydantic_settings import BaseSettings

from src.constants import Environment


class Config(BaseSettings):
    SITE_DOMAIN: str
    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]
    ENVIRONMENT: Environment = Environment.TESTING
    APP_VERSION: str = "1"

    EXCHANGERATE_API_KEY: str
    CONVERTER_SERVICE: str = "https://v6.exchangerate-api.com/v6/"

    @property
    def converter_service_url(self) -> str:
        return f"{self.CONVERTER_SERVICE + self.EXCHANGERATE_API_KEY}/pair/"


settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}

if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/api/v{settings.APP_VERSION}"
else:
    app_configs["root_path"] = "/api"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
