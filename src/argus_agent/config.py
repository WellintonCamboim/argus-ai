from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    anthropic_api_key: str = ""

    openrouter_api_key: str = ""
    openrouter_model: str = "nvidia/nemotron-3.5-lightning:free"

    grafana_url: str = ""
    grafana_api_key: str = ""

    database_url: str = ""


settings = Settings()
