# cria uma funcao para calcular o imc
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
#cria uma funcao para classificar o imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
#cria um funcao para pedir os dados da pessoa
#float é para numeros decimais
#input é para criar uma caixa de entrada
def executar_calculadora_imc():
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
        #calcula o imc        
        imc = calcular_imc(peso, altura)
        
        #mostra a classificacao final
        classificacao = classificar_imc(imc)
        
        #mostra o resultado
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    
# Executar a calculadora de IMC
executar_calculadora_imc()
