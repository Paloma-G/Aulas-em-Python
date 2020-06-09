'''
1) Escreva uma função chamada fatorial para calcular o fatorial
de um número inteiro.

def fatorial(n):
    from scipy.special import factorial
    resp = factorial(n)
    print(resp)


n = int(input('Digite um número inteiro: '))
fatorial(n)

'''

'''
2) Escreva uma função chamada maxnum que retorne o maior
número de um conjunto de números. Utilize
empacotamento para fazer a função.

def maxnum(* n):
    import numpy as np
    resp = np.max(n)
    print(f'O maxnum é {resp}')


maxnum(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
'''

'''
3) Escreva uma função que receba dois números e retorne True
se o primeiro número for múltiplo do segundo.

def mult(a,b):
    if a>b:
        if a%b==0:
            print(f'O valor {a} é múltiplo de {b}')
        else:
            print(f'O valor {a} não é múltiplo de {b}')
    elif a<b:
        if b%a==0:
            print(f'O valor {b} é múltiplo de {a}')
        else:
            print(f'O valor {b} não é múltiplo de {a}')
    else:
        print(f'Os valores {b} e {a} são iguais e portanto múltiplos entre si.')


a = int(input('digite um número inteiro: '))
b = int(input('digite um número inteiro: '))
mult(a,b)
'''

'''
4) Escreva uma função chamada área_quad que recebe os
lados de um retângulo e retorne sua área.

def área_quad(l, a):
    resp = 1
    resp = l * a
    print(f'O valor da área é {resp}')


l = float(input('digite o valor da largura do retângulo: '))
a = float(input('digite o valor da altura do retângulo: '))
área_quad(l, a)
'''

'''
5) Escreva uma função chamada área_triang que receba a
base e a altura de um triangulo e retorne sua aréa.

def área_triang(b, a):
    resp = 1
    resp = (b * a)/2
    print(f'O valor da área é {resp}')


b = float(input('digite o valor da base do triângulo: '))
a = float(input('digite o valor da altura do triângulo: '))
área_triang(b, a)
'''


'''
6) Crie uma função na qual calcula o valor do cos a partir da série
de Taylor (50 primeiros termos) e seno a partir da seguinte
identidade. Obs: Fazer a serie utilizando for e utilizar a função
fatorial desenvolvida no exercício 1.

def fatorial(n):
    from scipy.special import factorial
    f = factorial(n)
    return f


import numpy as np
x = 2
n = np.arange(2,50,2)
a = x**n
b = fatorial(n)
termos = a/b
for i in range(0,50,2):
    termos = -1*termos #do início até o fial pulando de 2 em dois e mult. por -1
    cosvalue = np.sum(termos)+1

seno = np.sqrt((cosvalue**2)-1)


print(seno)
print(cosvalue)
'''


'''
7) Crie um vetor x com 60 pontos linearmente espaçados entre
-2π e 2π e construa o gráfico a baixo. Utilize as bibliotecas
numpy e matplotlib

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi,2*np.pi,(60))
s = np.sin(x)
c = np.cos(x)
tang = np.tan(x)

plt.subplot(2,2,1)
plt.plot(x,s,'r')
plt.title('Função seno(x)') #Add título ao gráfico
plt.xlim((-6,6)) #limita a vizualização do gráfico
plt.ylim((-1,1)) #limita a vizualização do gráfico

plt.subplot(2,2,2)
plt.bar(x,c)
plt.title('Função cos(x)') #Add título ao gráfico
plt.xlim((-6,6)) #limita a vizualização do gráfico
plt.ylim((-1,1)) #limita a vizualização do gráfico

plt.subplot(2,2,3)
plt.scatter(x,tang)
plt.title('Função tg(x)') #Add título ao gráfico
plt.xlim((-6,6)) #limita a vizualização do gráfico
plt.ylim((-40,40)) #limita a vizualização do gráfico
plt.show()

'''


