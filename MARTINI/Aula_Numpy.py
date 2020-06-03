'''
Teoria

O Numpy é uma biblioteca para a linguagem de programação
Python que diciona suporte para cálculo matricial de forma
efiiente. Possui suporte para matrizes multidimensionais,
além de com uma grande coleção de funções matemáticas de
alto nível para operar nessas matrizes.

Vantagens do uso da biblioteca numpy:
- Um poderoso objeto de matriz N-dimensional;
- Funções sofisticadas (transmissão);
- Ferramentas para integrar código C/C++ e Fortran;
- Rescursos úteis de álgebra linear, transformação de Fourier e
úmeros aleatórios.

ndarray: é uma matriz n-dimensional e todos os elementos são do mesmo tipo

ex.
import numpy as np
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(3 * matrix)

Modo de acesso:
M[L,C]
M[0:2,0] : pega da linha 0 a linha 1 e a coluna 0.

Extraindo informações:
m.ndim: o número de dimensões da matriz
m.shape: formato da matriz (l,c)
m.size: retorna a quantidade de elementos na matriz
m.dtype: retorna o tipo dos elementos a matriz



'''


'''
import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
n = np.array([[1,2.1,3],[4,5,6],[7,8,9]])
a = m[1,1]
b = m[1,1:3]
c = m[1,:]
d = m[0:2,:]
e = m.ndim
f = m.size
g = m.shape
h = m.dtype
i = n.dtype

print(m) #mostra a matriz inteira
print(a) #mostra o elemento nesta posição
print(b) #mostra os elementos dessa posição
print(c) #mostra os elementos dessa posição
print(d)
print(e,f,g,h,i)


'''

'''
import numpy as np
m = np.arange(0,9)
m_zeros = np.zeros_like(m)
m_ones = np.ones_like(m)
a = np.linspace(0,10,20)
b = np.random.randint(0,10,(2,3)) #valores aleatórios entre 0 e 9, em uma matriz 2x3
# matriz de números aleatórios entre 0 e 3
c = 3*np.random.rand(2,3)
# matriz de números aleatórios entre -5 e 5
d = 10*np.random.rand(2,3)-5

print(m ,m_zeros,m_ones,a,b)

print(c)

print(d)
'''

'''
import numpy as np
m = np.ones((3,3))
n = np.ones((3,3),dtype=np.int8) #define
a = n.itemsize
b = np.ones((3,3),dtype=np.int64)
c = b.itemsize
d = b.astype('int8')
e = d.itemsize

print(m)
print(n)
print(a)
print(b)
print(c)
print(d)
print(e)
'''
