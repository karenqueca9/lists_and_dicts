#Los diccionarios son estructuras similares a las listas o arreglos, pero se accede a sus elementos mediante "llaves o "key" y no pur su indice

#Ejemplo
#Definimos un diccionario utilizando llaves o "curly braces"
programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

#Accedemos a los elementos por la llave
print(programmer["name"])
#No podemos acceder por el indice
#print(programmer[0])
print(programmer["position"])
print(programmer["skills"])

#Tambien podemos acceder a sus elementos con el metodo get()
print(programmer.get("position"))

#son de tipo <class dict>
print(type(programmer))

#podemos acceder a todas sus llaves con el metodo keys()
keys = programmer.keys()
print(keys)