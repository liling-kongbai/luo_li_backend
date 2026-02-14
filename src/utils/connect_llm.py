from os import getenv

from langchain_deepseek import ChatDeepSeek
from langchain_ollama import ChatOllama
from pydantic import SecretStr


def connect_ollama_llm(
    model: str, base_url: str | None = None, temperature: float | None = None
) -> ChatOllama:
    """连接 Ollama LLM"""

    params = {'model': model}
    params['base_url'] = base_url or r'http://localhost:11434'
    if temperature is not None:
        params['temperature'] = temperature
    return ChatOllama(**params)


def connect_deepseek_llm(
    model: str, api_key: SecretStr | None = None, temperature: float | None = None
) -> ChatDeepSeek:
    """连接 DeepSeek LLM"""

    params = {'model': model}
    params['api_key'] = api_key or getenv('DEEPSEEK_API_KEY')
    if temperature is not None:
        params['temperature'] = temperature
    return ChatDeepSeek(**params)
