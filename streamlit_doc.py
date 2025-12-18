import streamlit as st
import pandas as pd
import numpy as np
import time

#text utility

st.title("Streamlit Dashboard")
st.header("I am learning Streamlit")
st.subheader("And I am Loving it")
st.write("This is a normal text")

st.markdown("""
### My Favourite Movies
- 96
- Vaathi
- RDX 
""")

st.code('''
def foo(num):
    return num**2
''')

st.latex("x^2+y^2+5=0")

df=pd.DataFrame({
    "name":["Nitish","Ankit","Anupama"],
    "marks":[50,60,70],
    "package":[10,12,14]
})

#Display Elements

st.dataframe(df)

st.metric("Revenue","Rs 3L","-3 %")

st.json({
    "name":["Nitish","Ankit","Anupama"],
    "marks":[50,60,70],
    "package":[10,12,14]
})

#Display Media

st.image("join.png")

st.video("02. How to install Git [windows].mp4")

#creating Layouts

st.sidebar.title("Hellooo")

col1,col2=st.columns(2)
with col1:
    st.image("join.png")
with col2:
    st.image("join.png")

#showing status

st.error("Login Failed")
st.success("Login Successful")
st.info("You got it")
st.warning("Warning!!!")

bar=st.progress(0)

for i in range(0,101):
    time.sleep(0.1)
    
#taking user input

email=st.text_input("Enter Email")
number=st.number_input("Enter age")
dt=st.date_input("Enter regd date")

