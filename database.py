import uuid
from datetime import datetime

class MockVectorDB:
    def __init__(self):
        self.store = {}

    def insert_task(self, request_data):
        task_id = str(uuid.uuid4())
        self.store[task_id] = {
            "request": request_data,
            "status": "pending",
            "created_at": datetime.now()
        }
        return task_id

    def update_task(self, task_id, result):
        if task_id in self.store:
            self.store[task_id]["status"] = "completed"
            self.store[task_id]["result"] = result
            self.store[task_id]["updated_at"] = datetime.now()

    def get_task(self, task_id):
        return self.store.get(task_id)

db_instance = MockVectorDB()
