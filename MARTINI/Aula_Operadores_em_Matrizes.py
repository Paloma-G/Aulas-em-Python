'''
#matrizes de mesma dimensão
import numpy as np
a = np.array([[4,5,6],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a+b
d = a-b
e = a*b # mult. elemento por elemento
f = a/b
g = a//b
h = a**b

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
'''

'''
#Operação com escalar
import numpy as np
a = np.array([[4,5,6],[8,2,3]])
b = 3+a
d = 3-a
e = a*3 # mult. elemento por elemento
f = a/3
g = a//3
h = a**3

print(a)
print(b)
print(d)
print(e)
print(f)
print(g)
print(h)
'''

'''
#Multiplicação de matrizes - Álgebra Linear
import numpy as np
a = np.array([[4,6],[8,2]])
b = np.array([[5,3],[9,4]])
c = np.dot(a,b)

print(a)
print(b)
print(c)
'''

'''
#Matriz inversa
import numpy as np
a = np.array([[4,6],[8,2]])
b = np.linalg.inv(a)
print(a)
print(b)

'''

'''
#Determinante de uma matriz
import numpy as np
a = np.array([[4,6],[8,2]])
b = np.linalg.det(a)
print(a)
print(b)

'''

'''
#Matriz transposta
import numpy as np
a = np.array([[4,6],[8,2]])
b = a.transpose()
# ou B = a.T
print(a)
print(b)

'''

'''
#Extraindo informações das matrizes
import numpy as np
a = np.array([[2,5,3],[8,6,9]])

print(a.min()) #valor mínimo da matriz
print(a.min(0)) #valor mínimo  dos elementos do eixo 1=linha (cada)
print(a.min(1)) #valor mínímo dos elementos do eixo 0=coluna (cada)

print(a.max()) #valor máximo da matriz
print(a.max(0)) #valor máximo dos elementos do eixo 1=linha (cada)
print(a.max(1)) #valor minímo dos elementos do eixo 0=coluna (cada)

print(a.sum()) #soma da matriz
print(a.sum(0)) #soma dos elementos do eixo 1=linha (cada)
print(a.sum(1)) #soma dos elementos do eixo 0=coluna (cada)

print(a.cumsum()) #soma acumulativa

print(a.mean()) #média da matriz
print(a.mean(0)) #média dos elementos do eixo 1=linha (cada)
print(a.mean(1)) #média dos elementos do eixo 0=coluna (cada)

print(a.std()) #desvio padrão da matriz
print(a.std(0)) #desvio padrão dos elementos do eixo 1=linha (cada)
print(a.std(1)) #desvio padrão dos elementos do eixo 0=coluna (cada)

'''

'''
#Funções Matemáticas

import numpy as np
angle = np.linspace(0,2*np.pi,3) #em radianos
sinvalue = np.sin(angle)
print(angle)
print(sinvalue)
'''


'''
#Principais funções:
np.absolute(x): retorna o valor absoluto
np.exp2(x): retorna o valor 2^x
np.log(x): retorna o log de e
np.log10(x): retorna o log na base 10
np.log2(x): retorna o log na base 2
np.angle(x): retorna o ângulo da parte complexa
np.real(x): retorna a parte real de um número complexo
np.imag(x): retorna a parte imaginária de um número complexo
np.conj(x): retorna o valor conjulgado
np.sqrt(x): retorna a raiz quadrada
np.cbrt(x): retorna a raiz cúbica
np.around(x): retorna o arredondamento
np.floor(x): retorna o valor inteiro inferior
np.ceil(x): retorna o valor inteiro superior
np.trunc(x): retorna o valor inteiro truncado



'''
