import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos (ajusta la ruta si es necesario)
car_data = pd.read_csv('vehicles_us.csv')

st.header("Dashboard de anuncios de coches")
st.write("Aplicación web para visualizar datos de anuncios de vehículos en EE.UU.")

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    
    # Crear histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para histograma
hist_button = st.button('Construir histograma', key='hist')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    
    # Crear histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para scatter plot
scatter_button = st.button('Construir gráfico de dispersión', key='scatter')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: odometer vs price')
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig_scatter, use_container_width=True)

# Casillas de verificación
show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_hist:
    st.write('Histograma de la columna odometer')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Gráfico de dispersión: odometer vs price')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
