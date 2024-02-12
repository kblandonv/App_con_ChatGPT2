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
    opcion_longitud = st.selectbox('Seleccione el tipo de conversión:',
                                   ('Pies a metros', 'Metros a pies',
                                    'Pulgadas a centímetros', 'Centímetros a pulgadas'))

    if opcion_longitud == 'Pies a metros':
        pies = st.number_input('Ingrese la longitud en pies:')
        metros = pies * 0.3048
        st.write(f'{pies} pies equivalen a {metros} metros.')

    elif opcion_longitud == 'Metros a pies':
        metros = st.number_input('Ingrese la longitud en metros:')
        pies = metros / 0.3048
        st.write(f'{metros} metros equivalen a {pies} pies.')

    elif opcion_longitud == 'Pulgadas a centímetros':
        pulgadas = st.number_input('Ingrese la longitud en pulgadas:')
        centimetros = pulgadas * 2.54
        st.write(f'{pulgadas} pulgadas equivalen a {centimetros} centímetros.')

    elif opcion_longitud == 'Centímetros a pulgadas':
        centimetros = st.number_input('Ingrese la longitud en centímetros:')
        pulgadas = centimetros / 2.54
        st.write(f'{centimetros} centímetros equivalen a {pulgadas} pulgadas.')



def peso_masa():
    st.subheader('Conversiones de peso/masa')
    opcion_peso = st.selectbox('Seleccione el tipo de conversión:',
                               ('Libras a kilogramos', 'Kilogramos a libras',
                                'Onzas a gramos', 'Gramos a onzas'))

    if opcion_peso == 'Libras a kilogramos':
        libras = st.number_input('Ingrese el peso en libras:')
        kilogramos = libras * 0.453592
        st.write(f'{libras} libras equivalen a {kilogramos} kilogramos.')

    elif opcion_peso == 'Kilogramos a libras':
        kilogramos = st.number_input('Ingrese el peso en kilogramos:')
        libras = kilogramos / 0.453592
        st.write(f'{kilogramos} kilogramos equivalen a {libras} libras.')

    elif opcion_peso == 'Onzas a gramos':
        onzas = st.number_input('Ingrese el peso en onzas:')
        gramos = onzas * 28.3495
        st.write(f'{onzas} onzas equivalen a {gramos} gramos.')

    elif opcion_peso == 'Gramos a onzas':
        gramos = st.number_input('Ingrese el peso en gramos:')
        onzas = gramos / 28.3495
        st.write(f'{gramos} gramos equivalen a {onzas} onzas.')


def volumen():
    st.subheader('Conversiones de volumen')
    opcion_volumen = st.selectbox('Seleccione el tipo de conversión:',
                                   ('Galones a litros', 'Litros a galones',
                                    'Pulgadas cúbicas a centímetros cúbicos', 'Centímetros cúbicos a pulgadas cúbicas'))

    if opcion_volumen == 'Galones a litros':
        galones = st.number_input('Ingrese el volumen en galones:')
        litros = galones * 3.78541
        st.write(f'{galones} galones equivalen a {litros} litros.')

    elif opcion_volumen == 'Litros a galones':
        litros = st.number_input('Ingrese el volumen en litros:')
        galones = litros / 3.78541
        st.write(f'{litros} litros equivalen a {galones} galones.')

    elif opcion_volumen == 'Pulgadas cúbicas a centímetros cúbicos':
        pulgadas_cubicas = st.number_input('Ingrese el volumen en pulgadas cúbicas:')
        centimetros_cubicos = pulgadas_cubicas * 16.3871
        st.write(f'{pulgadas_cubicas} pulgadas cúbicas equivalen a {centimetros_cubicos} centímetros cúbicos.')

    elif opcion_volumen == 'Centímetros cúbicos a pulgadas cúbicas':
        centimetros_cubicos = st.number_input('Ingrese el volumen en centímetros cúbicos:')
        pulgadas_cubicas = centimetros_cubicos / 16.3871
        st.write(f'{centimetros_cubicos} centímetros cúbicos equivalen a {pulgadas_cubicas} pulgadas cúbicas.')


