from fastapi import FastAPI
from routers.articulos import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(router)

app.title = "Tienda de Musica"
app.summary = "Venta de instrumentos"
app.version = "0.0"

