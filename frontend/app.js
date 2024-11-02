const viewer = new Cesium.Viewer('cesiumContainer', {
    terrainProvider: Cesium.createWorldTerrain()
});

async function loadRoads() {
    try {
        const response = await fetch('http://localhost:8000/roads'); 
        const data = await response.json();
        
        if (data.roads) {
            data.roads.forEach(road => {
                const coordinates = JSON.parse(road.geometry).coordinates;
                const roadName = road.road_name;

                viewer.entities.add({
                    name: roadName,
                    polyline: {
                        positions: Cesium.Cartesian3.fromDegreesArray(coordinates.flat()), 
                        width: 5,
                        material: Cesium.Color.RED
                    }
                });
            });
        }
    } catch (error) {
        console.error('Error loading roads:', error);
    }
}

loadRoads();

