from typing import List, Optional
from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime



class ErrorMessage(BaseModel):
    msg: str

class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

@api_router.get("/healthcheck", include_in_schema=True)
def healthcheck():
    return {"status": "ok"}

@api_router.get("/routes/", summary="Get the top 3 shortest routes between two locations")
async def get_routes(request: Request, start: str, end: str):
    gmaps = request.app.state.gmaps
    try:
        now = datetime.now()
        directions_result = gmaps.directions(start, end, mode="driving", alternatives=True, departure_time=now)
        sorted_routes = sorted(directions_result, key=lambda x: x['legs'][0]['distance']['value'])[:3]
        return {
            "routes": [
                {
                    "summary": route["summary"],
                    "distance": route["legs"][0]["distance"]["text"],
                    "duration": route["legs"][0]["duration"]["text"],
                    "steps": [
                        {"instruction": step["html_instructions"], "distance": step["distance"]["text"]}
                        for step in route["legs"][0]["steps"]
                    ]
                }
                for route in sorted_routes
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))