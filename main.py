import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def helloworld():
    return "Hello World"

if __name__=='__main__':
    uvicorn.run("main:app",host='127.0.0.1', port=5000, reload=False, )