from fastapi import FastAPI, BackgroundTasks, HTTPException
from models import InferenceRequest, InferenceResult
from database import db_instance
from worker import process_queue

app = FastAPI(title="Distributed ML Inference Node")

@app.post("/api/v1/predict", status_code=202)
async def submit_prediction(request: InferenceRequest, background_tasks: BackgroundTasks):
    task_id = db_instance.insert_task(request.model_dump())
    background_tasks.add_task(process_queue, task_id, request.model_dump())
    return {"task_id": task_id, "status": "processing"}

@app.get("/api/v1/result/{task_id}", response_model=InferenceResult)
async def get_result(task_id: str):
    task_data = db_instance.get_task(task_id)
    if not task_data:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_data["status"] == "pending":
        return InferenceResult(
            task_id=task_id,
            status="pending",
            confidence_score=0.0,
            bounding_boxes=[]
        )
        
    return InferenceResult(
        task_id=task_id,
        status="completed",
        **task_data["result"]
    )
