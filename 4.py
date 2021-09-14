#Escreva um algoritmo que imprima na tela os números de 0 a 10, com exceção do 7.
num = 0

while num <= 7:
    if num == 7:
        num = num + 1
        while num <= 10:
            print(num)
            num = num + 1
    else:
        print(num)
        num = num + 1