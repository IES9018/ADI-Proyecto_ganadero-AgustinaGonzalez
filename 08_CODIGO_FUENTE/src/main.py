from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.get("/animales")
def animales_page():
    return FileResponse("templates/animales.html")

@app.get("/sanidad")
def sanidad_page():
    return FileResponse("templates/sanidad.html")

from routes.animal_routes import router as animal_router
from routes.sanidad_routes import router as sanidad_router

app.include_router(animal_router)
app.include_router(sanidad_router)