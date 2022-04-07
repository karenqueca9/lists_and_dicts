fruits = ["Mango","Piña","Durazno","Plátano", "Arándanos"]

# El metodo sort() es destructivo. Modifica la lista original
fruits.sort()

print(fruits)

# Por defecto ordena ascendente. Con la "key" reverse podemos ordenar en forma descendente
fruits.sort(reverse = True)

print(fruits)

grades = [10,9,10,9,8,8,5]

grades.sort(reverse = True)

print(grades)

cat_bag = ["hola", 12, True]

# No es posiblecompara enteros con strings
# cat_bag.sort()

print(cat_bag)

veggies = ["papas", "Quinoa","choclo","Papas"]

# Con el parametro "key" podemos indicar una funcion para que realice el ordenamiento
veggies.sort(key = str.lower)

print(veggies)

def strLength(elem):
    return len(elem)

# La lista será ordenana por el largo de los elementos
fruits.sort(key = strLength, reverse = True)    

print(fruits)

#cat_bag.sort(key = strLength) tambien es errror, los enteros no tienen largo

print(cat_bag)