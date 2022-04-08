programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto itera sobre las llaves, pero podria ser cualquier nombre: eje attr
for key in programmer:
    print(key)

# Podriamos imprimir los valores
for key in programmer:
    print(programmer[key]) 

for key, value in programmer.items():
    print(key, ":",value)       