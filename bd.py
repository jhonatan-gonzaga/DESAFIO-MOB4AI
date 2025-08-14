from fastapi import Query

@order_router.get("/processes")
async def get_processes(start: int = Query(None), end: int = Query(None)):
    """
    Retorna registros filtrando pelo timestamp se start e end forem fornecidos.
    """
    session = Session()
    resultado = []

    colunas_desejadas = ["timestamp", "uid", "package_name", "usagetime", "cpu_usage", "rx_data", "tx_data"]

    query_stmt = processes_table.select()

    if start is not None and end is not None:
        query_stmt = query_stmt.where(
            processes_table.c.timestamp >= start,
            processes_table.c.timestamp <= end
        )

    query = session.execute(query_stmt).fetchall()

    for row in query:
        registro = {col: row[col] for col in colunas_desejadas}
        resultado.append(registro)

    session.close()
    return resultado
