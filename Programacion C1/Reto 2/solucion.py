def veterinaria(nombres, tipos, edades, pesos):
    # ACÁ INICIA LA FUNCIÓN VETERINARIA
    # (En este espacio debe poner el código necesario para crear los diccionarios y promedios pedidos)
    diccionario = {}
    beneficiarios_can_fel = {}
    beneficiarios_equ_bov = {} 
    promedio_can_fel = 0
    promedio_equ_bov = 0
    suma_edades_can_fel_benf = 0
    suma_edades_equ_bov_benf = 0

    contador_diccionario = 0
    contador_beneficiarios_can_fel = 0
    contador_beneficiarios_equ_bov = 0
    
    while contador_diccionario < len(nombres):
        list_dato_actual = []
        list_dato_actual.append(nombres[contador_diccionario])
        list_dato_actual.append(tipos[contador_diccionario])
        list_dato_actual.append(edades[contador_diccionario])
        list_dato_actual.append(pesos[contador_diccionario])

        diccionario[str(contador_diccionario + 1)] = list_dato_actual

        if tipos[contador_diccionario] =="canino" or tipos[contador_diccionario]=="felino":
            if edades[contador_diccionario] >= 9:
                suma_edades_can_fel_benf += edades[contador_diccionario]
                
                list_dato_actual = []
                list_dato_actual.append(nombres[contador_diccionario])
                list_dato_actual.append(tipos[contador_diccionario])
                list_dato_actual.append(pesos[contador_diccionario])
                
                beneficiarios_can_fel[str(contador_beneficiarios_can_fel + 1)] = list_dato_actual
                
                contador_beneficiarios_can_fel += 1

        elif tipos[contador_diccionario] =="equino" or tipos[contador_diccionario]=="bovino":
            if edades[contador_diccionario] >= 16:
                suma_edades_equ_bov_benf += edades[contador_diccionario]

                list_dato_actual = []
                list_dato_actual.append(nombres[contador_diccionario])
                list_dato_actual.append(tipos[contador_diccionario])
                list_dato_actual.append(pesos[contador_diccionario])

                beneficiarios_equ_bov[str(contador_beneficiarios_equ_bov + 1)] = list_dato_actual
                
                contador_beneficiarios_equ_bov += 1

        contador_diccionario += 1

    if len(beneficiarios_can_fel) > 0:
        promedio_can_fel = suma_edades_can_fel_benf / len(beneficiarios_can_fel)
    
    if len(beneficiarios_equ_bov) > 0:
        promedio_equ_bov = suma_edades_equ_bov_benf / len(beneficiarios_equ_bov)

    if promedio_can_fel == 0:
        promedio_can_fel = None
    
    if promedio_equ_bov == 0:
        promedio_equ_bov = None
    
    # ACÁ TERMINA LA FUNCIÓN VETERINARIA
    # NO MODIFIQUE LA SIGUIENTE LÍNEA
    return diccionario, beneficiarios_can_fel, beneficiarios_equ_bov, promedio_can_fel, promedio_equ_bov



Nombres = ["Martín", "Milú", "Anastasia", "Lupita", "Tomasa", "Pelusa", "Genoveva", "Motita"]
Tipos= ["canino", "canino", "felino", "felino", "felino", "canino", "bovino", "roedor"]
Edades= [12, 9, 10, 8, 9, 2, 14, 1]
Pesos=[33, 26, 4, 5, 5, 6, 106.4, 0.34]

result = veterinaria(Nombres,Tipos, Edades, Pesos)
for i in result:
    print(i)
