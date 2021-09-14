#Escreva um algoritmo que receba dois números e exiba para o usuário todos os valores
#intermediários a eles, veja exemplo:
#Primeiro número: 5
#Segundo número: 15
#Resultado: 6 7 8 9 10 11 12 13 14
num = int(input("Escreva primeiro número: "))
num2 = int(input("Escreva segundo número: "))
if num > num2:
    cont = num2 + 1
    while cont < num:
        print(cont)
        cont = cont + 1
else:
    cont = num + 1
    while cont < num2:
        print(cont)
        cont = cont + 1