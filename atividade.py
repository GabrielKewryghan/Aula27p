Qtd_alunos = int(input("Escreva a quantidade de alunos: "))                         #quantidade de alunos
cont = 1                                                                            #contador

while cont <= Qtd_alunos:                                                           #while para cada aluno
    print (f"\nDados do {cont}° aluno")                                             #identificando o aluno

    Nome = input("\nescreva o nome do aluno: ")                                     #pedindo o nome do aluno

    Nt1 = float(input("\nescreva a primeira nota do aluno: "))                      #pegando a primeira nota do aluno   
    Nt2 = float(input("escreva a segunda nota do aluno: "))                         #pegando a segunda nota do aluno
    Nt3 = float(input("escreva a terceira nota do aluno: "))                        #pegando a terceira notas do aluno
    Nt4 = float(input("escreva a quarta nota do aluno: "))                          #pegando a quarta notas do aluno

    Faltas = int(input("\nEscreva a quantidade de faltas: "))                       #pedindo as faltas do aluno
    
    Media = (Nt1+Nt2+Nt3+Nt4)/4

    cont += 1                                                                       #incremeto do contador