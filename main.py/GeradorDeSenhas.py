import random, os, time, pyperclip

#Função para criar uma linha de separação

def line():

    print(" " * 50)
    print("=" * 50)
    print(" " * 50)

#função para separar por espaços

def space():

    print(" " * 50)

os.system("cls")

#sistema de gerar senhas

gerar_senha = True

while gerar_senha == True:

    print(" / / / Gerador de senhas aleatórias \ \ \ ")
    line()
    crcs_list = []

    #quando o usuário digitar o número de caracteres da senha

    while True:

        try:

            numero_de_caracteres = int(input("--- quantidade de caracteres em sua senha: "))

            if numero_de_caracteres >= 100 or numero_de_caracteres < 5:

                print("o máximo de caracteres são 99 caracteres.")
                print("o minímo de caracteres são 5")

            else:

                break

        except ValueError:

            print("digite um número entre 5 e 99.")

    line()

    #selecionador de protocolos

    while True:

        print("selecione o tipo do protocolo.")
        line()
        print("a = (somente letras.)")
        space()
        print("b = (somente números.)")
        space()
        print("c = (somente simbolos.)")
        space()
        print("você também pode misturas os protocolos em sua senha.")
        protocolo = str(input("Tipo de protocolo: ")).lower()
        space()
        
        if protocolo and all(p in "abc" for p in protocolo):

            break

        else:

            time.sleep(1)
            line()
            print("protocolo inválido.")
            space()

    os.system("cls")

    caracteres_possiveis = []

    #caraceres possíveis para cada protocolo

    if "a" in protocolo:
        caracteres_possiveis.extend(list("abcdefghijklmnopqrstuvwxyz"))

    if "b" in protocolo:
        caracteres_possiveis.extend(list("1234567890"))

    if "c" in protocolo:
        caracteres_possiveis.extend(list("!@#$%¨&*()[]{}"))

    #embaralhador de senha

    for i in range(numero_de_caracteres):

        if caracteres_possiveis:

            crcs_list.append(random.choice(caracteres_possiveis))

        else:

            exit

    #senha final

    senha = "".join(crcs_list)

    #copiador de senhas

    os.system("cls")

    print("senha gerada.")
    print("senha: ", senha)


    line()

    while True:

        cop = str(input("deseja copiar a senha para a área de transferência? (sim / não): ")).lower()

        space()

        if cop == "sim":

            print("copiando senha para a área de trânsferência.")
            line()
            pyperclip.copy(senha)
            break

        elif cop == "não":

            print("senha não copiada.")
            line()
            break

        else:

            print("opção invalida, tente novamente.")
            space()

    senhas_salvas = []

    while True:

        sv_op = str(input("deseja salvar a senha? (sim / não): "))

        if sv_op == "sim":

            nome_salvamento = str(input("nome do salvamento da senha: "))
            print("salvando senha.")
            senhas_salvas.append((nome_salvamento, senha))
            line()
            break

        elif sv_op == "não":

            print("senha não salva.")
            line()
            break
            
        else:

            print("opção invalida, tente novamente.")
            space()

    #uso do menu principal

    print("digite ``continuar`` para continuar o programa.")
    space()
    print("digite ``fim`` para finalizar o programa.")
    space()
    print("digite ``senhas salvas`` ver as senhas salvas dentro do programa.")
    space()

    line()

    menu_loop = True

    while menu_loop == True:

        opç_menu = str(input("opções: "))

        if opç_menu == "gerar nova senha":

            menu_loop = False
            os.system("cls")

        elif opç_menu == "fim":
        
            print("programa finalizado.")
            menu_loop = False
            gerar_senha = False
        
        elif opç_menu == "senhas  salvas":

            print("senhas salvas:")

            for nome, senha in senhas_salvas:

                print(f"{nome}: {senha}")

        else:

            print("opção inválida, tente novamente.")