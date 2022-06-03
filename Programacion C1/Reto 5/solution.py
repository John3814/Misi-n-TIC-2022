#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las librería csv y json respectivamente
import csv, json
import numpy as np
"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)
def read_data():

    data = []
    data_detalles_json = {"date_lowest_volume":'', "lowest_volume":pow(1000,10), "date_highest_volume":'',"highest_volume":-1, "mean_volume":-1,"date_greatest_difference":"", "greatest_difference":-1}
    data_counter = 0
    sum_volume = 0

    with open('JandJ.csv') as File:
        reader = csv.DictReader(File)

        for data_i in reader:
            data_counter += 1
            date_i = data_i['Date']
            open_i = data_i['Open']
            close_i = data_i['Close']
            Volume_i = int(data_i['Volume'])

            status = ""
            if (float(close_i)-float(open_i))>0:
                status = 'SUBE'
            elif (float(close_i)-float(open_i))<0:
                status = 'BAJA'
            else:
                status = 'ESTABLE'

            abs = np.abs(float(close_i)-float(open_i))

            dic_date_i = {'Fecha analizada':date_i, 'Comportamiento de la accion':status, 'abs Diferencia Close-Open':abs}
            data.append(dic_date_i)

            if Volume_i < data_detalles_json['lowest_volume']:
                data_detalles_json['date_lowest_volume'] = date_i
                data_detalles_json['lowest_volume'] = Volume_i
            elif Volume_i > data_detalles_json['highest_volume']:
                data_detalles_json['date_highest_volume'] = date_i
                data_detalles_json['highest_volume'] = Volume_i

            sum_volume += Volume_i

            if abs > data_detalles_json['greatest_difference']:
                data_detalles_json['date_greatest_difference'] = date_i
                data_detalles_json['greatest_difference'] = abs
        data_detalles_json['mean_volume'] = sum_volume / data_counter

    return data, data_detalles_json

def write_data(data):
    with open('analisis_archivo.csv', 'w') as File:
        fieldnames = ['Fecha analizada', 'Comportamiento de la accion','abs Diferencia Close-Open']
        writer = csv.DictWriter(File, delimiter='\t',  fieldnames=fieldnames )
        writer.writeheader()
        for i in data:
            writer.writerow(i)

def write_json_data(data_detalles_json):
    with open('detalles.json', 'w') as File_json:
        json.dump(data_detalles_json, File_json)


"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    data, data_detalles_json= read_data()
    write_data(data)
    write_json_data(data_detalles_json)
    
            
              
        

solucion()
    
    
    
    