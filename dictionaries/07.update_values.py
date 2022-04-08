programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Actualizamos indicando la llave con el nuevo valor
programmer["position"] = "sr Software Developer"

print(programmer)

# Actualizando utilizando el método update entregando un diccionario con la llve a actualizar
programmer.update({"name": "Alice smith"})

print(programmer)

# Con el metodo update() podemos también agregar nuevas llaves con su valor
programmer.update({"hobbies": ["Cats", "Playstation","Contemplate the moon"]})

print(programmer["hobbies"])