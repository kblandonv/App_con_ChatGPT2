import streamlit as st

def temperatura():
    st.subheader('Conversiones de temperatura')
    opcion_temp = st.selectbox('Seleccione el tipo de conversión:',
                               ('Celsius a Fahrenheit', 'Fahrenheit a Celsius',
                                'Celsius a Kelvin', 'Kelvin a Celsius'))

    if opcion_temp == 'Celsius a Fahrenheit':
        celsius = st.number_input('Ingrese los grados Celsius:')
        fahrenheit = (celsius * 9/5) + 32
        st.write(f'{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.')

    elif opcion_temp == 'Fahrenheit a Celsius':
        fahrenheit = st.number_input('Ingrese los grados Fahrenheit:')
        celsius = (fahrenheit - 32) * 5/9
        st.write(f'{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.')

    elif opcion_temp == 'Celsius a Kelvin':
        celsius = st.number_input('Ingrese los grados Celsius:')
        kelvin = celsius + 273.15
        st.write(f'{celsius} grados Celsius equivalen a {kelvin} grados Kelvin.')

    elif opcion_temp == 'Kelvin a Celsius':
        kelvin = st.number_input('Ingrese los grados Kelvin:')
        celsius = kelvin - 273.15
        st.write(f'{kelvin} grados Kelvin equivalen a {celsius} grados Celsius.')

def longitud():
    st.subheader('Conversiones de longitud')
    # Agrega aquí las conversiones de longitud

def peso_masa():
    st.subheader('Conversiones de peso/masa')
    # Agrega aquí las conversiones de peso/masa

def volumen():
    st.subheader('Conversiones de volumen')
    # Agrega aquí las conversiones de volumen

def tiempo():
    st.subheader('Conversiones de tiempo')
    # Agrega aquí las conversiones de tiempo

def velocidad():
    st.subheader('Conversiones de velocidad')
    # Agrega aquí las conversiones de velocidad

def area():
    st.subheader('Conversiones de área')
    # Agrega aquí las conversiones de área

def energia():
    st.subheader('Conversiones de energía')
    # Agrega aquí las conversiones de energía

def presion():
    st.subheader('Conversiones de presión')
    # Agrega aquí las conversiones de presión

def tamaño_datos():
    st.subheader('Conversiones de tamaño de datos')
    # Agrega aquí las conversiones de tamaño de datos

# Título y descripción de la aplicación
st.title('Conversor Universal')
st.write('Seleccione la categoría y el tipo de conversión que desea realizar.')

# Opciones para seleccionar la categoría
categorias = ['Temperatura', 'Longitud', 'Peso/Masa', 'Volumen', 'Tiempo',
              'Velocidad', 'Área', 'Energía', 'Presión', 'Tamaño de Datos']
opcion_categoria = st.selectbox('Seleccione la categoría:', categorias)

# Lógica para mostrar las opciones de conversión basadas en la categoría seleccionada
if opcion_categoria == 'Temperatura':
    temperatura()
elif opcion_categoria == 'Longitud':
    longitud()
elif opcion_categoria == 'Peso/Masa':
    peso_masa()
elif opcion_categoria == 'Volumen':
    volumen()
elif opcion_categoria == 'Tiempo':
    tiempo()
elif opcion_categoria == 'Velocidad':
    velocidad()
elif opcion_categoria == 'Área':
    area()
elif opcion_categoria == 'Energía':
    energia()
elif opcion_categoria == 'Presión':
    presion()
elif opcion_categoria == 'Tamaño de Datos':
    tamaño_datos()
