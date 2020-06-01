'''
from random import randint
p = randint(0,5)
print(p)
v = int(input('Qual foi o valor pensado? '))
if v == p:
    print(f'True')
else:
    print(f'False')

'''


'''
v = int(input('Digite um número? '))
p = v%2

if p == 0:
    print(f'{v} é par')
else:
    print(f'{v} é ímpar')

'''


'''a = int(input('Digite o lado a do triângulo? '))
b = int(input('Digite o lado a do triângulo? '))
c = int(input('Digite o lado a do triângulo? '))


if a+b>c:
    if b+c>a:
        if a+c>b:
             print(f'Pode formar um triângulo')
        else:
            print(f'Não pode formar um triângulo')
    else:
        print(f'Não pode formar um triângulo')
else:
    print(f'Não pode formar um triângulo')'''


