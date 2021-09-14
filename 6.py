#Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no
#primeiro produto, 11% no segundo e apresente o valor final a ser pago.
val = float(input("Escreva valor do primeiro produto: "))
val2 = float(input("Escreva valor do segundo produto: "))
media1 = (val / 100) * 8
media2 = (val / 100) * 11
final = (val - media1) + (val2 - media2)
print(f"Valor final: {final}")