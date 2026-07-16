import asyncio
import random
from database import db_instance
from datetime import datetime

async def process_queue(task_id: str, request_data: dict):
    await asyncio.sleep(random.uniform(1.0, 3.0))
    
    mock_result = {
        "confidence_score": round(random.uniform(0.85, 0.99), 4),
        "bounding_boxes": [
            [10, 20, 150, 200],
            [45, 80, 220, 310]
        ],
        "processed_at": datetime.now()
    }
    
    db_instance.update_task(task_id, mock_result)