def tiempo():
    st.subheader('Conversiones de tiempo')
    opcion_tiempo = st.selectbox('Seleccione el tipo de conversión:',
                                 ('Horas a minutos', 'Minutos a segundos',
                                  'Días a horas', 'Semanas a días'))

    if opcion_tiempo == 'Horas a minutos':
        horas = st.number_input('Ingrese la cantidad de horas:')
        minutos = horas * 60
        st.write(f'{horas} horas equivalen a {minutos} minutos.')

    elif opcion_tiempo == 'Minutos a segundos':
        minutos = st.number_input('Ingrese la cantidad de minutos:')
        segundos = minutos * 60
        st.write(f'{minutos} minutos equivalen a {segundos} segundos.')

    elif opcion_tiempo == 'Días a horas':
        dias = st.number_input('Ingrese la cantidad de días:')
        horas = dias * 24
        st.write(f'{dias} días equivalen a {horas} horas.')

    elif opcion_tiempo == 'Semanas a días':
        semanas = st.number_input('Ingrese la cantidad de semanas:')
        dias = semanas * 7
        st.write(f'{semanas} semanas equivalen a {dias} días.')


def velocidad():
    st.subheader('Conversiones de velocidad')
    opcion_velocidad = st.selectbox('Seleccione el tipo de conversión:',
                                    ('Millas por hora a kilómetros por hora', 'Kilómetros por hora a metros por segundo',
                                     'Nudos a millas por hora', 'Metros por segundo a pies por segundo'))

    if opcion_velocidad == 'Millas por hora a kilómetros por hora':
        mph = st.number_input('Ingrese la velocidad en millas por hora:')
        kph = mph * 1.60934
        st.write(f'{mph} millas por hora equivalen a {kph} kilómetros por hora.')

    elif opcion_velocidad == 'Kilómetros por hora a metros por segundo':
        kph = st.number_input('Ingrese la velocidad en kilómetros por hora:')
        mps = kph / 3.6
        st.write(f'{kph} kilómetros por hora equivalen a {mps} metros por segundo.')

    elif opcion_velocidad == 'Nudos a millas por hora':
        nudos = st.number_input('Ingrese la velocidad en nudos:')
        mph = nudos * 1.15078
        st.write(f'{nudos} nudos equivalen a {mph} millas por hora.')

    elif opcion_velocidad == 'Metros por segundo a pies por segundo':
        mps = st.number_input('Ingrese la velocidad en metros por segundo:')
        fps = mps * 3.28084
        st.write(f'{mps} metros por segundo equivalen a {fps} pies por segundo.')


def area():
    st.subheader('Conversiones de área')
    opcion_area = st.selectbox('Seleccione el tipo de conversión:',
                               ('Metros cuadrados a pies cuadrados', 'Pies cuadrados a metros cuadrados',
                                'Kilómetros cuadrados a millas cuadradas', 'Millas cuadradas a kilómetros cuadrados'))

    if opcion_area == 'Metros cuadrados a pies cuadrados':
        metros_cuadrados = st.number_input('Ingrese el área en metros cuadrados:')
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f'{metros_cuadrados} metros cuadrados equivalen a {pies_cuadrados} pies cuadrados.')

    elif opcion_area == 'Pies cuadrados a metros cuadrados':
        pies_cuadrados = st.number_input('Ingrese el área en pies cuadrados:')
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f'{pies_cuadrados} pies cuadrados equivalen a {metros_cuadrados} metros cuadrados.')

    elif opcion_area == 'Kilómetros cuadrados a millas cuadradas':
        kilometros_cuadrados = st.number_input('Ingrese el área en kilómetros cuadrados:')
        millas_cuadradas = kilometros_cuadrados * 0.386102
        st.write(f'{kilometros_cuadrados} kilómetros cuadrados equivalen a {millas_cuadradas} millas cuadradas.')

    elif opcion_area == 'Millas cuadradas a kilómetros cuadrados':
        millas_cuadradas = st.number_input('Ingrese el área en millas cuadradas:')
        kilometros_cuadrados = millas_cuadradas / 0.386102
        st.write(f'{millas_cuadradas} millas cuadradas equivalen a {kilometros_cuadrados} kilómetros cuadrados.')


