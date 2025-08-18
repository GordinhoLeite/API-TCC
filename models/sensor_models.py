from pydantic import BaseModel, Field

# ✅ Modelo de dados para receber as leituras dos sensores
# O FastAPI usa este modelo para validar os dados recebidos na requisição
class SensorData(BaseModel):
    sensorID: str
    temperatura: float
    umidade: float  # ✅ Novo campo para a umidade
    distancia: float

# ✅ Modelo de dados para controlar o estado da ventoinha
class VentoinhaState(BaseModel):
    estado: str = Field(..., pattern="^(ligado|desligado)$")
