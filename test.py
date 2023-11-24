#definir una lista

mi_lista = []
print(mi_lista)

mi_lista2 = ['a', 'b', 1, 2, ['carlos', 'maria'], {'nombre': 'juan', 'edad': 30}]
print(len(mi_lista2))

for elemento in mi_lista2:
    print(elemento)
print(mi_lista2[3])

print(mi_lista2[4][0]) #es lo mismo que -> for i in mi_lista2[4]: print(i)
print(mi_lista2[4][1])

#definir cantidad de elementos en una lista y que me permita agregar uno por uno los elementos
lista_vacia = []
n = int(input("Ingrese la cantidad de elementos: "))
for i in range(n):
    lista_vacia.append(input("Ingrese el elemento: "))
print(lista_vacia)
#lish comprehension con el for


lista_vacia2 = []
cant_elementos = int(input("Ingrese la cantidad de elementos: "))
for i in range(cant_elementos):
    valor = input("Ingrese el elemento: ")
    lista_vacia2.append(valor)
print(lista_vacia2)
#list comprehension - hace que se vea mas resumido el codigo
lista_vacia3 = [input("Ingrese el elemento: ") for elemento_guardar in range(cant_elementos)]
print(lista_vacia3)

#investigar los metodos filter y map y funciones como lambda.
#filter -> filtra los elementos de una lista
#map -> aplica una funcion a cada elemento de una lista
#lambda -> funcion anonima

#vectores bidimensionales y lista enlanzadas (proxima semana)

