import streamlit as st

st.set_page_config(layout="wide")

name = ""
name = st.text_input("What's your name?")

color = ""
color = st.text_input("What's your favorite color?")

animal = ""
animal = st.text_input("What's your favorite animal?")

food = ""
food = st.text_input("What's your favorite food?")

if st.checkbox("Show results"):
    if food != "" and animal != "" and color != "" and name != "":
        st.write("Hello " + name + "! Your favorite color is " + color + ", you love " + animal + "s, and your favorite food is " + food + "!")
    else:
        st.write("You didn't provide us enough information.")