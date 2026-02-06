from pydantic import BaseModel
from typing import Optional

class SensorData(BaseModel):
    sensorID: str
    temperatura: float
    umidade: float
    distancia: float
    volume: Optional[float] = 0.0      # Campo volume adicionado
    porcentagem: Optional[float] = 0.0 # Campo porcentagem adicionado

class VentoinhaState(BaseModel):
    estado: str # "ligado" ou "desligado"