from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# In-memory "database"
energy_readings = []

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EnergyData(BaseModel):
    voltage: float
    current: float
    power: float
    kwh: float

@app.post("/data")
def receive_data(data: EnergyData):
    print(f"Received: {data}")
    energy_readings.append(data)
    return {"status": "success", "data": data}

@app.get("/data")
def get_data():
    return energy_readings[-10:]  # return last 10 readings (or modify as needed)
