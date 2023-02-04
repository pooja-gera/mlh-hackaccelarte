import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_parking_price(num_cars, time_of_day):
    base_price = 5
    num_cars_price = num_cars * 0.5
    time_of_day_price = 0
    
    if time_of_day >= 8 and time_of_day <= 18:
        time_of_day_price = 2
    elif time_of_day > 18 and time_of_day <= 24:
        time_of_day_price = 4
    elif time_of_day >= 0 and time_of_day < 8:
        time_of_day_price = 1
        
    return base_price + num_cars_price + time_of_day_price

st.title("Parking Price Predictor")

num_cars = st.slider("Number of cars in the parking lot", 0, 100, 50)
time_of_day = st.slider("Time of day (hours)", 0, 24, 12)

price = calculate_parking_price(num_cars, time_of_day)

st.write("Parking price: ${:.2f}".format(price))
