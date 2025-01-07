import streamlit as st




st.set_page_config(layout="wide")


bill = 0

st.header("Kamil's Restaurant")




st.image("https://as1.ftcdn.net/v2/jpg/05/01/56/92/1000_F_501569274_wVbQ7NpKIM54c3gA6tIGyVHDyApUkuLn.jpg")




st.subheader("Food")




meal1, meal2, meal3, meal4 = st.columns(4) #drinks, fruits, snacks




with meal1:
    if st.checkbox("Fried rice & chicken: $15"):
        st.write("Ok done")
        bill += 15



with meal2:
    if st.checkbox("Potatoes & Fish: $10"):
        st.write("Ok done")
        bill += 10



with meal3:
    if st.checkbox("Pasta & soup: $20"):
        st.write("Ok done")
        bill += 20



with meal4:
    if st.checkbox("Beans porridge: $15"):
        st.write("Ok done")
        bill += 15



st.subheader("Drinks")




drink1, drink2, drink3, drink4 = st.columns(4) #drinks, fruits, snacks




with drink1:
    if st.checkbox("Coke: $25"):
        st.write("Ok done")
        bill += 25



with drink2:
    if st.checkbox("Fanta: $15"):
        st.write("Ok done")
        bill += 15



with drink3:
    if st.checkbox("Pepsi: $20"):
        st.write("Ok done")
        bill += 20



with drink4:
    if st.checkbox("Ice tea: $10"):
        st.write("Ok done")
        bill += 10



st.subheader("Fruits")




fruit1, fruit2, fruit3, fruit4 = st.columns(4) #drinks, fruits, snacks




with fruit1:
    if st.checkbox("Apples: $15"):
        st.write("Ok done")
        bill += 15



with fruit2:
    if st.checkbox("Bananas: $10"):
        st.write("Ok done")
        bill += 10



with fruit3:
    if st.checkbox("Oranges: $20"):
        st.write("Ok done")
        bill += 20



with fruit4:
    if st.checkbox("Mangoes: $15"):
        st.write("Ok done")
        bill += 15



st.subheader("Snacks")




snack1, snack2, snack3, snack4 = st.columns(4) #drinks, fruits, snacks




with snack1:
    if st.checkbox("Meat pie: $15"):
        st.write("Ok done")
        bill += 15



with snack2:
    if st.checkbox("Chicken pie: $30"):
        st.write("Ok done")
        bill += 30



with snack3:
    if st.checkbox("Sausage roll: $15"):
        st.write("Ok done")
        bill += 15



with snack4:
    if st.checkbox("Egg roll: $15"):
        st.write("Ok done")
        bill += 15




if st.button("Check total bill"):
    st.success(f"Your total bill is ${bill}")

if st.checkbox("Click here to split the bill"):
    people = st.slider("Choose how many people in total", 2, 10)
    personbill = round(bill / people, 2)
    st.success(f"Each person will have to pay ${personbill}")