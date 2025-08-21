
## Creacion de primer StreamLit app

import streamlit as st

st.write("Hola Mundo que mas puedo hacer? 🤔")

## st.button permite mostrar un botón.

## Que estamos construyendo?
## Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.

## Comportamiento de la aplicación:

## Por defecto, la aplicación imprime Goodbye
## Una vez que se hace click sobre el botón, la aplicación imprime Why hello there

st.header('st.button')

if st.button('Di Hola!!'):
    st.write('Gaaa')
else:
    st.write('Goodbye')


st.header('Parte 2', divider="blue")
st.header('st.write')
    
"""
st.write permite imprimir texto y datos en la Streamlit app.

Además de poder mostrar texto, también se puede mostrar lo siguiente mediante el comando st.write():

- Muestra cadenas; funciona como st.markdown()
- Muestra un dict de Python
- Muestra pandas DataFrame se puede mostrar como una tabla
- Gráficos/Esquemas/Representaciones de matplotlib, plotly, altair, graphviz, bokeh
- Y mas (ver st.write en la documentación de Streamlit)    
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st



## Ejemplo 1
st.write("aqui puedes agregar un mensaje!") 

## Ejemplo 2
st.write(12345)

## Ejemplo 3
df = pd.DataFrame({
    "col1" : [1,2,3,4],
    "col2" : [10,20,30,40]
})

st.write(df)

## Ejemplo 4
st.write("Abajo hay un datframe:", df, "Encima hay un dataframe")

## Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])


c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.header('Parte 3', divider="blue")
st.header('st.slider')

"""
st.slider

- st.slider permite la visualizacion de un control deslizante. 

Se admiten los sigueintes tipo de datos: int, float, date, time y datetime. 

## Que estamos construyendo?

Una aplicación simple que muestra diferentes maneras de como aceptar datos del usuario con el control deslizante

- Comportamiento de la aplicación:

1. El usuario selecciona el valor ajustando el control deslizante
2. La aplicación imprime el valor seleccionado

"""

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

## Ejemplo 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25) ## por defecto 25 años. 
st.write("I'm ", age, 'years old')

## Ejemplo 2

st.subheader('Range Slider')

values = st.slider("seleccione un rango de valores", 
                0.0, 100.0, 
                (25.0, 90.0) ## por defecto
                )

st.write('values:', values)

# Ejemplo 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Ejemplo 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

## Ejemplo 5. 

st.subheader('Selected slider')

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"), ## por defecto red and blue puedes borrar esto si deseas
)
st.write("My favorite color is", color)


st.header("Parte 4", divider="blue")
st.header("st.line_chart")

"""
st.line_chart muestra un gráfico de líneas.

- Esto es un syntax-sugar en torno a st.altair_chart. La principal diferencia es que este comando utiliza la columna y los índices propios de los datos para determinar las especificaciones del gráfico. Como resultado, esto es más fácil de usar para muchos escenarios, mientras que es menos personalizable.

- Si st.line_chart no adivina la especificación de datos correctamente, intente especificar su gráfico deseado usando st.altair_chart.

### Que estamos construyendo?

Una aplicación sencilla para mostrar un gráfico de líneas.

- Comportamiento de la aplicación:

1. Cree un DataFrame Pandas a partir de números generados aleatoriamente usando NumPy.
2. Cree y muestre el gráfico de líneas mediante el comando st.line_chart().

"""

import streamlit as st
import pandas as pd
import numpy as np


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.write(chart_data.head())

st.line_chart(chart_data)  ## Finalmente, se crea un gráfico de líneas usando st.line_chart() con el DataFrame almacenado en la variable chart_data como datos de entrada


st.header("Parte 5", divider="blue")
st.header("st.selectbox")

"""

- st.selectbox permite la visualización de un componente de selección.

### Que estamos construyendo?
- Una sencilla aplicación que pregunta al usuario cuál es su color favorito.

- Comportamiento de la aplicación:

- El usuario selecciona un color
- La aplicación imprime el color seleccionado

"""