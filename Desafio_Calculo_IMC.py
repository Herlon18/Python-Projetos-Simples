# Desafio IMC de uma pessoa

kg = float(input("Digite seu pego em kg: "))
altura = float(input("Digite sua altura em metros separando por ponto: "))

print ("O seu Peso é {}".format (kg))
print ("A sua Altura é {}".format (altura))

imc = kg / (altura ** 2) # Calculo do IMC 

# Resultado do calculo formatado para apresentar apenas 2 caracteres do float utilizando round("Nome da variavel", "Numero dos caracteres")
imc_formatado = round(imc, 2)

print ("Seu IMC é:", imc_formatado)

# Apresentar resultado do calculo de acordo com as regras do IMC

if imc_formatado <= 18.4:
    print ("Você está abaixo do peso")
elif imc_formatado >= 18.5 and imc_formatado <= 24.9:
    print ("Você está na faixa de Peso Normal")
elif imc_formatado >= 25 and imc_formatado <= 29.9:
    print ("Você está com Sobrepeso")
elif imc_formatado >= 30 and imc_formatado <= 34.9:
    print ("Você está com Obesidade grau 1")
elif imc_formatado >= 35 and imc_formatado <= 39.9:
    print ("Você está com Obesidade grau 2")
else:
    print ("Você está com Obesidade grau 3")