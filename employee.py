import streamlit as st

menu = st.sidebar.selectbox("Menu", ["Register Staff", "Staff Database", "Staff File"])

if menu == "Register Staff":

    st.title("Register Here")

    leftcol, rightcol = st.columns(2)

    with leftcol:
        name = st.text_input("First Name:")
        mail = st.text_input("Email Adress:")
    with rightcol:
        lname = st.textinput("Last Name:")
        gender = st.