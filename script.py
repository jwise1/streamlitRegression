import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import joblib

model = pickle.load(open('data/linReg.pkl','rb'))
#LR = joblib.load('data/linReg.pkl') 
# Use the loaded model to make predictions 

weight=200
bias=7
def predictRecs(uMonth):
    prediction = model(int(uMonth))
    
    return str(prediction)

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df = df.fillna("None")
    return df

def main():
    # This sets the page title and a cute favicon
    st.set_page_config(page_title='Predicting Monthly Receipt Totals with Linear Regression', page_icon="🧾")

    data = load_data("data/data_daily.csv")

    st.title("Predicting Monthly Receipt Totals with Linear Regression🧾")

    # Set a few custom parameters to make our plot blend in with the white background
    custom_params = {"axes.spines.right": False, "axes.spines.top": False}
    sns.set_theme(style="ticks", rc=custom_params)
    sns.color_palette("Set2")

    # Plot the data using Seaborn's countplot
    fig, ax = plt.subplots(figsize=(100, 50))
    ax = sns.scatterplot(data,x=data["Receipt_Count"],y=data["# Date"])

    st.pyplot(fig)

    uMonth = st.text_input("Enter month of 2023 as numeral","Type Here")

    safe_html ="""  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
        </div>
        """
    if st.button("Predict the receipt total"):
        output = predictRecs(uMonth)
        st.success('The predicted receipt total is {}'.format(str(output)))

if __name__=='__main__':
    main()