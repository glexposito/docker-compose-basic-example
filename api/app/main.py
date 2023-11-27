from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"


@app.get("/colors")
def read_colors():
    return ["Red", "Blue", "Yellow"]