from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig


async def chat_node(state, config: RunnableConfig, llm: BaseChatModel) -> dict:
    """对话节点"""

    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', '{system_prompt}'),
            MessagesPlaceholder(variable_name='messages'),
        ]
    )
    chain = chat_prompt_template | llm
    response = await chain.ainvoke(
        {
            'system_prompt': state.system_prompt,
            'messages': state.messages,
        },
        config,
    )
    return {'messages': response}
