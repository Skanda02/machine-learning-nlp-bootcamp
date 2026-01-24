import streamlit as st
import pandas as pd
import numpy as np

# title of the app
st.title("Simple Data Analysis App")

# Display simple text
st.write("This app allows you to upload a CSV file and perform basic data analysis.")

# Display simple metrics
st.metric(label="App Version", value="1.0.0")

# Display a button
if st.button("Click Me"):
    st.write("Button clicked!")

# display a dataframe
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=['A', 'B', 'C', 'D', 'E']
)
st.dataframe(data)

# Display a file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Create line chart from random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
