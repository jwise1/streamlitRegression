import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import os 
import matplotlib.pyplot as plt
import dill
import pickle

# with open("model.dill", "rb") as f:
#     model=dill.load(f)

with open("weight.pkl", "rb") as f:
    weight = pickle.load(f)
with open("bias.pkl", "rb") as f:
    bias=pickle.load(f)

# Use the loaded values to make predictions 

# weight=7169074.5
# bias=221875330.0

def predictRecs(uMonth):
    return str((float(uMonth)*weight)+bias)

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df = df.fillna("None")
    return df

def main():
    # This sets the page title and a cute favicon
    st.set_page_config(page_title='Predicting 2023 Monthly Receipt Totals with Linear Regression', page_icon="🧾")

    data = load_data("data_daily.csv")

    st.title("Predicting Monthly Receipt Totals with Linear Regression🧾")

    # Set a few custom parameters to make our plot blend in with the white background
    custom_params = {"axes.spines.right": False, "axes.spines.top": False}
    sns.set_theme(style="ticks", rc=custom_params)
    sns.color_palette("Set2")

    # Plot the data using Seaborn's countplot
    fig, ax = plt.subplots(figsize=(30, 8))
    ax = sns.scatterplot(data,x=data["# Date"],y=data["Receipt_Count"])

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
