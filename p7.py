import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
r=open("regression.pkl","rb")
regressor=pickle.load(r)
exp=st.number_input("Experience in Years:",0,42,1)
exp=np.array(exp).reshape(1,-1)
prediction=regressor.predict(exp)[0]
if st.button("Salary Prediction"):
    st.write(f"{prediction}")
