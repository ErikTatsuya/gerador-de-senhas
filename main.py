import function
import os


while True:

    option = ""

    print("Bem-vindo ao Gerenciador de Senhas!")

    function.line()

    print("Selecione uma opção:")
    print("1. - Gerar uma nova senha aleatória")
    print("2. - Ver senhas salvas")
    print("3. - escrever uma nova senha")
    print("4. - Sair")

    option = input("Digite o número da opção desejada: ")


    if option == "1":
        os.system("cls")
        function.new_password()

    if option == "2":
        os.system("cls")
        function.show_passwords()

    if option == "3":
        os.system("cls")
        function.write_password()

    if option == "4":
        print("Saindo do Gerenciador de Senhas. Até logo!")
        break