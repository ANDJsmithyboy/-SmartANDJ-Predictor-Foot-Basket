from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse, FileResponse
from pathlib import Path

from .routers import predict


def create_app() -> FastAPI:
    app = FastAPI(
        title="SmartANDJ Predictor API",
        description="API de prédiction pour football et basketball (prototype)",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(predict.router, prefix="/predict", tags=["Predictions"]) 

    # Serve static assets under /static and index at '/'
    static_dir = Path(__file__).parent / "static"
    app.mount("/static", StaticFiles(directory=str(static_dir), html=False), name="static")

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    @app.get("/healthz")
    def healthz() -> JSONResponse:
        return JSONResponse({"status": "ok"})

    return app


app = create_app()

