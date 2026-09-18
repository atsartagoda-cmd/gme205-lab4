# GmE 205 Laboratory Exercise 4: Structured Programming + Object Systems Integration

This repository contains the outputs for Laboratory Exercise 4 in GmE 205 – Geospatial Programming.

## Description

This project demonstrates the integration of structured programming and object-oriented programming concepts in a simple geospatial parcel analysis system. Parcel data are loaded from a JSON file and represented as `Parcel` objects with Shapely geometries. The system uses structured analysis functions to calculate the total area of active parcels, identify parcels above an area threshold, count parcels by zone, and identify parcels suitable for development based on a selected zone. The results are displayed in the terminal and saved to `output/summary.json`.

## Getting Started

### Dependencies

The project requires:

- Python 3
- Shapely
- NumPy
- pytest

The exact package versions used in the project are listed in `requirements.txt`.

### Installing

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

```powershell
python -m venv .venv
```

4. Activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install the required packages:

```powershell
pip install -r requirements.txt
```

### Executing Program

To run the main parcel analysis:

```powershell
python -m src.run_lab4
```

The program will:

1. Load the parcel data from `data/parcels.json`.
2. Construct `Parcel` objects.
3. Perform the required parcel analyses.
4. Display the results in the terminal.
5. Save the summary to `output/summary.json`.

To run the object demonstration:

```powershell
python -m src.demo
```

To run the spatial object test:

```powershell
python -m pytest tests/test_spatial.py -v
```

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

## Reflection

### 1. Where in your system do Sequence, Selection, and Repetition explicitly appear?

Sequence appears in `run_lab4.py`, where the program loads the parcel data, creates Parcel objects, performs the analyses, prints the results, and saves the summary in order. Selection appears in the `if` statements used to check whether parcels were loaded and whether parcels meet specific conditions. Repetition appears in the `for` loops used to create and analyze multiple Parcel objects.

### 2. If you removed your algorithm planning step, how would your implementation likely change?

Without the algorithm planning step, the implementation would likely be less organized and more prone to unnecessary or misplaced code. Planning the sequence beforehand helped identify what the program needed to do first, where decisions and loops were needed, and which responsibilities belonged in `spatial.py`, `analysis.py`, and `run_lab4.py`.

### 3. Where does spatial behavior live in your system, and why is that important?

Spatial behavior lives in `SpatialObject` in `spatial.py`, particularly through the `area()` method that uses the object's geometry. This is important because spatial operations remain with the objects that own the geometry, while the analysis functions simply use that behavior. It keeps responsibilities clear and avoids repeating spatial logic elsewhere in the program.

### 4. Why does analysis.py contain structured logic instead of demo.py?

`analysis.py` contains the structured logic because its purpose is to perform the actual parcel analyses using functions, loops, and conditions. In contrast, `demo.py` only demonstrates how the `Parcel` object works. Keeping the analysis logic separate makes the program easier to organize, reuse, and maintain.

### 5. What would happen if all filtering logic were placed inside the Parcel class?

If all filtering logic were placed inside the `Parcel` class, the class would take on responsibilities beyond representing a single parcel and its spatial behavior. It would become harder to maintain as more analysis rules are added. Keeping filtering in `analysis.py` allows `Parcel` to remain focused on its own data and behavior.

### 6. If a new rule is added (e.g., “exclude inactive industrial parcels”), how easily can your current design adapt?

The current design can adapt easily because the filtering rules are separated from the Parcel class. A new condition, such as excluding inactive industrial parcels, can be added to the appropriate function in `analysis.py` without changing the basic structure of the Parcel objects or the rest of the program.

### 7. How does separating structured logic from object behavior prevent “God classes”?

Separating structured logic from object behavior prevents one class from becoming responsible for too many parts of the system. The `Parcel` and `SpatialObject` classes focus on storing data and providing spatial behavior, while `analysis.py` handles the analysis rules. This keeps each part focused, easier to understand, and easier to modify.

## Help

If PowerShell prevents the virtual environment from activating because script execution is disabled, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

The execution policy change above applies only to the current PowerShell session.

## Author

Airah Shayne T. Sartagoda

## Version History

### 1.0

- Initial implementation of GmE 205 Laboratory Exercise 4.
- Added spatial object classes and shared spatial behavior.
- Added structured parcel analysis functions.
- Added the main application runner and JSON summary output.
- Added spatial object testing and project documentation.

## Acknowledgments

This project was developed as part of GmE 205 – Geospatial Programming, Laboratory Exercise 4: Structured Programming + Object Systems Integration.

The laboratory exercise and its instructions provided the framework for applying structured programming concepts, object-oriented design, and Shapely-based spatial behavior in the parcel analysis system.