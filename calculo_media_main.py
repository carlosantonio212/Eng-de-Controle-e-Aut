#calculo de media 
print("digite o nome do a:")
nome = input()

print("Digite a nota 1 do aluno:")
nota1 = float(input())

print("Digite a nota 2 do aluno:")
nota2 = float(input())

media = (nota1 + nota2)/2
print ("o nome informado é " + nome)
print ("as notas digitadas foram :" , nota1, "e", nota2)

msg_final = "a média de " + nome + " é " + str(media)

print(msg_final)