CREATE TABLE roads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    road_name VARCHAR(255),
    geometry GEOMETRY(GEOMETRY, 4326),
    photo_1 BYTEA,
    photo_2 BYTEA,
    photo_3 BYTEA,
    photo_4 BYTEA,
    photo_5 BYTEA,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
