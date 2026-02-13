from enum import Enum

from pydantic import BaseModel


# 意图相关
class IntentClassification(str, Enum):
    """枚举，意图类别"""

    IntuitionLayer = 'intuition_layer'  # 直觉层
    RoutineLayer = 'routine_layer'  # 常规层
    InferenceLayer = 'inference_layer'  # 推理层


class Intent(BaseModel):
    """数据模型，意图"""

    intent: IntentClassification
