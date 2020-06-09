'''
#Lista 5
1) Crie um vetor com 40 elementos igualmente espaçados entre
0 e 2π.

import numpy as np
a = np.linspace(0,(2*np.pi),40)
print(a)
'''

'''
2) Escreva uma expressão que possa selecionar apenas os
elementos de índice par em um vetor, independente do
tamanho do vetor. Teste essa expressão em alguns vetores da
sua escolha.

import numpy as np
a = np.linspace(0,(2*np.pi),40)
b = np.linspace(0,2,8)

print(a)
print(a[::2])
print(b)
print(b[::2])
'''


'''
3) Crie uma matriz 4 x 3 de números aleatórios inteiros no
intervalo -5 a 5 e armazene em uma variável “mat”.
a) Escreva um comando que retorna o valor absoluto dos
elementos dessa matriz.

import numpy as np
mat = 10*np.random.rand(4,3)-5
print(mat)

b) Escreva um comando que retorna o seno dos valores
contidos na primeira linha dessa matriz.

import numpy as np
mat = 10*np.random.rand(4,3)-5
seno = np.sin(mat[0])
print(seno)

c) Escreva um comando que retorne o valor máximo das
colunas da matriz

import numpy as np
mat = 10*np.random.rand(4,3)-5
max = np.max(mat[0:4,0])
max1 = np.max(mat[0:4,1])
max2 = np.max(mat[0:4,2])
print(mat)
print(max)
print(max1)
print(max2)

d) Calcule a soma dos elementos em cada coluna da matriz

import numpy as np
mat = 10*np.random.rand(4,3)-5
s0 = np.sum(mat[0:4,0])
s1 = np.sum(mat[0:4,1])
s2 = np.sum(mat[0:4,2])
print(mat)
print(s0)
print(s1)
print(s2)

e) Calcule a soma dos elementos em cada linha da matriz

import numpy as np
mat = 10*np.random.rand(4,3)-5
s0 = np.sum(mat[0,0:3])
s1 = np.sum(mat[1,0:3])
s2 = np.sum(mat[2,0:3])
s3 = np.sum(mat[3,0:3])
print(mat)
print(s0)
print(s1)
print(s2)
print(s3)

f) Calcule o produto entre os elementos de cada coluna da
matriz. Dica: procure no google como resolver isso
import numpy as np
mult0 = 1
mult1 = 1
mult2 = 1
mat = 10*np.random.rand(4,3)-5
s0 = np.absolute(mat[0:4,0])
s1 = np.absolute(mat[0:4,1])
s2 = np.absolute(mat[0:4,2])

for l in range(0,4):
    mult0 *= s0[l]
    mult1 *= s1[l]
    mult2 *= s2[l]

print(mat)
print(s0)
print(s1)
print(s2)
print(mult0)
print(mult1)
print(mult2)

'''

'''
4) Crie uma rotina na qual calcula o valor do cos a partir da série
de Taylor ( 50 primeiros termos) e seno a partir da seguinte
identidade. OBS: essa função não pode conter funções de loop
tal como: for while. Dica procure no google qual a função em
numpy/python que calcula o fatorial.


import numpy as np
from scipy.special import factorial
x = 2
exp = np.arange(2,100,2)
a = x**exp
b = factorial(exp)
termos = a/b
termos[::2] = -1*termos[::2] #do início até o fial pulando de 2 em dois e mult. por -1
cosvalue = termos.sum()+1
seno = np.sqrt(1-cosvalue**2)
print(seno)
print(cosvalue)

'''




