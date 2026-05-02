# Bikeshare Data Analysis 🚲

## Overview

This project is an interactive Python application that allows users to explore bikeshare data for three major U.S. cities:

* Chicago
* New York City
* Washington

Users can filter data by **city**, **month**, and **day of the week**, and the program will compute and display various statistics.

---

## Features

### 🔍 User Input

* Select a city (Chicago, New York City, Washington)
* Filter by:

  * Month (January–June or all)
  * Day of the week (Monday–Sunday or all)

### 📊 Data Analysis

The program calculates and displays:

#### 1. Time Statistics

* Most common month
* Most common day of the week
* Most common start hour

#### 2. Station Statistics

* Most commonly used start station
* Most commonly used end station
* Most frequent trip (start → end)

#### 3. Trip Duration Statistics

* Total travel time
* Average travel time

#### 4. User Statistics

* User type counts
* Gender distribution (if available)
* Birth year stats:

  * Earliest
  * Most recent
  * Most common

### 📄 Raw Data View

* View raw data in chunks of 5 rows
* Interactive prompt to continue or stop

---

## Project Structure

```
.
├── bikeshare.py          # Main Python script
├── chicago.csv           # Chicago dataset
├── new_york_city.csv     # NYC dataset
├── washington.csv        # Washington dataset
└── README.md             # Project documentation
```

---

## Requirements

* Python 3.x
* pandas
* numpy

Install dependencies using:

```
pip install pandas numpy
```

---

## How to Run

1. Clone or download this repository
2. Make sure all CSV files are in the same directory as the script
3. Run the program:

```
python bikeshare.py
```

4. Follow the prompts in the terminal

---

## Example Usage

```
Hello! Let's explore some US bikeshare data!

Which city would you like to analyze? chicago
Which month? march
Which day? friday
```

---

## Notes

* Some datasets may not include **Gender** or **Birth Year** columns (e.g., Washington)
* Input is case-insensitive
* Invalid inputs are handled with prompts

---

## Possible Improvements

* Add data visualizations (matplotlib / seaborn)
* Build a web interface (e.g., Streamlit)
* Export filtered data or results
* Improve input flexibility (aliases like "NYC")

---

## Author
Varsha Maruti Gavari
---

## License

This project is open source and available under the MIT License.
Include the date you created this project and README file.

##Username : varsha Gavari
