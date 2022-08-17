import random

lista = []

contador = 0
while contador < 50:
    x = random.randrange(1,50)
    lista.append(x)
    contador += 1

numeroDesejado = random.randrange(1,50)

print("o numero desejado é " + str(numeroDesejado))

ocorrencias = 0

for i in lista:
    if (i == numeroDesejado):
        ocorrencias += 1

print("o numero de ocorrencias é " + str(ocorrencias))

probabilidade = (ocorrencias / len(lista)) * 100

print(len(lista))

print("a probabilidade de sair o numero sorteado é de " + str(probabilidade) + "%")
