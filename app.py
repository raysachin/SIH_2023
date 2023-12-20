import streamlit
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

from PIL import Image
st.set_page_config(
    page_title= "SOLAR CITY",
    page_icon= "RENEWABLE ENERGY"

)

temp=0
# # import the model
rf_model = pickle.load(open('lr_model.pkl', 'rb'))
st.title("SolarCity - Solar Generation Prediction ML Model")


col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input('Current Temperature (°C)')
with col2:
    humidity = st.number_input('Current Humidity')

col3, col4 = st.columns(2)
with col3:
    dew_point = st.number_input('Current Dewpoint (°C)')
with col4:
    precipitation = st.number_input('Current Precipitation')

col5, col6 = st.columns(2)
with col5:
    capacity = st.number_input('Solar Panel Capacity')

# Degree celsius to farehnheit
temperature = (9/5)*temperature + 32
dew_point = (9/5)*dew_point + 32
# for buttons
# if st.button('predict generation'):
#     input_df = pd.DataFrame({
#         'Temperature(°F)': [temperature],
#         'Humidity(%)': [humidity],
#         'Dew Point(°F)': [dew_point],
#         'Precipitation(in)': [precipitation]
#
#     })
#
#
#
#     st.table(input_df)
#     result = rf_model.predict(input_df)
#     temp = result
#     result = (result*capacity)/1000
#     if(humidity == 0 or dew_point == 0):
#         st.header("Check Your IOT device")
#     else:
#         st.header("Predicted Generation: " + str(result) + "kWh")



st.title("Actual Energy Genartion by Solar Panel")
col7, col8 = st.columns(2)
with col7:
    current = st.number_input('Current')
with col8:
    voltage = st.number_input('voltage')

power = (current*voltage)/1000
energy = power * 10

options = ["Yes", "No"]
selectbox_selection = st.selectbox("Is the Weather Cloudy?", options)
selectbox_selection2 = st.selectbox("Is the panel Clean?", options)


if st.button('predict generation'):
    input_df = pd.DataFrame({
        'Temperature(°F)': [temperature],
        'Humidity(%)': [humidity],
        'Dew Point(°F)': [dew_point],
        'Precipitation(in)': [precipitation]

    })



    st.table(input_df)
    result = rf_model.predict(input_df)
    temp = result
    result = (result*capacity)/1000
    if(humidity == 0 or dew_point == 0):
        st.header("Check Your IOT device")
    else:
        st.header("Predicted Generation: " + str(result) + "kWh")

    st.header("Actual Generation: " + str(energy) + "kWh")
    if (temp <= energy):
        st.header("Panel is working well")
    else:
        if(selectbox_selection == "Yes" and selectbox_selection2 == "Yes"):
            st.header("Low Generation Expected")
        elif(selectbox_selection == "No" and selectbox_selection2 == "Yes"):
            st.header("Check for preventive maintainance")
        elif (selectbox_selection == "No" and selectbox_selection2 == "No"):
            st.header("Clean the panel! Book your appointment")










