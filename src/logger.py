import logging
import sys
from src.config import settings

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Se não existir o Logger, será criado
    if not logger.handlers:
        logger.setLevel(level=logging.INFO)     # inserir apenas informações
        formatter = logging.Formatter(
            fmt = "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
            datefmt = "%Y-%m-%d %H:%M:%S"
        )

        # Handler Console
        console_handler = logging.StreamHandler(sys.stdout)     # saída enviada para o Terminal
        console_handler.setFormatter(fmt=formatter)
        logger.addHandler(hdlr=console_handler)

        # Handler Arquivo
        file_handler = logging.FileHandler(filename=settings.LOGS_DIR / "mle_pipeline.log")     # local de armazenamento dos logs
        file_handler.setFormatter(fmt=formatter)
        logger.addHandler(file_handler)

    return logger