import logging
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import googlemaps
from contextlib import asynccontextmanager
from api import api_router
from starlette.config import Config

# Load environment variables
config = Config(".env")
api_key = config("GOOGLE_MAPS_API_KEY", cast=str)

log = logging.getLogger('uvicorn.error')


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )
exception_handlers = {404: not_found}

@asynccontextmanager
async def lifespan(api: FastAPI):
    # Initialize the Google Maps client and store it in app state
    log.info("Setting up context...")
    api.state.gmaps = googlemaps.Client(key='')  # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    yield
    # Cleanup actions here if necessary (e.g., closing connections)

app = FastAPI(
    exception_handlers=exception_handlers,
    title="ReMap API",
    description="API for ReMap",
    root_path="/api/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
    lifespan=lifespan
)

app.include_router(api_router)