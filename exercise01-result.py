listaClientes = []
respuesta=""
costototal=0 

respuesta=input("¿Desea ingresar clientes?")
if respuesta=="si":
    while respuesta == "si":
        cliente = input("nombre del cliente: ")
        producto = input("producto: ")
        costo = float(input("costo ($0.00): "))
        registro = dict(cliente=cliente, producto=producto, costo=costo)

        listaClientes.append(registro)

        for registro in listaClientes:
            print(registro)
        respuesta=input("¿Desea ingresar clientes?")  
    else: 
        if respuesta == "no":   
        #no supe como hacer para que sumara :(
            costototal = str(costototal)
            print ("Perfecto. El costo total hasta este momento es: "+costototal)
        else:
            print ("Esa respuesta no es válida")
elif respuesta == "no":
    costototal = str(costototal)
    print ("Perfecto. El costo total hasta este momento es: "+costototal)
else:
    print ("Esa respuesta no es válida")