def energia():
    st.subheader('Conversiones de energía')
    opcion_energia = st.selectbox('Seleccione el tipo de conversión:',
                                   ('Julios a calorías', 'Calorías a kilojulios',
                                    'Kilovatios-hora a megajulios', 'Megajulios a kilovatios-hora'))

    if opcion_energia == 'Julios a calorías':
        julios = st.number_input('Ingrese la energía en julios:')
        calorias = julios / 4.184
        st.write(f'{julios} julios equivalen a {calorias} calorías.')

    elif opcion_energia == 'Calorías a kilojulios':
        calorias = st.number_input('Ingrese la energía en calorías:')
        kilojulios = calorias * 0.004184
        st.write(f'{calorias} calorías equivalen a {kilojulios} kilojulios.')

    elif opcion_energia == 'Kilovatios-hora a megajulios':
        kilovatios_hora = st.number_input('Ingrese la energía en kilovatios-hora:')
        megajulios = kilovatios_hora * 3.6
        st.write(f'{kilovatios_hora} kilovatios-hora equivalen a {megajulios} megajulios.')

    elif opcion_energia == 'Megajulios a kilovatios-hora':
        megajulios = st.number_input('Ingrese la energía en megajulios:')
        kilovatios_hora = megajulios / 3.6
        st.write(f'{megajulios} megajulios equivalen a {kilovatios_hora} kilovatios-hora.')


def presion():
    st.subheader('Conversiones de presión')
    opcion_presion = st.selectbox('Seleccione el tipo de conversión:',
                                  ('Pascales a atmósferas', 'Atmósferas a pascales',
                                   'Barras a libras por pulgada cuadrada', 'Libras por pulgada cuadrada a bares'))

    if opcion_presion == 'Pascales a atmósferas':
        pascales = st.number_input('Ingrese la presión en pascales:')
        atm = pascales / 101325
        st.write(f'{pascales} pascales equivalen a {atm} atmósferas.')

    elif opcion_presion == 'Atmósferas a pascales':
        atm = st.number_input('Ingrese la presión en atmósferas:')
        pascales = atm * 101325
        st.write(f'{atm} atmósferas equivalen a {pascales} pascales.')

    elif opcion_presion == 'Barras a libras por pulgada cuadrada':
        barras = st.number_input('Ingrese la presión en barras:')
        psi = barras * 14.5038
        st.write(f'{barras} barras equivalen a {psi} libras por pulgada cuadrada.')

    elif opcion_presion == 'Libras por pulgada cuadrada a bares':
        psi = st.number_input('Ingrese la presión en libras por pulgada cuadrada:')
        barras = psi / 14.5038
        st.write(f'{psi} libras por pulgada cuadrada equivalen a {barras} barras.')


def tamaño_datos():
    st.subheader('Conversiones de tamaño de datos')
    opcion_datos = st.selectbox('Seleccione el tipo de conversión:',
                                ('Megabytes a gigabytes', 'Gigabytes a terabytes',
                                 'Kilobytes a megabytes', 'Terabytes a petabytes'))

    if opcion_datos == 'Megabytes a gigabytes':
        megabytes = st.number_input('Ingrese el tamaño en megabytes:')
        gigabytes = megabytes / 1024
        st.write(f'{megabytes} megabytes equivalen a {gigabytes} gigabytes.')

    elif opcion_datos == 'Gigabytes a terabytes':
        gigabytes = st.number_input('Ingrese el tamaño en gigabytes:')
        terabytes = gigabytes / 1024
        st.write(f'{gigabytes} gigabytes equivalen a {terabytes} terabytes.')

    elif opcion_datos == 'Kilobytes a megabytes':
        kilobytes = st.number_input('Ingrese el tamaño en kilobytes:')
        megabytes = kilobytes / 1024
        st.write(f'{kilobytes} kilobytes equivalen a {megabytes} megabytes.')

    elif opcion_datos == 'Terabytes a petabytes':
        terabytes = st.number_input('Ingrese el tamaño en terabytes:')
        petabytes = terabytes / 1024
        st.write(f'{terabytes} terabytes equivalen a {petabytes} petabytes.')


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
