from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EnergyData(BaseModel):
    voltage: float
    current: float
    power: float
    kwh: float

@app.post("/data")
def receive_data(data: EnergyData):
    print(f"Received: {data}")
    return {"status": "success", "data": data}