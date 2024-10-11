'''
Crie um algoritmo que, dado um número informado pelo usuário, imprima 
a tabuada dele de 1 a 10, de maneira que sejam impressos somente as 
multiplicações cujo resultado seja um número par.
'''

n = int(input("Digite um número: "))
contador = 1

while contador <= 10:
    result = contador * n
    if result%2 == 0:
        print(f'{contador} x {n} = {result} --> Par')
    else:
        print(f'{contador} x {n} = {result} --> Ímpar')
    contador += 1

# print(f'1 x {n} = {1*n}')
# print(f'2 x {n} = {2*n}')
# print(f'3 x {n} = {3*n}')
# print(f'4 x {n} = {4*n}')
# print(f'5 x {n} = {5*n}')


