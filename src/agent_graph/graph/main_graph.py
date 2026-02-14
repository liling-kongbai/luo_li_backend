from functools import partial

from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.graph import END, START, StateGraph

from ..condition import intent_classifier_condition
from ..node import chat_node, intent_classifier_entry_node
from ..type import IntentClassification


async def create_main_graph_builder(llm: BaseChatModel):
    """创建主图构建器"""

    builder = StateGraph()

    # 添加节点
    builder.add_node('intent_classifier_entry_node', intent_classifier_entry_node)
    builder.add_node('chat_node', chat_node)

    # 添加边
    builder.add_edge(START, 'intent_classifier_entry_node')
    builder.add_conditional_edges(
        'intent_classifier_entry_node',
        partial(intent_classifier_condition, llm=llm),
        {
            IntentClassification.IntuitionLayer: 'chat_node',
            IntentClassification.RoutineLayer: 'chat_node',
            IntentClassification.InferenceLayer: 'chat_node',
        },
    )

    builder.add_edge('chat_node', END)
    return builder
