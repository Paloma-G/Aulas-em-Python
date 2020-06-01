'''
Desafio 005

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n1 = int(input('Digite um número '))
a = n1 - 1;
s = n1 + 1;
print('Seu sucessor é {} e o seu antecessor é {}'.format(s,a))

'''

'''
Desafio 006

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input("Digite um número: "))
d = n * 2;
t = n * 3;
r = n ** (1/2);
print('O seu dobro é {:.3f}, o seu triplo é {:.3f} e a sua raiz quadrada é {:.3f}'.format(d,t,r))

'''

'''
Desafio 007

Desenvolva um programa que leia as duas notas de um aluno, calcule  mostre a sua média

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = ((n2 + n1)/2);
print('Sua média é {:.2f}'.format(m))

'''

'''
Desafio 008

Escreva um progrma que leia um valor em metros e o exiba convertido em centimetros e milimetros

v = float(input('Digite um valor em metros: '))
c = v * 100;
m = v * 1000;
print('Seu valor em cm {:.0f}\n e o seu valor em mm é {:.0f}'.format(c,m))



'''

'''
Desafio 009

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

v = int(input('Digite um número: '))
print('A sua tabuada é \n')
r1 = v * 1; r10 = v * 10;
r2 = v * 2;r3 = v *2;r3 = v * 3;r4 = v * 4;r5 = v * 5;r6 = v * 6; r7 = v * 7;r8 = v * 8;r9 = v * 9;
print('{} * 1 = {}'.format(v,r1)) # poderia ter colocado entro do format (v,v*1)
print('{} * 2 = {}'.format(v,r2))
print('{} * 3 = {}'.format(v,r3))
print('{} * 4 = {}'.format(v,r4))
print('{} * 5 = {}'.format(v,r5))
print('{} * 6 = {}'.format(v,r6))
print('{} * 7 = {}'.format(v,r7))
print('{} * 8 = {}'.format(v,r8))
print('{} * 9 = {}'.format(v,r9))
print('{} * 10 = {}'.format(v,r10))
print('='*12)

ou

v = int(input('Digite um número: '))
print('A sua tabuada é \n')
print('='*12)
print('{} * {:2} = {}'.format(v,1,v*1)) # poderia ter colocado entro do format (v,v*1)
print('{} * {:2} = {}'.format(v,2,v*2))
print('{} * {:2} = {}'.format(v,3,v*3))
print('{} * {:2} = {}'.format(v,4,v*4))
print('{} * {:2} = {}'.format(v,5,v*5))
print('{} * {:2} = {}'.format(v,6,v*6))
print('{} * {:2} = {}'.format(v,7,v*7))
print('{} * {:2} = {}'.format(v,8,v*8))
print('{} * {:2} = {}'.format(v,9,v*9))
print('{} * {:2} = {}'.format(v,10,v*10))
print('='*12)
'''

'''
Deafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Dólar = 3.27 reais

r = float(input("Quantos reais vc tem? "))
d = r / 3.27;
print('Vc pode comprar {:.2f} dólares'.format(d))
'''

'''
Desafio 011
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta para pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m**2

l = float(input('Quanto é a largura da parede: '))
al = float(input('Quanto é a altura da parede: '))

a = l * al;
t = a / 2;
print('Vc precisa de {} litros de tinta'.format(t))
'''

'''
Desafio 012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço: '))
np = (p -(p*0.05));
print('O novo preço é {}'.format(np))

'''
'''
Desafio 013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

p = float(input('Digite o salário: '))
np = (p +(p*0.15));
print('O novo salário é {}'.format(np))

'''
