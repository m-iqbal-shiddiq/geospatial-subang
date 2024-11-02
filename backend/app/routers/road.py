import json

from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy import func

from app.database.connection import SessionLocal
from app.database.models import Road
from app.schemas.road import RoadCreate


router = APIRouter(redirect_slashes=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

        
@router.post("/")
def create_road(request: RoadCreate, db = Depends(get_db)):
    
    try:
        
        if len(request.points) < 2:
            return JSONResponse(
                status_code=400, 
                content={"message": "Road must have at least 2 points"
            })
        
        wkt_linestring = f"LINESTRING({', '.join([f'{point[0]} {point[1]}' for point in request.points])})"
        
        road = Road(
            road_name=request.road_name,
            geometry=func.ST_GeomFromText(wkt_linestring, 4326),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(road)
        db.commit()
        
        return JSONResponse(
            status_code=201, 
            content={"message": "Road created successfully"
        })
        
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=400, 
            content={"message": str(e)
        })
        
@router.get("/")
def get_all_roads(db = Depends(get_db)):
    
    try:
        roads = db.query(
            Road.road_name,
            func.ST_AsGeoJSON(Road.geometry).label("geometry")  # Converts to GeoJSON
        ).all()
        
        # Format roads as dictionaries with nested GeoJSON
        road_data = [{"road_name": road.road_name, "geometry": json.loads(road.geometry)} for road in roads]
        
        return JSONResponse(
            status_code=200, 
            content={"roads": road_data}
        )
        
    except Exception as e:
        return JSONResponse(
            status_code=400, 
            content={"message": str(e)
        })
    