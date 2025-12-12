turma=["Gustavo","Rodrigo","Marcelo","Henrique","Larissa"]
mat=[15,12,8,15,11]
port=[17,10,6,17,2]
ingl=[18,18,10,16,4]
aluno=input("qual é a media que deseja ver as notas: ")
if aluno in turma:
 posicao= turma.index(aluno)
 media_a= (mat[posicao] + port[posicao] + ingl[posicao]) / 3
 print(f"O {aluno} teve media de: {media_a[posicao]:.1f} valores")
elif aluno == "Mat":
 media_mat =sum(mat) / 5
 print(f"A média da turma em Matemática é de {media_mat:.1f}")
elif aluno == "Port":
 media_port = sum(port) / 5
 print(f"A média da turma em Português é de {media_port:.1f}")
elif aluno == "Ingl":
 media_ingl = sum(ingl) / 5
 print(f"A média da turma em Inglês é de {media_ingl:.1f}")
else:
 print("opção inválida")