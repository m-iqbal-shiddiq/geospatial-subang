from pydantic import BaseModel
from typing import List

class RoadCreate(BaseModel):
    road_name: str
    points: List[List[float]]
    
    class Config:
        json_schema_extra = {
            "example": {
                "road_name": "Main Road",
                "points": [[30.0, 10.0], [10.0, 30.0], [40.0, 40.0]]
            }
        }