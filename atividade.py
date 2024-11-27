Qtd_alunos = int(input("Escreva a quantidade de alunos: "))                         #quantidade de alunos
cont = 1                                                                            #contador

while cont <= Qtd_alunos:                                                           #while para cada aluno
    print (f"\n\nDados do {cont}° aluno")                                             #identificando o aluno

    Nome = input("\nEscreva o nome do aluno: ")                                     #pedindo o nome do aluno
    Nt1 = float(input("\nEscreva a primeira nota do aluno: "))                      #pegando a primeira nota do aluno   
    Nt2 = float(input("Escreva a segunda nota do aluno: "))                         #pegando a segunda nota do aluno
    Nt3 = float(input("Escreva a terceira nota do aluno: "))                        #pegando a terceira notas do aluno
    Nt4 = float(input("Escreva a quarta nota do aluno: "))                          #pegando a quarta notas do aluno
    Faltas = int(input("\nEscreva a quantidade de faltas: "))                       #pedindo as faltas do aluno
    
    Media = (Nt1+Nt2+Nt3+Nt4)/4                                                     #calculo da media

    if Media >= 8:                                                                  #caso media alcance a nota necessario para ser aprovado
        situação = "aprovado"                                                       #caso o aluno passe, situação recebe true
    elif Media >= 5:                                                                #caso a media alcance a nota de recuperação
        ntRec = float(input("\nEscreva a nota de recuperação do aluno: "))          #variavel com a nota de recuperação
        if ntRec < (10 - Media):                                                    #caso o aluno não alcance a nota de recuperação necessaria
            situação = "Reprovado"                                                  #nesse caso, situação recebe False
        else:                                                                       #em qualquer outro caso o aluno é aprovado
            situação = "aprovado"                                                   #situação recebe True
    else:                                                                           #em qualquer outro caso o aluno é reprovado
        situação = "Reprovado"                                                      #situação recebe False
    
    if Faltas > 30:                                                                 #Caso as faltas sejam maior que 30 o aluno é reprovado imediatamente
        situação = "Reprovado"                                                      #situação recebe False
    
    Media=round(Media,2)                                                            #arredondando a media

    #Relatorio do aluno
    print (f"\nNome: {Nome}\n\nNotas: {Nt1}, {Nt2}, {Nt3}, {Nt4}\nfaltas: {Faltas}\nMedia: {Media}\nSituação: {situação}")

    cont += 1                                                                       #incremeto do contador