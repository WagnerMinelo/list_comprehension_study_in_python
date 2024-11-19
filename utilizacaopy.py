# list comprehension

def divisao1(x, y):
    return x / y

def multiplicacao1(x, y):
    return x * y

def potenciacao(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
multiplicacao = [multiplicacao1(numero, 2) for numero in numeros]
quadrado = [potenciacao(numero, 2) for numero in numeros]
divisao = [divisao1(numero, 2) for numero in numeros]


print(multiplicacao)
print(quadrado)
print(numeros)
print(divisao)
