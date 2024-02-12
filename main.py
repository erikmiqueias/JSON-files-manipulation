# Cadastro de Usuários + Lista de Tarefas
import json
from os import system
from time import sleep
from package.function import new_users, remove_user, insert_task, remove_task # Using modularization to divide functions

def menu():
    print("[1] - New User\n[2] - Remove User\n[3] - New Task\n[4] - Remove Task\n[5] - Exit")


def main():
    
    FILE_JSON = "/home/erik_miqueias/Documentos/JSON-files-manipulation/dados.json" # Use your path file
    
    while True:
        try:
            menu()
            option = int(input("Insert your option: "))
            match option:
                case 1:
                    name = input("Insert your name: ")
                    password = input('Insert your password: ')
                    
                    try:
                        cpf = input("Insert yout CPF: ")
                        int(cpf)
                        
                    except ValueError:
                        print("Insert just valid values!")
                        
                    if len(cpf) != 11:
                        system('clear')
                        print("CPF format invalid :(")
                        continue
                    new_users(FILE_JSON, name, password, cpf)
                        
                case 2:
                    try:
                        cpf = input("Insert your CPF to remove: ")
                        password = input(f"Insert your password: ")
                        int(cpf)
                        
                    except ValueError:
                        print("CPF format invalud :(")
                        
                    if len(cpf) != 11:
                        system('clear')
                        print("CPF format invalid :(")
                        continue
                    
                    remove_user(FILE_JSON, cpf, password)
                    
                case 3:
                    try:
                        cpf = input("Insert your CPF: ")
                        int(cpf)
                    except ValueError:
                        system('clear')
                        print("CPF format invalid!")
                        continue
                    
                    password = input("Insert your password: ")
                    your_task = input("Insert your new task: ")
                    insert_task(FILE_JSON, cpf, password, your_task)
                    
                case 4:
                    try:
                        cpf = input("Insert your CPF: ")
                        int(cpf)
                    except ValueError:
                        print("CPF format invalid!")
                        continue
                    password = input("Insert your password: ")
                    your_task = input("Insert your task to remove: ")
                    remove_task(FILE_JSON, cpf, password, your_task)
                    
                case 5:
                    system('clear')
                    print("Leaving...")
                    sleep(2)
                    break
                
                case _:
                    system('clear')
                    print("Invalid option!")
                
        except KeyboardInterrupt:
            system('clear')
            print("Impossible to interrupt program execution!")      
            continue

if __name__ == "__main__":
    print("USUÁRIOS")
    main()