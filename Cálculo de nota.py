print("Digite a primeria nota: ")
nota1 = float(input())

print("Digite a segunda nota: ")
nota2 = float(input())

media = (nota1 + nota2)/2

print("A média obtida foi:", media)

if media >= 7 :
    print("Aluno aprovado! Parabéns!")
elif media >=3 :
    print("Aluno está na final! Estude!")
else:
    print("Aluno foi reprovado! Fica para próxima!")

print("Fim do programa!")