from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: bool


@app.get("/tasks")
async def read_tasks(request: Request):
    global tasks
    return {'tasks': tasks}

@app.get("/tasks/{task_id}")
async def read_tasks(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            return tasks[i]
    return HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
            tasks[i].id = task_id       
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            return {"item_id": tasks.pop(i)}
    return HTTPException(status_code=404, detail="Task not found")



