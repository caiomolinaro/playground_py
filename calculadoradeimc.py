print('Seja bem vindo a calculadora de IMC')

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc =  (peso / (altura**2))

if imc < 18.5 :
    print(nome, "seu imc é", imc, "e você se encaixa na classificação de: MAGREZA")

elif imc >= 18.5 and imc <= 24.9 :
    print(nome, "seu imc é", imc, "e você se encaixa na classificação: NORMAL")

elif imc >= 25.0 and imc <= 29.9 :
    print(nome, "seu imc é", imc, "e você se encaixa na classificação de: SOBREPESO e Obesidade grau I")

elif imc >= 30.0 and imc <= 39.9 :
    print(nome, "seu imc é", imc, "e você se encaixa na classificação de: OBESIDADE e Obesidade grau II")

elif imc > 40 :
    print(nome, "seu imc é", imc, "e você se encaixa na classificação de: OBESIDADE GRAVE e Obesidade grau II")

else :
    print("Valores errados digitados")