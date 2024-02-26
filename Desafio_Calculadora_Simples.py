# Calculadora Simples com Adição, Subtração, Multiplicação e Divisão

def  exibir_menu(): # Exibição do Menu
    print()
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print()

reset_color = "\033[0m" # Cor padrão para ser setada após mensagem de erro
red = "\033[1;31;40m" # Cor vermelha para mensagem de erro

while True: # Inicio do loop
    exibir_menu()

    opcao = int(input("Digite a opção desejada: "))

    if 1 <= opcao <= 4: # Função para delimitar numero digitado entre 1 e 4
        print()

    else: # Caso não seja entre 1 e 4 mostrar mensagem de erro em Vermelho e depois resetar a cor para padrão e reinicialização do loop
        print()
        print(red + "Opção inválida, escolha uma das opções a seguir." + reset_color)
        continue

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Agora segue a base da opção escolhida junto com a função imprimir e o break para parar o codigo após a exibição.

    if opcao == 1:
        adicao = numero1 + numero2
        adicao = round(adicao, 2)

        print()
        print (f"O resultado da Adição de {numero1} + {numero2} é : {adicao}")
        print()
        break

    elif opcao == 2:
        subtracao = numero1 - numero2
        subtracao = round(subtracao, 2)

        print()
        print (f"O resultado da Subtração de {numero1} - {numero2} é: {subtracao}")
        print()
        break

    elif opcao == 3:
        multiplicacao = numero1 * numero2
        multiplicacao = round(multiplicacao, 2)

        print()
        print (f"O resultado da Multiplicação de {numero1} * {numero2} é: {multiplicacao}")
        print()
        break

    elif opcao == 4:
        divisao = numero1 / numero2
        divisao = round(divisao, 2)

        print()
        print(f"O resultado da Divisão de {numero1} / {numero2} é: {divisao}")
        print()
        break