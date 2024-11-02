import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import LargeBinary
from geoalchemy2 import Geometry

Base = declarative_base()

class Road(Base):
    __tablename__ = 'roads'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    road_name = Column(String, nullable=False)
    geometry = Column(Geometry(geometry_type='LINESTRING', srid=4326), nullable=False)
    photo_1 = Column(LargeBinary)
    photo_2 = Column(LargeBinary)
    photo_3 = Column(LargeBinary)
    photo_4 = Column(LargeBinary)
    photo_5 = Column(LargeBinary)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    
