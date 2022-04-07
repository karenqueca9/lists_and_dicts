todo_list = ["estudiar python","sacar la basura","alimentar al Boby","recibir el bono","barrer la entrada"]

def check_if_exist(check, list):
    if check in list:
        return True

if check_if_exist("comer pastel",todo_list):
    print("tienes cosas por hacer")
else:            
    print("sin bono sigo en cama")

