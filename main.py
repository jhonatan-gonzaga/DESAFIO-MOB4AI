from fastapi import FastAPI, HTTPException
from typing import Union
app = FastAPI()

from order_routes import order_router

app.include_router(order_router)