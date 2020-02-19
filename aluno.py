aluno = str(input("Nome do Aluno: "))
nota = int(input("Digite a nota do aluno: "))
aluno = aluno.upper()

print ("O aluno {}, tirou nota {}".format(aluno,nota))

if nota >= 7:
    print("Portanto o aluno está APROVADO. Parabéns")
else:
    print("O aluno está em RECUPERAÇÃO. Estude mais que você vai conseguir!")

