'''
#Lista 3
1)  Escreva um programa que pergunte a velocidade do carro
de um usuário. Caso ultrapasse 80 km/h, exiba uma
mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando 5 reais por Km
acima de 80Km/h.

v = float(input('Qual a sua velocidade? '))
p = (v-80)*5.0
if v>80:
    print('Vc foi multado, no valor de {}'.format(p))
else:
    print('Vc não será multado!')
'''

'''
2) Escreva um programa que leia 3 números e que imprima
o maior e o menor


v1 = float(input('Qual a sua valor 1? '))
v2 = float(input('Qual a sua valor 2? '))
v3 = float(input('Qual a sua valor 3? '))

if v1>v2:
    if v1>v3:
        if v2>v3:
             print('V1 {} é o maior e v3 {} é o menor'.format(v1,v3))
        elif v3>v2:
            print('V1 {} é o maior e v2 {} é o menor'.format(v1, v2))

if v2>v1:
    if v2>v3:
        if v1>v3:
            print('V2 {} é o maior e v3 {} é o menor'.format(v2,v3))
        elif v3>v1:
            print('V2 {} é o maior e v1 {} é o menor'.format(v2, v1))


if v3>v1:
    if v3>v2:
        if v2>v1:
            print('V3 {} é o maior e v1 {} é o menor'.format(v3,v1))
        elif v1>v2:
            print('v3 {} é o maior e v2 {} é o menor'.format(v3, v2))


if v1 == v2:
    if v1>v3:
        print('V1 {} e v2 {} são os maiores e v3 {} é o menor'.format(v1,v2,v3))
    elif v1 == v2 == v3:
        print('Todos valores podem ser iguais')
    else :
        print('V3 {} é o maior e v1 {} e v2 {} são os menores'.format(v3,v1,v2))
elif v2 == v3:
    if v2 > v1:
        print('V2 {} e v {} são os maiores e v1 {} é o menor'.format(v2, v3, v1))
    elif v1 == v2 == v3:
        print('Todos valores podem ser iguais')
    else:
        print('V1 {} é o maior e v2 {} e v3 {} são os menores'.format(v1, v2, v3))
elif v1 == v3:
    if v1 > v2:
        print('V1 {} e v3 {} são os maiores e v2 {} é o menor'.format(v1, v3, v2))
    elif v1 == v2 == v3:
        print('Todos valores podem ser iguais')
    else:
        print('V2 {} é o maior e v1 {} e v3 {} são os menores'.format(v2, v1, v3))
'''


'''
3) Escreva um programa que pergunte a distância que um
passageiro deseja percorrer em km. Calcule o preço da
passagem cobrando 0,50 por Km rodado para viagens até
200Km e 0,45 para viagens mais longas.

d = float(input('Qual a distância que vc deseja percorrer? '))
p = 0
if d<=200:
    p = 0.5*d
    print(f'O preço da passagem será {p:.2f}')
else:
    p = 0.45*d
    print(f'O preço da passagem será {p:.2f}')

'''

'''
4) Desenvolva um programa que solicite o primeiro número
de uma PA e sua razão. O programa deve imprimir os 10
primeiros termos.

n = float(input('Qual o primeiro número da PA? '))
r = float(input('Qual a razão da PA? '))
t = 0

for i in range(0,10):
    t = n + (i*r)
    print('O termo {} da PA é {}'.format(i,t))


'''


'''
5) Escreva um programa que pergunte o deposito inicial e a
taxa de Juros de uma poupança. Exiba os valores mês a
mês para os 24 primeiros meses. No final deve imprimir o
total de ganho com juros no período.

n = float(input('Qual é o deposito inicial? '))
t = float(input('Qual é a taxa de juros? '))
d = n

s = 0

for i in range(1,25):
    d =  (d *(1+t))
    print('O mês {:>2} dará um lucro de {:.2f}'.format(i,d))

    s += d

print(f'O total ganho com juros é {s:.2f}')

'''

'''
6) Faça um programa que calcule a soma os números
impares e múltiplos de 3 que se encontram no intervalo
de 1 até 500

i = 1
d = 0
t = 0
o = 0
s = 0

for i in range(1,500):
    d = i % 2
    t = i % 3
    if d == 1 and t == 0:
        o = i
        s += o
        print('O número {} dará a soma de {}'.format(i,s))
    else:
        print('O número {} pode não ser ímpar ou multiplo de 3'.format(i))

    elif d == 1 and t == 1:
        print('O número {} é ímpar, mas não é múltiplo de 3'.format(i))
    elif d == 0 and t == 1:
        print('O número {} não é ímpar e não é múltiplo de 3'.format(i))
    else:
        print('O número {} não é ímpar e é multiplo de 3'.format(i))
'''



'''
7) Escreva um script que exibe a seguinte tábua de
multiplicação na tela:


for i in range(1,6):

    for j in range(i,i*i+1,i):
        print(str(j) +' ',end='')
    print('')

'''





