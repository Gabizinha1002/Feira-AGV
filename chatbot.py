#define uma funcao que mostra as opcoes do que ele pode fazer
def exibir_menu():
    print("\n--- Chatbot Simples ---")
    print("1. Diga Olá")
    print("2. Perguntar o nome")
    print("3. Perguntar como estou")
    print("4. Despedir-se")
#cria uma funcao da resposta da pessoa
def responder_usuario(opcao):
    if opcao == "1":
        print("Chatbot: Olá! Como posso ajudar você hoje?")
    elif opcao == "2":
        nome = input("Chatbot: Qual é o seu nome? ")
        print(f"Chatbot: Prazer em conhecê-lo(a), {nome}!")
    elif opcao == "3":
        print("Chatbot: Você parece estar ótimo(a)!")
    elif opcao == "4":
        print("Chatbot: Até logo! Tenha um bom dia!")
    else:
        print("Chatbot: Desculpe, não entendi essa opção.")
#cria uma funcao para a pessoa responder
def executar_chatbot():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "4":
            responder_usuario(opcao)
            break
        responder_usuario(opcao)

# Executar o chatbot
executar_chatbot()
