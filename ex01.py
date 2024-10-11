'''
Escrever um algoritmo que lê 5 valores, um de cada vez, e conta 
quantos destes valores são negativos, escrevendo esta informação.
'''

contador = 1
contadorNegativo = 0

while contador <= 5:
    valor = int(input("Digite um número: "))
    contador += 1
    if valor < 0:
        contadorNegativo += 1

print("O total de números negativos foi: ", contadorNegativo)






