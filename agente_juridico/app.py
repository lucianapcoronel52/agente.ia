from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Analizador Normativo",
    description="Sistema de análisis de cumplimiento normativo",
    version="0.1.0"
)

# Carpeta donde están las páginas HTML
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



@app.get("/api/estado")
async def estado():
    return {
        "estado": "ok",
        "mensaje": "El Analizador Normativo está funcionando"
    }
