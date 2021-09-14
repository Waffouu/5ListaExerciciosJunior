#Escrevaum algoritmoque leia o ano de nascimento de dez pessoas e no final mostre quantas 
#pessoas são maiores de idade.
cont = 1
num2 = 0
while cont <= 10:
    num = int(input(f"Digite a data de nascimento da {cont}° pessoa: "))
    cont = cont + 1
    if num <= 2003:
        num2 = num2 + 1
print (f"{num2} pessoas são maior de idade.")