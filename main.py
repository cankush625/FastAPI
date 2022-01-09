from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello() -> str:
    """Add some description to display in the project docs"""
    
    return "hello"
