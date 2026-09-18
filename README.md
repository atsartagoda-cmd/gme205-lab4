# GmE 205 Laboratory Exercise 4: Structured Programming + Object Systems Integration

This repository contains the outputs for Laboratory Exercise 4 in GmE 205 – Geospatial Programming.

## Algorithm

1. Start.
2. Load parcel data from the JSON file.
3. Convert each record into a Parcel object.
4. Check whether any parcels were loaded.
   - If no parcels are loaded, display an error message and stop the program.
5. Calculate the total area of active parcels.
6. Identify parcels above the specified area threshold.
7. Count the parcels in each zone.
8. Identify parcels suitable for development based on the selected zone.
9. Display the analysis results.
10. Save the results to output/summary.json.
11. End.

## Pseudocode

BEGIN

LOAD parcel_data from JSON file

SET parcel_list to empty list

FOR each record in parcel_data
    CONVERT record into Parcel object
    ADD Parcel object to parcel_list
END FOR

IF parcel_list is empty THEN
    PRINT "No parcels found."
    STOP
END IF

COMPUTE total area of active parcels

COMPUTE parcels above area threshold

COMPUTE parcel count by zone

COMPUTE parcels suitable for development based on selected zone

PRINT results

SAVE results to output/summary.json

END

## Control Structures

The program explicitly demonstrates the three basic control structures:

- **Sequence** – Parcel data are loaded, converted into objects, analyzed, displayed, and saved in a logical order.
- **Selection** – The program checks conditions, such as whether the parcel list is empty and whether parcels meet specific criteria.
- **Repetition** – The program uses loops to create and process multiple Parcel objects.