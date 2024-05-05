from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Multiple MicrosefvicesCool Just Added Volume!!": "5 MAY"}
