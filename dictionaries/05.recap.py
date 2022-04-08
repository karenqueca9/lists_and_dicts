programmer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Estas variables quedan referencias que se actualizan
keys = programmer.keys()
values = programmer.values()
items = programmer.items()

print(keys)
print(values)
print(items)

# Acá estamos agragando un nuevo item
programmer["dream"] = "Be a Python pro"

# Las llaves se actualizan considerando la nueva llave y valor agregados
print(items)