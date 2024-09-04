#inclui um pacote no codigo
import random

#cria uma funcao para adivinhar o numero
def adivinhar_numero():
    #aparece na tela
    print("Pense em um número entre 1 e 100.")
    #abre uma caixa para responder
    input("Pressione Enter quando estiver pronto...")

    #define cada um
    menor = 1
    maior = 100
    tentativas = 0

    while True:
        #adiciona uma tentativa
        tentativas += 1
        #classifica se é maior, menor ou o numero escolhido
        palpite = random.randint(menor, maior)
        #mostra se esta certo ou nao
        print(f"O computador adivinha: {palpite}")
        #abre uma caixa para resposta
        resposta = input("O número é (maior, menor, correto)? ").lower()

        #se for "correto" o computador mostra em quantas tentativas e termina
        if resposta == "correto":
            print(f"O computador acertou em {tentativas} tentativas!")
            break
        #senao, se for maior, o computador fala que é um numero maior e adiciona 1 tentativa
        elif resposta == "maior":
        #senao, se for menor, o computador fala que é um numero menor e diminui 1 tentativa
            menor = palpite + 1
        elif resposta == "menor":
            maior = palpite - 1
        #se nao for nenhuma das alternativas vai aparecer resposta invalida    
        else:
            print("Resposta inválida. Por favor, responda com 'maior', 'menor' ou 'correto'.")

# Executar o programa
adivinhar_numero()
