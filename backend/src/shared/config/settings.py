import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # General
    PROJECT_NAME: str = "Telecom AI Assistant"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./telecom_assistant.db")

    # AI Config
    # Use GROQ_API_KEY or HF_TOKEN
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    HF_TOKEN: Optional[str] = os.getenv("HF_TOKEN")

    # Model Choice: 'groq' or 'hf'
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "groq")

    # Model IDs
    # Example Groq: llama-3.1-70b-versatile
    # Example HF: meta-llama/Llama-3.1-8B-Instruct
    MODEL_ID: str = os.getenv("MODEL_ID", "llama-3.1-70b-versatile")

    class Config:
        env_file = ".env"

settings = Settings()
