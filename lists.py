import streamlit as st

st.sidebar.write("Made by Mr.Tree")

menu = st.sidebar.selectbox("Menu", ["Page 1", "Page 2", "Page 3"])

if menu == "Page 1":
    
    color = st.selectbox("Choose a color", ["Blue", "Black", "Orange", "White", "Gray"])

    st.write("You chose " + color)

if menu == "Page 2":

    gender = st.radio("Select your gender", ["male", "female"], horizontal=True)

    st.write("You're a " + gender)