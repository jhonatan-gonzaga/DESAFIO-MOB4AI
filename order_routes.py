from fastapi import APIRouter, Query
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

db = create_engine("sqlite:///lives.db")
metadata = MetaData()
metadata.reflect(bind=db)

processes_table = Table("processes", metadata, autoload_with=db)

Session = sessionmaker(bind=db)
order_router = APIRouter(prefix="/GET", tags=["GET"])

@order_router.get("/processes")
async def get_processes(start: int = Query(...), end: int = Query(...)):
    """
    Retorna os registros com timestamp entre start e end.
    """
    session = Session()
    resultado = []

    colunas_desejadas = ["timestamp", "uid", "package_name", "usagetime", "cpu_usage", "rx_data", "tx_data"]

    # filtra pelo intervalo de timestamp
    query = session.execute(
        processes_table.select().where(
            processes_table.c.timestamp >= start,
            processes_table.c.timestamp <= end
        )
    ).fetchall()

    for row in query:
        registro = {col: row[col] for col in colunas_desejadas}
        resultado.append(registro)

    session.close()
    return resultado
