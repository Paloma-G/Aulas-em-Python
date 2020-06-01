'''
v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu salário: '))
a = float(input('Digite em quantos anos vc pretende quitar casa: '))
m = a * 12
p = v/m
t = s*0.3
if p<=t:
    print(f'Pode realizar o empréstimo \nValor da prestação {p:.2f} e o valor da condição {t:.2f}')
else:
    print(f'Não pode fazer')


'''


'''
v = int(input('Digite um valor: '))
print('Digite a base escolhida para a conversão:[1] binário[2] octal[3] hexa')

base = int(input('A base escolhida é: '))

if base==1:
    print(f'O valor {v} em binário será {bin(v)}')
elif base==2:
    print(f'O valor {v} em binário será {oct(v)}')
elif base==3:
    print(f'O valor {v} em binário será {hex(v)}')
else:
    print(f'Opção inválida')
'''

'''
import random
print('Digite a sua escolha:[1] Pedra[2] Papel[3] Tesoura')
e = int(input('A sua escoha é: '))
c = random.randint(1,3)
print(f'A escolha do pc é {c}')
if e==1 and c==1:
    print('Jogue novamente')
elif e==2 and c==2:
    print('Jogue novamente')
elif e == 3 and c == 3:
     print('Jogue novamente')
elif e == 1 and c == 2:
    print('O pc ganhou')
elif e == 1 and c == 3:
    print('O jogador ganhou')
elif e == 2 and c == 1:
    print('O jogador ganhou')
elif e == 2 and c == 3:
    print('O pc ganhou')
elif e == 3 and c == 2:
    print('O jogador ganhou')
elif e == 3 and c == 1:
    print('O pc ganhou')
else:
    print('Opção inválida')

'''
'''
a = int(input('Por gentileza, insira um número para o calculo de tabuada: '))
for c in range(0, 11):
    n = a*c
    print(f'{a} x {c} = {n}')
'''

'''
s = 0
cont = 0
for i in range(1,7):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
         s = s + n # ou +=n
         cont = cont + 1 # ou += cont
print('vc informou {} números e a soma foi {}'.format(cont,s))

'''

'''
Palíndromo



'''


'''
frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.split()
junto = ''.join(p)
inverso = ''
inverso = junto[::-1]

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')

'''
