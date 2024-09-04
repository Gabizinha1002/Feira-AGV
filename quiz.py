class Quiz:
    def __init__(self):
        self.perguntas = []
        self.pontuacao = 0

    def adicionar_pergunta(self, pergunta, alternativas, resposta_correta):
        self.perguntas.append({
            'pergunta': pergunta,
            'alternativas': alternativas,
            'resposta_correta': resposta_correta
        })

    def fazer_quiz(self):
        for i, pergunta in enumerate(self.perguntas):
            print(f"\nPergunta {i + 1}: {pergunta['pergunta']}")
            for j, alternativa in enumerate(pergunta['alternativas']):
                print(f"{j + 1}. {alternativa}")
            
            try:
                resposta = int(input("Sua resposta (digite o número): "))
                if pergunta['alternativas'][resposta - 1] == pergunta['resposta_correta']:
                    print("Correto!")
                    self.pontuacao += 1
                else:
                    print(f"Incorreto! A resposta certa é: {pergunta['resposta_correta']}")
            except (ValueError, IndexError):
                print("Entrada inválida. Resposta desconsiderada.")
    
    def mostrar_pontuacao_final(self):
        print(f"\nQuiz finalizado! Sua pontuação foi {self.pontuacao} de {len(self.perguntas)} perguntas.")

def executar_quiz():
    quiz = Quiz()
    
    # Adicionando perguntas ao quiz
    quiz.adicionar_pergunta(
        "Sobre o que o nosso grupo apresentou?", 
        ["Front-end", "Cien. da Computação", "Banco de Dados", "Mobile", "Python"], 
        "Python"
    )
    quiz.adicionar_pergunta(
        "Sobre que programa nós falamos?", 
        ["Adivinhar", "IMC", "Chatbot", "tarefas","biblioteca"], 
        "IMC"
    )
    quiz.adicionar_pergunta(
        "Qual é a serie do nosso grupo?", 
        ["1°DS", "2°DS", "3°DS", "BioTecnologia", "Regular"], 
        "2°DS"
    )
    
    # Executar o quiz
    quiz.fazer_quiz()
    
    # Mostrar pontuação final
    quiz.mostrar_pontuacao_final()

# Executar o quiz
executar_quiz()
