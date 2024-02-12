import json
from os import system
def new_users(file_name, name, password, cpf):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
            
    data_user = {
        'nome': name,
        'senha': password,
        'cpf': f'{cpf}',
        'tarefas': [],
    }
    
    data[cpf] = data_user
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        system('clear')
        print("User added sucessfully!")
        
def remove_user(file_name, cpf, password):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if cpf in data:
        if password == data[cpf]['senha']:
            del data[cpf]
            with open(file_name, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                system('clear')
                print("User removed sucessfully!")
            
        else:
            system('clear')
            print("Invalid password!")
    else:
        system('clear')
        print(f"CPF: '{cpf} not found!")
        
        
def insert_task(file_name, cpf, password, task):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
    
    if cpf in data:
        if password == data[cpf]['senha']:
            new_task = data[cpf]['tarefas']
            new_task.append(task)
            system('clear')
            print("Task assigned sucessfully!")
            
        else:
            system('clear')
            print("Invalid password!")
            
    else:
        system('clear')
        print(f"CPF: '{cpf}' not found!")
    
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
        
def remove_task(file_name, cpf, password, task):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
        
    if task not in data[cpf]['tarefas']:
        system('clear')
        print("Task not found!")
        
    else:
        lista = data[cpf]['tarefas']
        for i in lista:
            if task in i:
                lista.remove(task)
                
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        system('clear')
        print("Task removed sucessfully!")           
    