#função garantindo que não há numero no nome
def Nome_valido():
    while True:
        nome = input("\nEscreva o nome do aluno: ")
        if nome.isalpha():
            return (nome)
        else:
            print("\nO nome não pode conter numeros! tente novamente")

#função garantindo que a nota inserida é valida
def Nt_valida(texto):
    while True:
        try:
            valor = float(input(texto))
            if valor >=0 and valor <=10:
                return (valor)
            else:
                print ("A nota não pode ser menor que 0 ou maior que 10! tente novamente.")
        except ValueError:
            print ("\nEssa não é uma nota valida! tente novamente.")

#função garantindo que quantidade de faltas é valida
def Faltas_validas():
    while True:
        try:
            qtd_faltas = int(input("\nEscreva a quantidade de faltas: "))
            return qtd_faltas
        except ValueError:
            print("\nErro! A quantidade de faltas deve ser um número inteiro. Tente novamente!")

# Array que vai guardar todos os alunos
alunos = []

# Função para cadastrar alunos
def cadastro():
    cont = 1  # Contador para o número de alunos

    # Array que vai guardar todos os alunos
    alunos = []

    while True:
        try:
            Qtd_alunos = int(input("\nEscreva a quantidade de alunos que deseja cadastrar: ")) 
            print ("----------------------------------------------------------------------------------------------------------")
            break
        except ValueError:
            print ("A quantidade de alunos deve ser um numero! tente novamente.")

    # Inicia o cadastro de alunos
    while cont <= Qtd_alunos:                                                           
        print (f"\n\nDados do {cont}° aluno") 

        # Array para guardar os dados de cada aluno
        aluno = []

        # Recebe os dados do aluno
        Nome = Nome_valido()
        Nt1 = Nt_valida("\nEscreva a primeira nota do aluno: ")                      
        Nt2 = Nt_valida("Escreva a segunda nota do aluno: ")                         
        Nt3 = Nt_valida("Escreva a terceira nota do aluno: ")                        
        Nt4 = Nt_valida("Escreva a quarta nota do aluno: ")                          
        QtdFaltas = Faltas_validas()

        # Calcula a média
        Media = (Nt1 + Nt2 + Nt3 + Nt4) / 4

        # Chama a função que lida com a situação do aluno atraves de condições.
        situacao = condicao(Media,QtdFaltas)                                                                        

        # Arredonda a média
        Media = round(Media, 2)                                                            

        # Armazena os dados do aluno no array Aluno
        aluno.append(Nome)
        aluno.extend([Nt1,Nt2,Nt3,Nt4])
        aluno.append(QtdFaltas)
        aluno.append(Media)
        aluno.append(situacao)

        # Armazena os dados dos alunos no array Alunos
        alunos.append(aluno)

        cont += 1  # Incrementa o contador de alunos

    return alunos

def condicao (Media,QtdFaltas):
    # Define a situação do aluno com base nas notas
        if QtdFaltas > 30:                                                              
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
        return situacao     

# Função para exibir o relatório dos alunos
def relatorio(alunos):
    for aluno in alunos:
        print (f"\nNome: {aluno[0]}")
        print (f"Notas: {', '.join(map(str, aluno[1:5]))}")
        print (f"Faltas: {aluno[5]}")
        print (f"Media: {aluno[6]}")
        print (f"Situação: {aluno[7]}")

# Loops de interação com o usuário
Decisao = int

while Decisao != 0:
    print("----------------------------------------------------------------------------------------------------------")
    print("\nO que deseja fazer?\n\nCadastrar alunos = 1\nVer o relatório dos alunos = 2\nSair do Menu = 0")
    try:
        Decisao = int(input("\nEscreva o número relacionado à ação que quer fazer (1, 2 ou 0): "))
    except ValueError: # Tratamento de erro 
            print("\nVocê deve fazer uma escolha valida! tente novamente.")
            continue

    # Opção 1: Cadastrar alunos
    if Decisao == 1:
        alunos.extend(cadastro())

    # Opção 2: Ver relatório dos alunos
    elif Decisao == 2:
        if len(alunos) > 0:  # Verifica se já existem alunos cadastrados
            relatorio(alunos)
        else:
            print("Nenhum aluno cadastrado. Primeiro, cadastre os alunos.")
        
    # Opção 0: Sair do menu
    elif Decisao == 0:
        print("Tudo bem, o programa vai ser encerrado agora.")
        
    # Opção inválida
    else:
        print("Número inválido, os números de operações disponíveis são: 1, 2 ou 0.")