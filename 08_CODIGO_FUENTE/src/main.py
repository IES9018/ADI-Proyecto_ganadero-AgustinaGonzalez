from fastapi import FastAPI
from presentacion.api.routes import router

app = FastAPI(title="Ganadapp - Sistema de Gestión Ganadera")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}