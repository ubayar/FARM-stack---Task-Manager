from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

#App object
app = FastAPI()

origins = ['https://localhost:300']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1

@app.post("/api/todo")
async def post_todo(todo):
    return 1

@app.put("/api/todo{id}")
async def put_todo(id, data):
    return 1

@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1

# if __name__ == '__main__':
#     uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)