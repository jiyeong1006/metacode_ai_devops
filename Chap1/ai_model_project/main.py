from fastapi import FastAPI
from faker import Faker
from redis_client import set_key_value, get_key_value

app = FastAPI()
fake = Faker()

@app.get("/")
def read_root():
    return {"message": "Hello, Docker + FastAPI!"}

@app.get("/fake-data")
def get_fake_data():
    return {"name": fake.name(), "email": fake.email(), "address": fake.address()}

@app.post("/set/{key}/{value}")
def set_data(key: str, value: str):
    set_key_value(key, value)
    return {"status": "success", "key": key, "value": value}

@app.get("/get/{key}")
def get_data(key: str):
    value = get_key_value(key)
    if value:
        return {"key": key, "value": value.decode("utf-8")}
    return {"key": key, "value": None, "message": "Key not found"}
