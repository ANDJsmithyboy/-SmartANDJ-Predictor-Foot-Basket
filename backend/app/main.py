from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

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

    # Static UI (index.html) served at '/'
    app.mount(
        "/",
        StaticFiles(directory=str(__file__).rsplit("/", 1)[0] + "/static", html=True),
        name="static",
    )

    @app.get("/healthz")
    def healthz() -> JSONResponse:
        return JSONResponse({"status": "ok"})

    return app


app = create_app()

