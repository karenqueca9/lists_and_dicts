fruits =["platano","kiwi","manzana","piña","melon","mangos","uvas"]

#Con rangos podemos obtener subconjuntos de la lista.El ultimo elemento del rango queda fuera
print(fruits[2:5])

#El siguiente ejemplo selecciona hasta el índice 3 (incluido)
print(fruits[:4])

#Desde el indice 3 hasta el final
print(fruits[:3])

#Esto imprime toda la lista
print(fruits[:])

#Siempre es desde el rango inferior incluido y excluido el rango superior
print(fruits[-4:-1])