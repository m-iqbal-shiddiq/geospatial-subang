from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import road

origins = [
    "http://localhost:8000",  
    "http://127.0.0.1:8000"
]


app = FastAPI(redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(road.router, prefix="/roads", tags=["roads"]) 
