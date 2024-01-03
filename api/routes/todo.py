from fastapi import APIRouter,HTTPException,status
from api.models.todo import Todo
from api.schemas.todo import GetTodo,PostTodo,PutTodo

todo_router =  APIRouter(prefix="/api",tags=["Todo"])

@todo_router.get("/")
async def all_todo():
    return await GetTodo.from_queryset(Todo.all())

@todo_router.post("/")
async def post_todo(body: PostTodo):
    data = body.model_dump(exclude_unset=True)
    row = await Todo.create(data)
    return await GetTodo.from_tortoise_orm(row)
    