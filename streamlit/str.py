import streamlit as st
import pandas as pd

st.title("MY app")
st.write("Hello World")





data = {
    "name":["Raj","Shekhar","Monu","Gravity"],
    "age":[20,21,22,23]
    
}

st.write(pd.DataFrame(data))
