# Sea Level Predictor

A Python project built as part of the **FreeCodeCamp Data Analysis with Python** certification.

## Description
Analyzes global average sea level change since **1880** and predicts sea level
rise through **2050** using linear regression. Two prediction lines are plotted:
one using all historical data and one using only data from year 2000 onwards.

## Chart Produced

| File | Description |
|---|---|
| `sea_level_plot.png` | Scatter plot with two lines of best fit predicting sea level rise to 2050 |

## How to Run

### Install dependencies
```bash
pip install matplotlib pandas scipy
```
### Run the project
```bash
python main.py
```
## Project Structure
```
├── sea_level_predictor.py  # Main solution file
├── epa-sea-level.csv       # Dataset (Global Average Sea Level Change 1880-2014)
├── main.py                 # Run and test the solution
├── test_module.py          # Unit tests (do not modify)
├── sea_level_plot.png      # Generated prediction chart
└── README.md
```
## Technologies Used
* Python 3

* Pandas

* Matplotlib

* SciPy (linregress)

## Data Source
Global Average Absolute Sea Level Change, 1880-2014.
US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
