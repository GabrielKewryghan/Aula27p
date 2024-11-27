Qtd_alunos = int(input("Escreva a quantidade de alunos: "))                         #quantidade de alunos
cont = 1                                                                            #contador

while cont <= Qtd_alunos:                                                           #while para cada aluno
    print (f"Dados do {cont}° aluno")                                               #identificando o aluno

    Nome = input("\nescreva o nome do aluno: ")                                     #pedindo o nome do aluno

    #pegando as notas do aluno
    Nt1 = float(input("\nescreva a primeira nota do aluno: "))                      
    Nt2 = float(input("escreva a segunda nota do aluno: "))
    Nt3 = float(input("escreva a terceira nota do aluno: "))
    Nt4 = float(input("escreva a quarta nota do aluno: "))

    Faltas = int(input("\nEscreva a quantidade de faltas: "))                       #pedindo as faltas do aluno
    
    cont += 1