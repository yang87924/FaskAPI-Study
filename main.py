from fastapi import FastAPI
from Controller.userController import router as userControllerRouter
from Controller.articleController import router as articleControllerRouter

app = FastAPI()
app.include_router(userControllerRouter, prefix="/user")
app.include_router(articleControllerRouter, prefix="/article")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}