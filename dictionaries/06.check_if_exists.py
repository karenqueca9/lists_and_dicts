programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto al buscar en el diccionario, se busca por las llaves
if "position" in programmer:
    print("Existe la posición")

# No va a buscar directamente en los valores
if "Alice" in programmer:
    print("Alice esta presente")

# De esta forma podemos buscar en los valores
if "Alice" in programmer.values():
    print("Alice esta en los valores")