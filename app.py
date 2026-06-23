import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Read the CSV file into a DataFrame
car_data = pd.read_csv(r'C:\Users\aloan\Documents\vehicles_us\vehicles_us.csv')

st.header('Vehicle Data Analysis')

hist_button = st.button('Construir histograma')

if hist_button:
    # Create a histogram using matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(car_data['odometer'], bins=20, color='blue', edgecolor='black')
    plt.title('Distribution of Vehicle Odometer Readings')
    plt.xlabel('Odometer')
    plt.ylabel('Frequency')
    
    # Display the histogram in Streamlit
    st.pyplot(plt)

disperse_button = st.button('Construir scatter plot')

if disperse_button:
    # Create a scatter plot using matplotlib
    plt.figure(figsize=(10, 6))
    plt.scatter(car_data['odometer'], car_data['price'], color='red', alpha=0.5)
    plt.title('Relationship between Odometer and Price')
    plt.xlabel('Odometer')
    plt.ylabel('Price')

    # Display the scatter plot in Streamlit
    st.pyplot(plt)

