import streamlit as st
import pandas as pd
import plotly.express as px

try:
    readcsv = pd.read_csv("data.csv")
except:
    readcsv = pd.DataFrame()

menu = st.sidebar.selectbox("Menu", ["Enter student's data", "View table|charts"])

if menu == "Enter student's data":
    name = st.text_input("Enter student's name")
    number = st.number_input("Enter student's roll number", 1, 40)
    present = st.number_input("Enter the total days present", 0, 300)
    absent = st.number_input("Enter the total days absent", 0, 300)

    if st.button("Enter data"):
        if name != "":
            data_dict = {"Roll number": [number], "Name": [name], "Days present": [present], "Days absent": [absent]}
            data_table = pd.DataFrame(data_dict)
            joinables = pd.concat([readcsv, data_table], ignore_index = True)
            joinables.to_csv("data.csv", index = False)
            st.success("Data entered successfully")
        else:
            st.warning("Please enter student's name")

if menu == "View table|charts":
    table = readcsv.to_html(index = False)
    st.markdown(table, unsafe_allow_html = True)

    st.write("")
    st.write("")
    choosechart = st.pills("Choose chart to plot", ["Bar Chart", "Pie Chart"])
    if choosechart == "Bar Chart":
        try:
            barchart = px.bar(readcsv, x = "Name", y = ["Days present", 'Days absent'], barmode = 'group' )
            st.plotly_chart(barchart)
        except:
            st.error("No data")
    elif choosechart == "Pie Chart":
        pie1, pie2 = st.columns(2)
        with pie1:
            st.subheader("Days present")
            try:
                piechart = px.pie(readcsv, names = "Name", values = "Days present")
                st.plotly_chart(piechart)
            except:
                st.error("No data")
        with pie2:
            st.subheader("Days absent")
            try:
                piechart = px.pie(readcsv, names = "Name", values = "Days absent")
                st.plotly_chart(piechart)
            except:
                st.error("No data")