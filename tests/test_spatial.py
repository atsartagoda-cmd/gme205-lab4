from src.spatial import Parcel


def test_parcel_from_dict():
    data = {
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

    parcel = Parcel.from_dict(data)

    assert parcel.parcel_id == 1
    assert parcel.zone == "Residential"
    assert parcel.is_active is True
    assert parcel.area_sqm == 5000
    assert parcel.geometry.geom_type == "Polygon"
    assert parcel.area() == 100