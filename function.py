import pyperclip
import random
import time
import os


PASTA_DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

NOME_DA_PASTA_SENHAS = "MinhasSenhasGerenciador"

CAMINHO_PASTA_COMPLETO = os.path.join(PASTA_DESKTOP, NOME_DA_PASTA_SENHAS)


os.system("cls")

def password_file():


    if not os.path.exists(CAMINHO_PASTA_COMPLETO):
        
        try:

            os.makedirs(CAMINHO_PASTA_COMPLETO)

            print(f"pasta {NOME_DA_PASTA_SENHAS} criada em {CAMINHO_PASTA_COMPLETO}")
        
        except IOError:

            print(f"erro ao criar pasta '{NOME_DA_PASTA_SENHAS}'")
            print("verifique suas permissões ou crie a pasta manualmente.")

def view_file():
    view_file("")

def line():
    print(" " * 50)
    print("=" * 50)
    print(" " * 50)

def new_password():
    """
        generate a new password
    """

    #variables to store the characters

    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    characters = []
    password = []



    print("Gerador de senhas")

    time.sleep(1)
    os.system("cls")


    while True:
        try:

            line()
            characters_range = int(input("coloque a quantidade de caracteres que deseja na senha: "))
            line()

            if characters_range < 1 or characters_range > 100:
                print("A quantidade de caracteres deve ser entre 1 e 100.")
                continue

            else:
                break
                os.system("cls")

        except ValueError:

            print("coloque somente um número válido entre 1 e 100.")

    os.system("cls")


    while True:
        try:

            line()
            print("Tipos de caracteres disponiveis:")
            print("1. Caracteres especiais.")
            print("2. Letras minúsculas.")
            print("3. Letras maiúsculas.")
            print("4. Números.")
            print("É possível misturar os tipos de caracteres separados para gerar uma senha. exemplo: 1 2 -> caracteres especiais e letras minúsculas\n.")


            options = str(input("coloque o número referente ao protocolo: ")).split()



            if not options:
                print("Nenhum tipo de caractere válido selecionado. Por favor, selecione pelo menos um tipo de caractere.")
                continue

            if "1" in options :
                characters.extend(special_characters)

            if "2" in options:
                characters.extend(lower_letters)

            if "3" in options:
                characters.extend(upper_letters)
                
            if "4" in options:
                    characters.extend(numbers)
            
            if not characters:
                line()
                os.system("cls")
                print("Nenhum tipo de caractere válido selecionado. Por favor, selecione pelo menos um tipo de caractere válido.")
                time.sleep(2)
                os.system("cls")
                continue

            break


        except ValueError:

            print("coloque somente números válidos separados por espaços. exemplo: 1 2 3 4.")
            time.sleep(1)
            os.system("cls")
            continue

    for i in range(characters_range):
        password.append(random.choice(characters))
    
    password = "".join(password)


    os.system("cls")
    line()

    print("Senha gerada: ", password)

    while True:
        try:

            copy_option = str(input("deseja copiar a senha para a área de transferência? (sim/não): "))

            if copy_option.lower() == "sim":
                pyperclip.copy(password)
                print("Senha copiada para a área de transferência.")
                break
            
            elif copy_option.lower() == "não" or copy_option.lower() == "nao":
                print("Senha não copiada para a área de transferência.")
                break

            else:
                print("Opção inválida. Por favor, digite 'sim' ou 'não'.")
                continue
        
        except ValueError:

            print("coloque somente 'sim' ou 'não'.")

    os.system("cls")
    line()

    while True:
        try:
            copy_option = str(input("salvar a senha? (sim/não): "))
            if copy_option.lower() == "sim":
                password_name = str(input("coloque o nome da senha: "))

                with open(f"{password_name}.txt", mode = "w") as file:
                    file.write(password)
                
                break

            elif copy_option.lower() == "não" or copy_option.lower() == "nao":
                print("Senha não salva.")
                break
            
            else:
                print("Opção inválida. Por favor, digite 'sim' ou 'não'.")
                continue
        
        except ValueError:
            print("coloque somente 'sim' ou 'não'.")
            continue

def show_passwords():
    
    while True:

        password_file = str(input("coloque o nome do arquivo de senhas que deseja ver (sem a extensão .txt): "))

        try:

            with open(f"{password_file}.txt", mode = "r") as file:
                passwords = file.read()
                print("Senhas salvas no arquivo:")
                print(passwords)
                break
            
        except FileNotFoundError:

            print(f"Arquivo '{password_file}.txt' não encontrado. Verifique o nome do arquivo e tente novamente.")      

def write_password():
        

    while True:
            
        password = str(input("coloque a sua senha: "))

        option = str(input("confirmar o nome da senha(sim/não): "))

        if option in ["sim", "não", "nao"]:
                
            if option in ["não", "nao"]:
                continue

            if option == "sim":
                break
            
        else:
            print("opção inválida. tente novamente.")
        
    while True:

        password_name = str(input("coloque o nome da senha: \n"))

        option = str(input("confirme (sim/não): \n"))

        os.system("cls")

        if option in ["sim", "não", "nao"]:
                
            if option in ["não", "nao"]:
                continue

            if option == "sim":
                break

        else:
            print("coloque um valor válido.")
            time.sleep(2)
            os.system("cls")
    
    with open(f"{password_name}.txt", mode="w") as file:
        file.write(password)