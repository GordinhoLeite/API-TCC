from fastapi import APIRouter
from models.sensor_models import SensorData
from datetime import datetime, timezone, timedelta
from firebase_config import get_firestore_client

router = APIRouter()

@router.post("/sensores")
async def receber_dados(data: SensorData):
    try:
        db = get_firestore_client()
        fuso_mt = timezone(timedelta(hours=-4))
        agora = datetime.now(fuso_mt)
        data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

        payload = {
            "temperatura": data.temperatura,
            "umidade": data.umidade,
            "distancia": data.distancia,
            "volume": data.volume,
            "porcentagem": data.porcentagem,
            "data": data_formatada
        }

        # Atualiza tempo real
        db.collection("sensores").document(data.sensorID).set(payload, merge=True)

        # Adiciona ao histórico
        historico_payload = payload.copy()
        historico_payload["sensorID"] = data.sensorID
        db.collection("sensores").document(data.sensorID).collection("leituras").add(historico_payload)

        return {"status": "sucesso", "porcentagem": data.porcentagem}

    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}