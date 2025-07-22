# NASA Asteroid Data Analysis

This project analyzes near-Earth asteroid data from a NASA-provided CSV file. It includes data filtering, statistical analysis, and visualization to help understand the characteristics and behaviors of asteroids that have approached Earth.



## Features

- **CSV Data Loader**: Validates and loads asteroid data from a `.csv` file.
- **Data Filtering**: Filters asteroids by close approach year (from 2000 onwards).
- **Data Cleaning**: Removes irrelevant columns and provides dataset structure details.
- **Insights & Analysis**:
  - Finds the asteroid with the highest **absolute magnitude**.
  - Identifies the asteroid that came **closest to Earth**.
  - Counts **common orbit IDs**.
  - Determines how many asteroids have a **maximum diameter above the average**.
- **Visualizations**:
  - **Histogram** of average asteroid diameters.
     <img width="1918" height="965" alt="Histogram of average asteroid diameters" src="https://github.com/user-attachments/assets/7e15e2bd-ab72-4134-99ae-ea5fb039b449" />
  - **Histogram** of minimum orbit intersections.
    <img width="1918" height="966" alt="Histogram of minimum orbit intersections" src="https://github.com/user-attachments/assets/47a7e92a-bbc0-4fd5-856e-d507f31ba8ae" />
  - **Pie Chart** of hazardous vs. non-hazardous asteroids.
    <img width="1910" height="962" alt="Pie Chart of hazardous vs. non-hazardous asteroids" src="https://github.com/user-attachments/assets/d2f3c3a1-24a6-41c9-bde3-b7e31347a414" />
  - **Scatter Plot with Linear Regression**: Between miss distance and speed.
    <img width="1916" height="965" alt="Scatter Plot with Linear Regression: Between miss distance and speed" src="https://github.com/user-attachments/assets/a30b12f4-776f-4fc9-a3a5-32aa9107da4d" />

## Input

The input is a CSV file with asteroid data. Make sure your file:
- Has a `.csv` extension.
- Includes fields like: `Name`, `Close Approach Date`, `Absolute Magnitude`, `Hazardous`, `Miss Dist.(kilometers)`, `Est Dia in KM(min)`, `Est Dia in KM(max)`, `Orbit ID`, etc.
- Is in the same folder as your .py file

## Requirements

- Python 3.x
- `pandas`
- `numpy`
- `matplotlib`
- `scipy`
- `os`(standard library)

Install dependencies:
```bash
pip install pandas numpy matplotlib scipy
````

## How to Use

1. Place your asteroid data file in the same directory (e.g. `nasa.csv`).
2. Run the script:

```bash
python your_script_name.py
```

## Notes

* The project uses basic error handling for file validation.
* Statistical significance in linear regression is checked using `p-value`.

## Example Output

* Histogram of average asteroid diameters
* Pie chart of hazardous vs non-hazardous asteroids
* Scatter plot showing regression between miss distance and speed

## License

This project was created as a final university assignment for the course Introduction to Computation and Programming using Python at The Open University.

❗ Copying, redistributing, or using this project for non-educational purposes is strictly prohibited and may lead to academic penalties. Use at your own responsibility.

---

