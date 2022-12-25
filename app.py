## PLAYGROUND EM PYTHON PARA TESTAR CÓDIGOS

# HELLO WORLD

#print('Hello World')

# FUNÇÃO

#def fun ():
#    print("Função")
#fun()

# CALCULADORA

def calculadora():
    num1 = int(input('Digite o primeiro numero: '))
    op = input("Digite a operação(+ , - , *, /): ")
    num2 = int(input('Digite o segundo numero: '))
    
    if op == '+':
        res = num1 + num2
        print("O resultado é ",res)

    elif op == '-':
        res = num1 - num2
        print("O resultado é ",res)

    elif op == '*':
        res = num1 * num2
        print("O resultado é ",res)

    elif op == '/':
        res = num1 / num2
        restoDiv = num1 % num2
        print("O resultado é ",res, "E o resto da divisão é:", restoDiv)

    else :
        print("Você digitou algo errado")

calculadora()