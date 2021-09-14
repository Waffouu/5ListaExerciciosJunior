#Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem
#diferente para cada um dos casos a seguir:
#A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”;
#B) Se a média for menor que 7 e maior que 5, exiba a mensagem “Você ficou com média
#(media) e está de recuperação;
#C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”
media = 0
nome = str(input("Digite seu nome: "))
nota = int(input(f"Digite nota 1: "))
nota2 = int(input(f"Digite nota 2: "))
nota3 = int(input(f"Digite nota 3: "))
media = (nota + nota2 + nota3)/ 3
if media >= 7:
    print(f"Parabéns {nome}! Você foi aprovado")
elif 5 <= media < 7:
    print(f"Você ficou com média {media} e está de recuperação.")
elif media < 5:
    print(f"{nome}, você está reprovado")