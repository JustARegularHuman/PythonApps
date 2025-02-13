#Subit records/scores, save in a file.
#Teachers can view the chart their students and send trough mail


import streamlit as st # type: ignore #webpage for my python app
import pandas as pd
import plotly.express as px #plot chats

try:
    readcsv = pd.read_csv("scores.csv")
except:
    readcsv = pd.DataFrame()

studentID = "Student" + str(len(readcsv) + 1)

menu = st.sidebar.selectbox("Menu", ["Submit Scores", "View Table/Charts"])

if menu == "View Table/Charts":
    # st.table(readcsv) simple table view
    table = readcsv.to_html(index=False)
    st.markdown(table, unsafe_allow_html=True)

    subjects = ["Maths", "English", "Chemistry", "Biology", "Physics", "History"]
    try:
        subjectstable = readcsv[subjects].mean().reset_index()
    except:
        st.error("No data avaible")
    #st.table(subjectstable)

    st.write("")
    st.write("")
    choosechart = st.pills("Choose chart to plot", ["Bar Chart", "Pie Chart"])
    if choosechart == "Bar Chart":
        try:
            barchart = px.bar(subjectstable, x="index", y=0, labels={"index": "Subject", "0": "Average"})
            st.plotly_chart(barchart)
        except:
            st.error("No data avaible")

    elif choosechart == "Pie Chart":
        try:
            piechart = px.pie(subjectstable, names="index", values=0, labels={"index": "Subject", "0": "Average"})
            st.plotly_chart(piechart)
        except:
            st.error("No data avaible")

if menu == "Submit Scores":
    st.subheader("Submit Students Scores")
    name = st.text_input("Please enter student name")
    leftcol, rightcol = st.columns(2)
    with leftcol:
        math = st.number_input("Enter student score in Math", 0, 100, step = 10)
        chem = st.number_input("Enter student score in Chemistry", 0, 100, step = 10)
        biology = st.number_input("Enter student score in Biology", 0, 100, step = 10)

    with rightcol:
        eng = st.number_input("Enter student score in English", 0, 100, step = 10)
        physics = st.number_input("Enter student score in Physics", 0, 100, step = 10)
        history = st.number_input("Enter student score in History", 0, 100, step = 10)

    totalscore = math+chem+biology+eng+physics+history
    average = round(totalscore/6)


    #A+ 90
    #A 80
    #B+ 70
    #B 60
    #C 50
    #D 40
    #F <40

    grades = ["A+", "A", "B+", "B", "C", "D", "F"]
    nums = [90, 80, 70, 60, 50, 40]

    grade = "F"

    for x in range(len(nums)):
        if average >= nums[x]:
            grade = grades[x]
            break

    if st.button("Submit Student Score"):
        if average >= 80:
            st.success(f"{name}, your total is: {totalscore}. Average is: {average}. Your grade is {grade}.")
        elif average >= 60:
             st.info(f"{name}, your total is: {totalscore}. Average is: {average}. Your grade is {grade}.")
        elif average >= 40:
             st.warning(f"{name}, your total is: {totalscore}. Average is: {average}. Your grade is {grade}.")
        else:
            st.error(f"{name}, your total is: {totalscore}. Average is: {average}. Your grade is {grade}.")

        newstudentdict = {"StudentID": [studentID], "Name": [name], "Maths": [math], "English": [eng], "Chemistry": [chem], "Biology": [biology], "Physics": [physics], "History": [history], "Average": [average], "Grade": [grade]}
        newstudenttable = pd.DataFrame(newstudentdict)
        joinables = pd.concat([readcsv, newstudenttable], ignore_index = True)
        joinables.to_csv("scores.csv", index = False)