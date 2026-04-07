import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    
    # UI Constants
    APP_TITLE: str = "AgentLens"
    APP_TAGLINE: str = "AI-Powered LLM Discovery Assistant"
    APP_DESCRIPTION: str = "An end-to-end engineering project designed to help developers and researchers navigate the rapidly evolving landscape of Large Language Models (LLMs)."

settings = Settings()

# Alias for backward compatibility
OPENAI_API_KEY = settings.OPENAI_API_KEY
OLLAMA_HOST = settings.OLLAMA_HOST
APP_TITLE = settings.APP_TITLE
APP_TAGLINE = settings.APP_TAGLINE
APP_DESCRIPTION = settings.APP_DESCRIPTION
