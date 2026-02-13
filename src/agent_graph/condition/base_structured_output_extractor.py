from abc import ABC, abstractmethod
from logging import getLogger
from textwrap import dedent
from traceback import format_exc
from typing import Any, Type

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel

logger = getLogger(__name__)


class BaseStructuredOutputExtractor(ABC):
    """抽象基类，结构化输出提取器"""

    @property
    @abstractmethod
    def OUTPUT_SCHEMA(self) -> Type[BaseModel]:
        """输出模式"""

        pass

    @property
    @abstractmethod
    def SYSTEM_PROMPT(self) -> str:
        """系统提示词"""

        pass

    def __init__(self, llm: BaseChatModel):
        self._llm = llm
        try:
            self._llm_with_structured_output = self._llm.with_structured_output(
                self.OUTPUT_SCHEMA
            )
        except Exception:
            self._llm_with_structured_output = self._llm
            logger.warning(
                f'<BaseStructuredOutputExtractor>初始化 LLM 结构化输出功能报错！！！\n{format_exc()}'
            )

    def _get_partial_variables(self) -> dict[str, Any]:
        """获取部分变量，提供系统提示词中部分变量的值"""

        return {}

    def get_extractor_chain(self) -> RunnableSequence:
        """获取提取器链"""

        chat_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', dedent(self.SYSTEM_PROMPT)),
                ('human', '{input}'),
            ]
        )
        if partial_variables := self._get_partial_variables():
            chat_prompt = chat_prompt.partial(**partial_variables)
        return chat_prompt | self._llm_with_structured_output
