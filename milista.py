# ejemplo de uso de listas
misnovias=["Agripina","Anastasia","Maria"]
misnumeros=[666,77,10]
# mostrando mis novias
print(misnovias)
# mostrando mis numeros
print(misnumeros)
print("---accediendo a los elementos de la lista---")
print(misnovias[1])
if "sandra" in misnovias:
    print("si, Maria6 esta en la lista de mis novias")
else:
    print("no eres mi novia")
    print("numero de novias")
    Nnovias=len(misnovias)
    print(f"numero de novias = {Nnovias}")
    print("ciclo for en listas")
    posicion=0
    for medianaranja in misnovias:
        print(posicion," " ,medianaranja)
        posicion= posicion+1