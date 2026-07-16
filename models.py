from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class InferenceRequest(BaseModel):
    image_id: str
    model_version: str
    priority: int

class InferenceResult(BaseModel):
    task_id: str
    status: str
    confidence_score: float
    bounding_boxes: List[List[int]]
    processed_at: Optional[datetime] = None
