from fastapi import FastAPI

app = FastAPI()


@app.get("/colours")
def read_colours():
    return {["Red", "Blue", "Yellow"]}