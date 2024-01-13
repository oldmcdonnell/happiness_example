import streamlit as st
import plotly.express as px
import pandas as pd

#add a title
st.title("In Search for Happiness")

df = pd.read_csv("happy.csv")

#selection box for x axis
option_x = st.selectbox("Select option for X-Axis", ("GDP", "Happiness", "Generosity"))

#slection box for y axis
option_y = st.selectbox("Select option of Y-Axis", ("GDP", "Happiness", "Generosity"))

match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]


st.subheader(f"{option_x} and {option_y}")

figure1 = px.scatter(x=x_array, y=y_array,
                      labels={"x":option_x, "y":option_y})

st.plotly_chart(figure1)