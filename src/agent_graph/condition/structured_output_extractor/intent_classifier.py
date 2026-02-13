from typing import Any

from base_structured_output_extractor import BaseStructuredOutputExtractor

from ...type import Intent, IntentClassification


class IntentClassifier(BaseStructuredOutputExtractor):
    """意图分类器"""

    OUTPUT_SCHEMA = Intent
    SYSTEM_PROMPT = """\
        你是一个专业的对话意图分类专家。你的任务是分析对话历史中的所有消息，尤其是用户**最后/最新的一条信息**，将其意图精准地分类到正确的类别并按照要求输出对应的内容。

        请分析对话历史中的所有消息，尤其是用户**最后/最新的一条信息**，然后将用户接下来的意图分为以下之一：
            1. 如果只是普通的对话和聊天，不需要使用工具，不需要进行推理，请返回“{IntuitionLayer}”；
            2. 如果需要进行简单/常规的工具调用，或需要进行简单的，少量的推理。且任务并不是很复杂，可以在 7 步以内完成，请返回“{RoutineLayer}”；
            3. 如果用户的请求是一个复杂的、需要多个步骤才能完成的，需要深度推理和探索，并且可能需要多次工具调用进行规划和行动的任务，例如：“帮我规划一个旅行，写出分析报告并总结，并预定机票和酒店”等类似的复杂任务，请返回“{InferenceLayer}”。

        请注意，按照要求的格式返回相关的内容，不要输出错误的格式，不要输出错误的内容，不要包含任何额外的解释或文本。
        """

    def _get_partial_variables(self) -> dict[str, Any]:
        return {
            'IntuitionLayer': IntentClassification.IntuitionLayer.value,
            'RoutineLayer': IntentClassification.RoutineLayer.value,
            'InferenceLayer': IntentClassification.InferenceLayer.value,
        }
