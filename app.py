import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.markdown("<h1 style='text-align: center; color: red;'>Proyecto 5 - Servicio Web</h1>", unsafe_allow_html=True)
build_histogram = st.checkbox('Construir histograma para la columna odometro') # crear un botón
build_scatter = st.checkbox('Construir Diagrama de Dispersion') # crear un botón


if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: 
    st.write('Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig=px.scatter(car_data, x="odometer")
    st.plotly_chart(fig,use_container_width=True)
