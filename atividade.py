#arrays guardando as informações do usuario
Nomes = []                                                                                  
Notas = []                                                                                  
Faltas = []                                                                                 
Medias = []
situacoes = []

#Contadores exercendo diferentes funções
contgeral = 0
contAR = 0
cont = 1   

#Declarando a variavel de decisão
Decisao = int                                                                                    

#Inicio do input do usuario sobre qual decisão ele quer tomar
print ("----------------------------------------------------------------------------------------------------------")
while Decisao != 0:
    print ("\nO que deseja fazer?\n\nCadastrar alunos = 1\nVer o relatorio dos alunos = 2\nSair do Menu = 0")
    Decisao = int(input("\nEscreva o numero relacionado a ação que queria fazer(1, 2 ou 0): "))
    print ("----------------------------------------------------------------------------------------------------------")

    #Caso ele escolha a opção 1 entra na parte de cadastro de alunos
    if Decisao == 1:
        #Recebe quantidade de alunos, servindo como limite do while abaixo
        Qtd_alunos = int(input("\nEscreva a quantidade de alunos que deseja cadastrar: ")) 
        print ("----------------------------------------------------------------------------------------------------------")

        #while dando inicio ao processo de cadastro de cada aluno
        while cont <= Qtd_alunos:                                                           
            print (f"\n\nDados do {cont}° aluno")                                          

            #guardando os valores fornecidos pelo usuario
            Nome = input("\nEscreva o nome do aluno: ")                                     
            Nt1 = float(input("\nEscreva a primeira nota do aluno: "))                      
            Nt2 = float(input("Escreva a segunda nota do aluno: "))                         
            Nt3 = float(input("Escreva a terceira nota do aluno: "))                        
            Nt4 = float(input("Escreva a quarta nota do aluno: "))                          
            QtdFaltas = int(input("\nEscreva a quantidade de faltas: "))                    
            
            #calculo da media
            Media = (Nt1+Nt2+Nt3+Nt4)/4                                                     

            #conjunto de condições para cada caso de aprovação, reprovação e caso ocorro um erro nos valores
            if Media >= 8:                                                                  
                situação = "aprovado"                                                       
            elif Media >= 5:                                                               
                ntRec = float(input("\nEscreva a nota de recuperação do aluno: "))          
                if ntRec < (10 - Media):                                                    
                    situação = "Reprovado"                                                  
                else:                                                                       
                    situação = "aprovado"                                                   
            else:                                                                           
                situação = "Reprovado"      

            #Caso as faltas sejam maior que 30 o aluno é reprovado imediatamente
            if QtdFaltas > 30:                                                              
                situação = "Reprovado" 

            #Caso os dados não batem, a situação é definido como alterada
            if Media > 10 or Media < 0:                                                     
                situação = "Dados invalidos"                                                
            
            #arredondando a media
            Media=round(Media,2)                                                            

            #Cada array recebe um valor, facilitando o guardar de dados e principalmente a impressão na tela
            Nomes.append (f"Nome: {Nome}")
            Notas.append (f"Notas: {Nt1}, {Nt2}, {Nt3}, {Nt4}")
            Faltas.append (f"faltas: {QtdFaltas}")
            Medias.append (f"Media: {Media}")
            situacoes.append (f"situação: {situação}")

            cont += 1                                               #incremento do array do cadastro
            contgeral +=1                                           #incremento do contador dos arrays
            print ("--------------------------------------------------------------------------------------------------")

    #Caso o usuario escolha a segunda opção, é mostrado o relatorio de todos os alunos cadastrados
    elif Decisao == 2:
        #While utiliza um contando da operação e compara com o limite de contador geral de todos os alunos cadastrados
        while contAR < contgeral:
            print (Nomes[contAR],"\n",Notas[contAR],"\n",Faltas[contAR],"\n",Medias[contAR],"\n",situacoes[contAR])
            print ("-----------------------------------------------")
            contAR += 1
    
    #Caso o usario escolha 0 a operação é encerrada
    elif Decisao == 0:
        print ("tudo bem, o programa vai ser encerrado agora.")
    
    #Caso o usuario escreva algum outro valor, a mensagem de erro aparece
    else:
        print ("numero invalido, os numeros de operações disponiveis são: 1,2 ou 0")   
    
    #O contador do cadastro de usuario é resetado
    cont = 0