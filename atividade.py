Qtd_alunos = int(input("Escreva a quantidade de alunos: "))                         #quantidade de alunos
cont = 1                                                                            #contador

while cont <= Qtd_alunos:                                                           #while para cada aluno
    print (f"\nDados do {cont}° aluno")                                             #identificando o aluno

    Nome = input("\nEscreva o nome do aluno: ")                                     #pedindo o nome do aluno
    Nt1 = float(input("\nEscreva a primeira nota do aluno: "))                      #pegando a primeira nota do aluno   
    Nt2 = float(input("Escreva a segunda nota do aluno: "))                         #pegando a segunda nota do aluno
    Nt3 = float(input("Escreva a terceira nota do aluno: "))                        #pegando a terceira notas do aluno
    Nt4 = float(input("Escreva a quarta nota do aluno: "))                          #pegando a quarta notas do aluno
    Faltas = int(input("\nEscreva a quantidade de faltas: "))                       #pedindo as faltas do aluno
    
    Media = (Nt1+Nt2+Nt3+Nt4)/4                                                     #calculo da media

    situação = bool                                                                 #situação do aluno (aprovado ou reprovado)

    if Media >= 8:
        situação = True

    elif Media >= 5:
        ntRec = float(input("\nEscreva a nota de recuperação do aluno: "))
        if ntRec < (10 - Media):
            situação = False
        else:
            situação = True
    
    else:
        situação = False
    
    print (situação)

    cont += 1                                                                       #incremeto do contador