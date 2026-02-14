from langchain_ollama import ChatOllama


def connect_ollama_llm(
    model: str, base_url: str | None = None, temperature: float | None = None
) -> ChatOllama:
    """连接 Ollama LLM"""

    params = {'model': model}
    params['base_url'] = base_url or r'http://localhost:11434'
    if temperature is not None:
        params['temperature'] = temperature
    return ChatOllama(**params)
