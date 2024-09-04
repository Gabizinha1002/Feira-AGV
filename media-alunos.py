# Dicionário para armazenar os alunos e suas respectivas notas
alunos = {}

# def, é uma função e dentro dela são as instruções
# aqui vc cria uma funcao para cadastrar os alunos
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    # if, significa "se", então se o aluno já está cadastrado
    if nome in alunos:
        print("Aluno já cadastrado.")
        return
    
    # pede as notas do aluno
    # float é para se as notas são decimais
    # input é para abir uma caixa de pergunta
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Armazena o aluno e suas notas no dicionário
    alunos[nome] = [nota1, nota2, nota3]
    print(f"Aluno {nome} cadastrado com sucesso!\n")

# Função para calcular a média de um aluno
def calcular_media(nome):
    notas = alunos[nome]
    return sum(notas) / len(notas)

# Função para verificar a situação do aluno
def verificar_situacao():
    nome = input("Digite o nome do aluno para verificar a situação: ")
    
    # Verifica se o aluno está cadastrado
    if nome not in alunos:
        print("Aluno não encontrado.")
        return
    
    # Calcula a média
    media = calcular_media(nome)
    print(f"A média de {nome} é: {media:.2f}")
    
    # Verifica a situação do aluno com base na média
    if media >= 7:
        print(f"O aluno {nome} foi aprovado!")
    elif media >= 5:
        print(f"O aluno {nome} está de recuperação.")
    else:
        print(f"O aluno {nome} foi reprovado.")

# Função principal
def menu():
    while True:
        print("\n---- Sistema de Gestão Escolar ----")
        print("1. Cadastrar Aluno")
        print("2. Verificar Situação do Aluno")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            verificar_situacao()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
menu()
