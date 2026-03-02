from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4o-mini"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 100
    RETRIEVAL_TOP_K: int = 3
    CV_PATH: str = "cv.pdf"
    LOG_LEVEL: str = "INFO"
    OUTPUT_FILE: str = "output.txt"

    class Config:
        env_file = ".env"

settings = Settings()
