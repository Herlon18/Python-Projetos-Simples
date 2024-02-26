# Conversor de Temperatura

# Função deixada de fora do loop pois não é necessario incluir, apenas o "exibir_menu" já funciona.
def exibir_menu(): # feito a função para exibição do Menu com varias linhas
        print("Escolha a opção de conversão: ")
        print("1. Celsius para Fahrenheit.")
        print("2. Fahrenheit para Celsius.")

while True: # Colocado para realizar o Loop no codigo p/ opções inválidas
    exibir_menu()

    opcao = int(input("Opção: ")) # Opção digitada de acordo com exibição do menu

    if opcao == 1:
        valor_celsius = float(input("Digite a temperatura em Celsius: ")) # Input para digitar a temperatura

        valor_convertido = (valor_celsius * 1.8) + 32 # Calculo da temperatura
        valor_convertido = round(valor_convertido, 2) # Valor arredondado para duas casas decimais do float

        print ("{} graus Celsius são aproximadamente {} graus Fahrenheit.".format (valor_celsius, valor_convertido))
        break # Caso essa opção seja escolhida, após o print o break serve para parar o loop

    elif opcao == 2: # Mesmo esquema do input acima 
        valor_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

        valor_convertido = ((valor_fahrenheit - 32) /1.8 )
        valor_convertido = round(valor_convertido, 2)

        print ("{} graus Fahrenheit são aproximadamente {} graus Celsius".format (valor_fahrenheit, valor_convertido))
        break # Para parar o loop caso opção seja escolhida

    else:
        print (" Opção Inválida, por favor escolha uma das opções mostradas.")

        # O else não possui o break, pois caso ele seja mostrado, vai reiniciar o codigo para o usuario escolher a opção correta.