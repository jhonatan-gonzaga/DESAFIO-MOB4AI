from fastapi import APIRouter
from sqlalchemy import create_engine, Colum, String, Integer
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db")

base = declarative_base()

#criar as classes/tabelas de banco
class processes(base):
    __tablename__ = "processes"

    timestamp = Colum("timestamp", Integer, primary_Key=True, autoincrement=True)
    uid = Colum("uid", Integer)
    package_name = Colum("package_name", String)
    usagetime = Colum("usagetime", int)
    cpu_usage = Colum("cpu_usage", float)
    rx_data = Colum("rx_data", Integer)
    tx_data = Colum("tx_data", Integer)


order_router = APIRouter(prefix="/GET", tags="GET")

@order_router.get("/processes")
async def processes():
    resposta = await processes.get(base)
    dados = resposta.json()
    return {
        "timestamp" : resposta.timestamp,
        "uid" : resposta.nome,
        "package_name" : resposta.usagetime,
        "usagetime" : resposta.cpu_usage,
        "rx_data" : resposta.rx_data,
        "tx_data" : resposta.tx_data
    }