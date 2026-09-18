def total_active_area(parcels: list) -> float:
    total = 0

    for parcel in parcels:
        if parcel.is_active:
            total += parcel.area()

    return total


def parcels_above_threshold(parcels: list, threshold: float) -> list:
    result = []

    for parcel in parcels:
        if parcel.area() > threshold:
            result.append(parcel)

    return result


def count_by_zone(parcels: list) -> dict:
    counts = {}

    for parcel in parcels:
        if parcel.zone in counts:
            counts[parcel.zone] += 1
        else:
            counts[parcel.zone] = 1

    return counts


def intersecting_parcels(parcels: list, zone) -> list:
    result = []

    for parcel in parcels:
        if parcel.zone == zone:
            result.append(parcel)

    return result