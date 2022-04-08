programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# El método pop en los diccionarios requiere las llaves a eliminar
#position = programmer.pop("position")
#print(programmer)
#print(position)

# Otra forma de eliminar la llama ejemplo "position"
del programmer["position"]

print(programmer)

# Eliminar el diccionario completo
del programmer

#print(programmer) #Esto es un error al eliminar el programmer del programa

programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Vaciar el contenido del diccionario, pero manteniendo la variable
programmer.clear()

print(programmer) #Esto es lo que se imprime{}