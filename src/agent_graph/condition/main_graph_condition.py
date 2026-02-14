from logging import getLogger
from traceback import format_exc

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.runnables import RunnableConfig

from ..type import IntentClassification
from .structured_output_extractor import IntentClassifier

logger = getLogger(__name__)


async def intent_classifier_condition(
    state, config: RunnableConfig, llm: BaseChatModel
) -> IntentClassification:
    """意图分类器条件"""

    try:
        chain = IntentClassifier(llm).get_extractor_chain()
        result = await chain.ainvoke(
            {
                'messages': state.messages,
            },
            config,
        )
        return result.intent
    except Exception:
        logger.error(
            f'<intent_classifier_condition>意图分类器条件报错！！！\n{format_exc()}'
        )
        return IntentClassification.IntuitionLayer
