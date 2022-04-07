todo_list = ["estudiar python","sacar la basura","alimentar al Boby","recibir el bono","barrer la entrada"]

#Podemos eliminar un elemento en particular
element = todo_list.remove("recibir el bono")

print(todo_list)
print(element) #Esto es None!!

#El método pop() remueve el último y lo retorna.tambien acepta el índice
element = todo_list.pop(1)

print(todo_list)
print(element)

#Tambien existe la palabra clave "del"
del todo_list[1]

print(todo_list)

# Esto lo elimina del programa
del todo_list

#print(todo_list)

todo_list = ["estudiar python","sacar la basura","alimentar al Boby","recibir el bono","barrer la entrada"]

# Limpia toda la lista, pero no la elimina
todo_list.clear()

print(todo_list)