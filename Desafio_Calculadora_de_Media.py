# Desafio Calculadora de Média

print ("Digite as suas notas")
print()


while True:
    nota1 = float(input("Digite a primeira nota: "))
    if 0 <= nota1 <= 10:
        break
    else:
        print("Nota inválida, por favor, digita uma nota de 0 a 10")


while True:
    nota2 = float(input("Digita a segunda nota:"))
    if 0 <= nota2 <= 10:
            break
    else:
        print("Nota inválida, por favor, digita uma nota de 0 a 10")


while True:
    nota3 = float(input("Digite a terceira nota: "))
    if 0 <= nota3 <= 10:
            break
    else:
        print("Nota inválida, por favor, digita uma nota de 0 a 10")

valor_media = (nota1 + nota2 + nota3) / 3

print (f" A média das notas é {valor_media:.2f}")