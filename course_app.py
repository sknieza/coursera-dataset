import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import cufflinks as cf
import streamlit as st
import course_data as cd
import plotly.graph_objects as go


st.title('Course directory')
st.write('This is a test Coursera course directory. Select your field of interest in the sidebar and find the course you need.')
st.header("Explore the most popular courses", divider=True)


st.dataframe(cd.popular_courses, use_container_width=True)


st.header("Discover courses by topic:")
course_dirs = st.selectbox(
    "Select course topic:", 
    ("AI/ML", "Data", "Python", "Marketing", "Management")
)


st.header(course_dirs)


if course_dirs == 'AI/ML':
    st.subheader("These are the selected AI/ML courses, with rating above 75% of the courses")
    st.dataframe(cd.ai_courses, use_container_width=True)

if course_dirs == 'Data':
    st.subheader("These are the selected Data courses, with rating above 75% of the courses")
    st.dataframe(cd.data_courses, use_container_width=True)

if course_dirs == 'Python':
    st.subheader("These are the selected Python courses, with rating above 75% of the courses")
    st.dataframe(cd.python_courses, use_container_width=True)

if course_dirs == 'Marketing':
    st.subheader("These are the selected Marketing courses, with rating above 75% of the courses")
    st.dataframe(cd.marketing_courses, use_container_width=True)

if course_dirs == 'Management':
    st.subheader("These are the selected Management courses, with rating above 75% of the courses")
    st.dataframe(cd.management_courses, use_container_width=True)


st.header("Course directory: summary statistics")
st.write("This graph represents the course distribution by the certificate type and difficulty.")
st.write("Generally, specialization modules have a lower rating, while beginner courses are rated the best. "
         "Professional certificates have a highly varying rating, and specializations are usually mediocre. "
         "Take these considerations into account when selecting a course from a suggested directory.")

fig = px.sunburst(cd.sungraph_data, path=['course_Certificate_type', 'course_difficulty'],
                  color='course_rating_scaled', labels={"course_rating_scaled": "Rating"})

st.write(fig)
