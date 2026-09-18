import json


from src.analysis import (
    total_active_area,
    parcels_above_threshold,
    count_by_zone,
    intersecting_parcels,
)
from src.spatial import Parcel


with open("data/parcels.json", "r") as file:
    data = json.load(file)


parcels = []

for item in data:
    parcel = Parcel.from_dict(item)
    parcels.append(parcel)

if not parcels:
    print("No parcels found.")
    raise SystemExit


total_area = total_active_area(parcels)


threshold = 10000
above_threshold = parcels_above_threshold(parcels, threshold)


zone_counts = count_by_zone(parcels)


development_zone = "Residential"
development_parcels = intersecting_parcels(parcels, development_zone)


print(f"Loaded {len(parcels)} parcels.")
print(f"Total active area: {total_area:.2f}")
print(f"Parcels above {threshold} area units: {len(above_threshold)}")
print(f"Parcels by zone: {zone_counts}")
print(
    f"Parcels suitable for development in {development_zone}: "
    f"{len(development_parcels)}"
)


summary = {
    "total_active_area": total_area,
    "parcels_above_threshold": len(above_threshold),
    "parcels_by_zone": zone_counts,
    "development_zone": development_zone,
    "development_parcels": len(development_parcels),
}

with open("output/summary.json", "w") as file:
    json.dump(summary, file, indent=4)