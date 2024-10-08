# Coursera course dataset analysis

In this project, we explore Coursera courses dataset with 890 observations over 6 features. As there were no prerequisites on how to appraoch the data, we defined a brief scenario which would guide our exploration. The description of the scenario is provided in the main notebook file.

## Dataset

The dataset has 890 observations over 6 features. It was parsed with the intention to create an interactive course selection tool. It contains courses from different topics, but the most popular ones are on data science, Python and machine learning / AI – something that's trending in the tech right now.

The features of the dataset are as follows:

1. `course_title`: str – contains the course title;
2. `course_organization`: str – it tells which organization is conducting the courses;
3. `course_Certificate_type`: str – it has details about what are the different certifications available in courses;
4. `course_rating`: float – it has the ratings associated with each course;
5. `course_difficulty`: str – it tells about how difficult or what is the level of the course;
6. `course_students_enrolled`: str – it has the number of students that are enrolled in the course.

## Repository contents

### Main file

The main file of data analysis and charting is a Jupyter Notebook file `coursera_exploration.ipynb`. The analysis is split into three parts: 

1. Understanding the dataset;
2. Data wrangling and exploration;
3. Exploration based on scenario.

The scenario definition is provided beforehand. 

### Streamlit app

The file `course_app.py` contains a Streamlit app source code, and is dependent upon course_data.py file, which contains the script used for data cleaning and manipulation purposes (a simplified version of the Notebook, intended for app building).

The app can be run either by executing the certain cell in the exploration notebook or by running a terminal command:

```
streamlit run course_app.py
```

### Dataset

The `coursera_data.csv` is placed in `dataset/` folder.

## Requirements

The key requirements and dependencies are contained in `requirements.txt` file. Some of the prominent ones:

- `pandas` library for data manipulation and analysis;
- `numpy` library adding support for large, multi-dimensional arrays and matrices;
- `matplotlib`, `seaborn` and `plotly` for charting and visualisation of the data;
- `streamlit` for building lightweight web app with Python.

## Functions

This program has two functions for data conversion and outlier detection.

### value_to_float(x)

Takes a string notation of enrolled student count and converts it to float number

### find_outliers(column, method='zscore', threshold=3)

This function detects outliers in a numerical column using a specified method.