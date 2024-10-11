'''
Escrever um algoritmo que leia uma quantidade desconhecida de números 
e conte quantos deles estão nos seguintes intervalos: 
    [0 à 25] 
    [26 à 50] 
    [51 à 75] 
    [76 à 100]
A entrada de dados deve terminar quando for lido um número negativo.
'''

numero = int(input("Digite um número: "))

while not numero < 0:
    if numero>=0 and numero <= 25:
        print('Intervalo [0 à 25]')
    elif numero >= 26 and numero <= 50:
        print('Intervalo [26 à 50]')
    elif numero >= 51 and numero <= 75:
        print('Intervalo [51 à 75]')
    elif numero >= 76 and numero <= 100:
        print('Intervalo [76 à 100]')
        
    numero = int(input("Digite um número: "))

