todo_list = ["estudiar python","sacar la basura","alimentar al Boby","recibir el bono","barrer la entrada"]

for todo in todo_list:
    print(todo)

index = 0
while index < len(todo_list):
    print(todo_list[index])
    index += 1

#El índice termina en 5 por la ultima iteración
    print(index)

#Utilizando list comprehensions
    [print(todo) for todo in todo_list]
