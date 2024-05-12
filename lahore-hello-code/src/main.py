from fastapi import FastAPI
import requests

app = FastAPI()


def my_first_api_call():
    call_api = requests.get("http://order-api:8000/")
    return call_api.json()


@app.get("/")
def read_root():
    api_call = my_first_api_call()
    return {"Multiple Microsefvices!!": api_call}
