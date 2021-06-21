import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('randorm_forest_regression_model.pkl','rb'))



def main():
   
    html_temp="""
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-algin:center;">Old Car Selling App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Year = st.number_input("In Which Year you buy your Car",min_value=2010,max_value=2020,step=1)
    Present_Price = st.number_input(" What is the showroom Price(in lakhs)",min_value=2,step=1)
    Kms_Driven = st.number_input("How many Kilometers Drived",min_value=100,step=50)
    Kms_Driven2=np.log(Kms_Driven)
    Owner = st.slider("How much owners previously had the car(1 or 2 or 3",min_value=1,max_value=3)
    Fuel_Type_Diesel=0
    Fuel_Type_Petrol=st.radio("Fuel Type",options=['Petrol','Diesel'])
    if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    Year=2020-Year
    Seller_Type_Individual=st.radio("Are you a Dealer or Individual",options=['Dealer','Individual'])
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    Transmission_Mannual=st.radio("Transmission Type",options=['Manual','Auto'])
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
    if st.button("Calculate The Selling price"):
        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            st.error("Sorry you cant sell this car!")
        else:
            st.success("You Can Sell The Car at {}".format(output)+"Lakhs")

if __name__=="__main__":
    main()