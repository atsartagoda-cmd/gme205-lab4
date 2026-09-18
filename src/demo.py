from src.spatial import Parcel


parcel_data = {
    "parcel_id": 1,
    "zone": "Residential",
    "is_active": True,
    "area_sqm": 5000,
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [0, 0],
            [10, 0],
            [10, 10],
            [0, 10],
            [0, 0]
        ]]
    }
}

parcel = Parcel.from_dict(parcel_data)

print(f"Parcel ID: {parcel.parcel_id}")
print(f"Zone: {parcel.zone}")
print(f"Active: {parcel.is_active}")
print(f"Area: {parcel.area_sqm}")
print(f"Geometry type: {parcel.geometry.geom_type}")