import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "GOOGLE_API_KEY")
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("AI Based BMI Calculator-Know Your health")

name = st.text_input("Enter your name")
height = st.number_input("Enter your height in cm")
weight = st.number_input("Enter your weight in kg")
age = st.number_input("Enter your age")
gender = st.text_input("Enter your gender")
bmi = round(weight/(height/100)**2,2)
st.write(f"your bmi is: {bmi}")
user_promt = f"Act like a nutritionist with the following data: height is {height}, weight is {weight} and bmi is {bmi}"
response = model.generate_content(user_prompt)
st.markdown(response.text)


