

def solucion():
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    subtotal = 0
    sistema_ON = True

    while sistema_ON:
        valor_unit_producto = int(input("Ingrese el valor unitario: "))
        tiene_iva = input("El producto cuenta con IVA? S/N: ")
        cantidad_de_productos = int(input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))
        if tiene_iva == "S":
            iva = (cantidad_de_productos * valor_unit_producto) * 0.19
            subtotal += (cantidad_de_productos * valor_unit_producto) + iva
            print("IVA incluído")
            print("SUBTOTAL:", subtotal)
        else:
            subtotal += (cantidad_de_productos * valor_unit_producto)
            print("PRODUCTO SIN IVA")
            print("SUBTOTAL: ",subtotal)
        ops_sistema = input("Faltan producto por cobrar? S/N: ")
        if ops_sistema == "N":
            print("TOTAL A COBRAR: ",subtotal)
            sistema_ON = False
    
solucion()