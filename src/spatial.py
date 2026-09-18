from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

class Parcel(SpatialObject):
    def __init__(self, parcel_id, zone, is_active, area_sqm, geometry):
        self.parcel_id = parcel_id
        self.zone = zone
        self.is_active = is_active
        self.area_sqm = area_sqm
        super().__init__(geometry)

    @classmethod
    def from_dict(cls, data):
        return cls(
            parcel_id=data["parcel_id"],
            zone=data["zone"],
            is_active=data["is_active"],
            area_sqm=data["area_sqm"],
            geometry=shape(data["geometry"]),
        )