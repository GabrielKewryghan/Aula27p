# Função para cadastrar alunos
def cadastro(Nomes, Notas, Faltas, Media, situacoes):
    cont = 1  # Contador para o número de alunos

    Qtd_alunos = int(input("\nEscreva a quantidade de alunos que deseja cadastrar: ")) 
    print ("----------------------------------------------------------------------------------------------------------")

    # Inicia o cadastro de alunos
    while cont <= Qtd_alunos:                                                           
        print (f"\n\nDados do {cont}° aluno")                                          

        # Recebe os dados do aluno
        Nome = input("\nEscreva o nome do aluno: ")                                     
        Nt1 = float(input("\nEscreva a primeira nota do aluno: "))                      
        Nt2 = float(input("Escreva a segunda nota do aluno: "))                         
        Nt3 = float(input("Escreva a terceira nota do aluno: "))                        
        Nt4 = float(input("Escreva a quarta nota do aluno: "))                          
        QtdFaltas = int(input("\nEscreva a quantidade de faltas: "))       
        
        if Nome is None or Nt1 is None or Nt2 is None or Nt3 is None or Nt4 is None or QtdFaltas is None:
            print("\nAlguma informação não foi preenchida, tente novamente")
            continue  # Volta para o início do loop para tentar novamente             

        # Calcula a média
        Media = (Nt1 + Nt2 + Nt3 + Nt4) / 4                                                

        # Define a situação do aluno com base nas notas
        if Media > 10 or Media < 0:                                                     
            situacao = "Dados invalidos"
        elif QtdFaltas > 30:                                                              
            situacao = "Reprovado por faltas" 
        elif Media >= 8:                                                                  
            situacao = "Aprovado"                                                    
        elif Media >= 5:                                                               
            ntRec = float(input("\nEscreva a nota de recuperação do aluno: "))          
            if ntRec < (10 - Media):                                                    
                situacao = "Reprovado na recuperação"                                                  
            else:                                                                       
                situacao = "Aprovado na recuperação"                                                   
        else:                                                                           
            situacao = "Reprovado"                                                 

        # Arredonda a média
        Media = round(Media, 2)                                                            

        # Armazena as informações dos alunos
        Nomes.append(f"Nome: {Nome}")
        Notas.append(f"Notas: {Nt1}, {Nt2}, {Nt3}, {Nt4}")
        Faltas.append(f"Faltas: {QtdFaltas}")
        Medias.append(f"Média: {Media}")
        situacoes.append(f"Situação: {situacao}")

        cont += 1  # Incrementa o contador de alunos
        print ("--------------------------------------------------------------------------------------------------")

    return Nomes, Notas, Faltas, Medias, situacoes


# Função para exibir o relatório dos alunos
def relatorio(Nomes, Notas, Faltas, Medias, situacoes):
    contAR = 0  # Contador para exibir o relatório
    contgeral = len(Nomes)  # Número total de alunos cadastrados

    while contAR < contgeral:
        print(Nomes[contAR], "\n", Notas[contAR], "\n", Faltas[contAR], "\n", Medias[contAR], "\n", situacoes[contAR])
        print("--------------------------------------------------")
        contAR += 1

# Declara as listas fora da função, para manter os dados entre as chamadas
Nomes = []                                                                                  
Notas = []                                                                                  
Faltas = []                                                                                 
Medias = []                                                                                 
situacoes = []

# Loops de interação com o usuário
Decisao = int

while Decisao != 0:
    print("----------------------------------------------------------------------------------------------------------")
    print("\nO que deseja fazer?\n\nCadastrar alunos = 1\nVer o relatório dos alunos = 2\nSair do Menu = 0")
    Decisao = int(input("\nEscreva o número relacionado à ação que quer fazer (1, 2 ou 0): "))
    print("----------------------------------------------------------------------------------------------------------")

    # Opção 1: Cadastrar alunos
    if Decisao == 1:
        Nomes, Notas, Faltas, Medias, situacoes = cadastro(Nomes, Notas, Faltas, Medias, situacoes)

    # Opção 2: Ver relatório dos alunos
    elif Decisao == 2:
        if len(Nomes) > 0:  # Verifica se já existem alunos cadastrados
            relatorio(Nomes, Notas, Faltas, Medias, situacoes)
        else:
            print("Nenhum aluno cadastrado. Primeiro, cadastre os alunos.")
        
    # Opção 0: Sair do menu
    elif Decisao == 0:
        print("Tudo bem, o programa vai ser encerrado agora.")
        
    # Opção inválida
    else:
        print("Número inválido, os números de operações disponíveis são: 1, 2 ou 0.")
    print("----------------------------------------------------------------------------------------------------------")