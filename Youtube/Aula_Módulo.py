'''
Bibliotecas -> módulos
from math import sqrt    #importa somete sqrt
from math import sqrt,ceil

'''


'''
import math # importa tudo
a = float(input('digite um número: '))
arcima = math.ceil(a)
arbaixo = math.floor(a)
trunca = math.trunc(a)
potencia = math.pow(a,6)
raiz = math.sqrt(a)
fatorial = math.factorial(a) # só pode ser utilizado para inteiros

print(f'O número {a} pode ser arredondado pra cima {arcima}, para baixo {arbaixo} \n')
print(f'Truncado dessa forma {trunca}, com potência 6 de {a} é {potencia:.3f}, raiz {raiz:.3f} e fatorial {fatorial:.3f}')

'''
'''
from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

'''
'''
import random
num = random.randint(1,10)
print(num)
'''

import emoji

print(emoji.emojize("Olá, mundo :earth_americas: ", use_aliases=True))