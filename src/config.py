from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME: str = "previsao_preco_aluguel"
    VERSION: str = "1.0.0"

    # Caminhos
    BASE_DIR = Path(__file__).resolve().parent.parent
    ARTIFACTS_DIR = BASE_DIR / "artifacts"

    # Parâmetros (Ridge)
    ALPHA: float = 1.0

    class Config:
        env_file = ".env"

settings = Settings()

# Criando os Diretórios
settings.ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)