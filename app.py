from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
fake_database = []

@app.get("/todos")
async def get_all_todos():
    return fake_database

@app. post("/todos")
async def create_todos(request: Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo

@app.patch("/todos/{ID}")
async def updated_by_ID(ID: int, request: Request):
    todo_update = await request.json()
    for todo in fake_database:
        if todo["id"] == ID:
            todo.update(todo_update)
            return todo,200
    return None,404
        
@app. delete("/todos/{ID}")
async def delete_todo_by_id(ID: int, request: Request):
    fake_database.pop(ID)

