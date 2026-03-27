"""
Taskflow Sistema De Gestion De Proyectos - API REST
Generado por ATLAS CORE
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import init_db
from auth import router as auth_router
from routes.items import router as items_router

app = FastAPI(
    title="Taskflow Sistema De Gestion De Proyectos",
    description="API REST con autenticación JWT",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "project": "Taskflow Sistema De Gestion De Proyectos", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(items_router, prefix="/items", tags=["items"])

# Servir frontend
@app.get("/app")
def serve_frontend():
    return FileResponse("frontend/index.html")
