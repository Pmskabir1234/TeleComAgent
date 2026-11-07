from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from src.shared.config.settings import settings
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from typing import List

def get_llm():
    """
    Returns the configured LLM provider.
    To minimize tokens, we use Groq for fast, efficient inference.
    """
    if settings.AI_PROVIDER == "groq":
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_ID,
            temperature=0
        )
    elif settings.AI_PROVIDER == "hf":
        # Using OpenAI-compatible interface for HF endpoints
        return ChatOpenAI(
            api_key=settings.HF_TOKEN,
            base_url="https://api-inference.huggingface.co/v1",
            model_name=settings.MODEL_ID,
            temperature=0
        )
    else:
        raise ValueError(f"Unsupported AI provider: {settings.AI_PROVIDER}")
