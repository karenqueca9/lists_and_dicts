todo_list = ["estudiar python","sacar la basura","alimentar al Boby","recibir el bono","barrer la entrada"]

#Agrega un item en el indice del primer parametro, desplazandolos otros items
todo_list.insert(2,"bañarme")

#Agrega al final
todo_list.append("ver friends")

print(todo_list)

#Mezclar
movies = ["El dia de la independencia", "American Pie","Scary Movie"]

books = ["Harry Potter","The Bro Code","Como entrenar a tu dragon"]

#Agrega al final todo el arreglo entregado como parametro
movies.extend(books)

print(movies)

print(books)
