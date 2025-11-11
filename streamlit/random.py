import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data    #every time the function is called with the same parameters, the cached result is returned no need to reload the data again and again
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names
    # return X, y



df,target_names = load_data()   


model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df["species"])   #in order to train the model we need to provide features and target variable (first is for all features excluding last feature as it is the species (result we need))


st.sidebar.title("Feature Input")
sepal_length = st.sidebar.slider("sepal Length", float(df["sepal length (cm)"].min()), float(df["sepal length (cm)"].max()))
sepal_width = st.sidebar.slider("sepal Width", float(df["sepal width (cm)"].min()), float(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("Petal Length", float(df["petal length (cm)"].min()), float(df["petal length (cm)"].max()))
petal_width = st.sidebar.slider("Petal Width", float(df["petal width (cm)"].min()), float(df["petal width (cm)"].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
prediction_species = target_names[prediction][0]

st.write("Predictions")
st.write(f"The predicted species is: {prediction_species}")