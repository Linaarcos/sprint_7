# Dashboard de Vehículos – Sprint 7

Este proyecto consiste en una **aplicación web interactiva** desarrollada con **Streamlit** para visualizar y explorar datos de anuncios de vehículos en EE.UU.  

Permite a los usuarios interactuar con los datos de manera sencilla y obtener visualizaciones clave sobre los vehículos.

## Funcionalidad

- Cargar y mostrar un **dataset de vehículos** (`vehicles_us.csv`).  
- Visualizar la **distribución del odómetro** mediante un histograma interactivo.  
- Visualizar la relación **precio vs odómetro** mediante un gráfico de dispersión interactivo.  
- Interactividad mediante **botones** o **casillas de verificación** para construir los gráficos a demanda.

## Tecnologías utilizadas

- **Python 3.13.5**  
- **Streamlit**: para crear la aplicación web interactiva.  
- **Pandas**: para manipulación de datos.  
- **Plotly Express**: para gráficos interactivos.

## Cómo ejecutar la aplicación

1. Asegúrate de tener activado tu **entorno virtual** con las librerías necesarias (`pandas`, `plotly-express`, `streamlit`).  
2. Desde la raíz del proyecto, ejecuta:

```bash
streamlit run app.py
