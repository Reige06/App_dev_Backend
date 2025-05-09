from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed origins instead of "*" for more security
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
    return {"status": "success", "data": data}
