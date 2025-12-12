turma =[]
mat =[]
port = []
ing =[]
medias=[]
n= int(input("quantos alunos tem a turma?"))
for i in range(n):
    aluno= input("insira o nome do aluno: ")
    aluno.lower
    turma.append(aluno)
    nm= float(input("insira a nota que o aluno teve em Mat: "))
    mat.append(nm)
    np= float(input("insira a nota que o aluno teve em Português: "))
    port.append(np)
    ni= float(input("insira a nota que o aluno teve em Inglês: "))
    ing.append(ni)
    m = (nm + np + ni) /3
    medias.append(m)
while True:
    ver= input("Oque deseja ver?")
    ver.lower
    if ver in turma:
        posicao= turma.index(ver)
        print(f"Notas:\n nota a matemática: {mat[posicao]} \n nota a portugês: {port[posicao]} \n nota a inglês: {ing[posicao]} \n media do total do aluno: {medias[posicao]:.1f}")
    elif ver == "mat":
        print(f"{sum(mat) / n:.1f}")
    elif ver == "port":
        print(f"{sum(port) / n:.1f}")
    elif ver == "ing":
        print(f"{sum(ing) / n:.1f}")
    elif ver == "maior":
        maior_media= max(medias)
        print(f"o aluno com maior média: {turma[medias.index(maior_media)]}")
    elif ver == "menor":
        menor_media= min(medias)
        print(f"o aluno com menor média: {turma[medias.index(menor_media)]}")
    elif ver == "sair":
        break
    else:

        print("opção inválida")
