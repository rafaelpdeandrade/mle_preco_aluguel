from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import ClassVar

class Settings(BaseSettings):
    PROJECT_NAME: str = "previsao_preco_aluguel"
    VERSION: str = "1.0.0"

    # Caminhos
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent
    ARTIFACTS_DIR: ClassVar[Path] = BASE_DIR / "artifacts"
    LOGS_DIR: ClassVar[Path] = BASE_DIR / "logs"
    

    # Parâmetros (Ridge)
    ALPHA: float = 1.0

    # Configurações
    settings_config_dict = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

# Criando os Diretórios
settings.ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)