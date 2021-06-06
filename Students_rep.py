#Sudents Performance Analysis
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
 

st.title("Students Performance Analysis")

stud_file=pd.read_csv("StudentsFile.csv")
std_lunch=stud_file[stud_file["lunch"]=="standard"]
print("Students having standard lunch : ",std_lunch)

S_lunch=std_lunch["lunch"]
print("Number of Students having standard lunch : ",S_lunch.shape)
mark=stud_file[stud_file["math score"]>70]

print("Students with math score greater than 70",mark)
print("Student with Maximum math score is ",mark.max())
print("Mean of math score:",stud_file['math score'].mean())
print("Median of math score :",stud_file['math score'].median())
print("Variance of math score :",stud_file['math score'].var())

a=sns.pairplot(stud_file)
b=sns.jointplot(x='race/ethnicity',y='math score',data=stud_file,kind='scatter')


if st.button("No. of students having standard lunch"):
    st.write(S_lunch.shape)
if st.button("Students with math score greater than 70"):
    st.write(mark)
    
if st.button("Max Math score"):
    st.write(mark.max())
if st.button("Mean of Math score"):
    st.write(stud_file['math score'].mean())    
if st.button("Median of Math score"):
    st.write(stud_file['math score'].median())
if st.button("Variance of Math score"):
    st.write(stud_file['math score'].var())
if st.button("Pairplot of students performance"):
    st.pyplot(a)
if st.button("Joint plot of students performance"): 
    st.pyplot(b)   

