import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px
import cufflinks as cf
from mlxtend.preprocessing import minmax_scaling
from scipy import stats


course_data = pd.read_csv('dataset/coursera_data.csv')
course_data.rename(columns={"Unnamed: 0": "index"}, inplace=True)
course_data = course_data.set_index('index').sort_index()
course_data['course_Certificate_type'] = course_data.course_Certificate_type.astype('category')
course_data['course_difficulty'] = course_data.course_difficulty.astype('category')


def value_to_float(x):
    """
    Takes a string notation of enrolled student count and converts it to float number

    Parameters
    ----------
    x : str
        The string that contains course student count in format 100k or 3m

    Returns
    -------
    x : float
        This function returns a floating point value, removing the thousands
        or millions notation in string (k or m) and multiplying the remainder
        digit by 1000 or 1000000 accordingly.

    Notes
    -----
    - This function is used in pandas df.apply() method to change the cell values
    of the feature.
    """
    if 'k' in x:
        if len(x) > 1:
            return float(x.replace('k', '')) * 1000
        return 1000.0
    if 'm' in x:
        if len(x) > 1:
            return float(x.replace('m', '')) * 1000000
        return 1000000.0
    return 0.0


course_data['course_students_enrolled'] = course_data['course_students_enrolled'].apply(value_to_float)


def find_outliers(column, method='zscore', threshold=3):
    """
    This function detects outliers in a numerical column using a specified method.

    Args:
    column (pandas.Series): The numerical column to analyze.
    method (str, optional): The method for outlier detection. Defaults to 'zscore'.
        - 'zscore': Uses z-scores (standard deviations from the mean).
        - 'iqr': Uses Interquartile Range (IQR).
    threshold (float, optional): The threshold for outlier detection. Defaults to 3.
        - For z-scores, values with absolute value exceeding the threshold are considered outliers.
        - For IQR, values below Q1 - threshold * IQR or above Q3 + threshold * IQR are considered outliers.

    Returns:
    pandas.Series: A Series containing True for outliers and False for non-outliers.    
    """

    if method == 'zscore':
        z_scores = stats.zscore(column)
        return np.abs(z_scores) > threshold
    elif method == 'iqr':
        q1 = column.quantile(0.25)
        q3 = column.quantile(0.75)
        iqr = q3 - q1
        return (column < (q1 - threshold * iqr)) | (column > (q3 + threshold * iqr))
    else:
        raise ValueError("Invalid method. Choose 'zscore' or 'iqr'.")
    
enrolled_outliers = find_outliers(course_data["course_students_enrolled"], method='zscore')
enrolled_outliers_df = course_data[enrolled_outliers]
rating_outliers = find_outliers(course_data["course_rating"], method='zscore')
rating_outliers_df = course_data[rating_outliers]
cd_no_outliers = course_data.drop(labels=rating_outliers_df.index, axis=0)
cd_no_outliers = cd_no_outliers.drop(labels=enrolled_outliers_df.index, axis=0)

sungraph_data = cd_no_outliers
sungraph_data['course_rating_scaled'] = sungraph_data['course_rating']
sungraph_data['course_rating_scaled'] = (sungraph_data['course_rating_scaled'] - sungraph_data['course_rating_scaled'].min()) / (sungraph_data['course_rating_scaled'].max() - sungraph_data['course_rating_scaled'].min())


# # Academic institution keywords:
# academic_kw = ['Academy', 'University', 'School', 'Institute', 'École', 'College', 'Universitat', 'Università', 'Universidad', 'Universiteit', 'Tecnológico', 'Universität', 'Instituto', 'HEC Paris', 'INSEAD', 'Sciences']

# # Corporate institution keywords:
# corp_kw = ["IBM", "Google", 'Amazon', 'Cisco', 'PwC', 'BCG', 'Mail.Ru Group', 'Cloudera', 'Autodesk', 'Palo Alto', 'JetBrains', 'Unity', 'Automation Anywhere', 'VMware', 'Atlassian']

# # Now we run few loops to change the values:

# for _ in academic_kw:
#     cd_no_outliers.loc[cd_no_outliers.course_organization.str.contains(_), 'course_organization_type'] = 'Academic'

# for _ in corp_kw:
#     cd_no_outliers.loc[cd_no_outliers.course_organization.str.contains(_), 'course_organization_type'] = 'Corporate'

# cd_no_outliers['course_organization_type'] = cd_no_outliers['course_organization_type'].replace(to_replace="NaN", value="Other")


# feats_to_drop = ['course_rating_scaled', 'course_organization_type']
# cd_no_outliers.drop(labels = feats_to_drop, axis=1, inplace=True)

mapper = {
    "index": "No.",
    "course_title": "Title",
    "course_organization": "Organization",
    "course_Certificate_type": "Certificate Type",
    "course_rating": "Rating",
    "course_difficulty": "Difficulty",
    "course_students_enrolled": "Students Enrolled",
}


data_courses = cd_no_outliers.loc[
    (cd_no_outliers['course_title'].str.contains('Data')) & 
    (cd_no_outliers['course_rating'] >= cd_no_outliers['course_rating'].quantile(q=0.75))
    ]
data_courses.rename(columns=mapper, inplace=True)


ai_courses = cd_no_outliers.loc[
    (cd_no_outliers['course_title'].str.contains('AI')) |
    (cd_no_outliers['course_title'].str.contains('Machine Learning')) & 
    (cd_no_outliers['course_rating'] >= cd_no_outliers['course_rating'].quantile(q=0.75))
    ]
ai_courses.rename(columns=mapper, inplace=True)


marketing_courses = cd_no_outliers.loc[
    (cd_no_outliers['course_title'].str.contains('Marketing')) & 
    (cd_no_outliers['course_rating'] >= cd_no_outliers['course_rating'].quantile(q=0.5))
    ]
marketing_courses.rename(columns=mapper, inplace=True)


python_courses = cd_no_outliers.loc[
    (cd_no_outliers['course_title'].str.contains('Python')) & 
    (cd_no_outliers['course_rating'] >= cd_no_outliers['course_rating'].quantile(q=0.75))
    ]
python_courses.rename(columns=mapper, inplace=True)


management_courses = cd_no_outliers.loc[
    (cd_no_outliers['course_title'].str.contains('Management')) |
    (cd_no_outliers['course_title'].str.contains('Strategy')) & 
    (cd_no_outliers['course_rating'] >= cd_no_outliers['course_rating'].quantile(q=0.75))
    ]
to_drop = [102, 242, 290, 326, 444, 587, 597, 764, 177, 354, 660]
management_courses.drop(to_drop, axis='index', inplace=True)
management_courses.rename(columns=mapper, inplace=True)


popular_courses = enrolled_outliers_df
popular_courses.rename(columns=mapper, inplace=True)
