'''
1) Faça um programa que leia o nome e nota da P1 de vários
alunos guardando tudo em uma lista e no final mostre:
a. Quantas alunos foram cadastradas
b. O nome do aluno com maior nota
c. O nome da pessoa menor nota
d. O nota média da sala.

lista = []
dados = []
mai = 0
men = 10
s = 0
while True:

    dados.append(str(input('Qual é seu nome? ')))
    dados.append(float(input('Qual foi sua nota da p1: ')))
    if len(dados) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar: [S/N] '))

    if resp in 'Nn':
        break

print(f'Você cadastrou {len(lista)} pessoas')

for p in lista:
    if p[1] == mai:
        print(f'{p[0]} tem a maior nota que é {mai}')

for p in lista:
    if p[1] == men:
        print(f'{p[0]} tem a menor nota que é {men}')

for p in lista:
    s = p[1] + s

m = s / (len(lista))

print(f'A média da sala é {m:.2f} ')
'''






'''
2) Crie um programa onde o usuário possa digitar 10 valores
numéricos e cadastre-os em 2 listas separadas. Sendo a
primeira contendo números primos e segunda não
primos.

primos = list()
nprimos = list()

for i in range(0,10):
    n = int(input('Qual o valor: '))
    # determinando se é numero primo
    p = True

    for k in range(2,n):
         if (n % k == 0):
             nprimos.append(n)
             p = False
             break
    if (p):
        primos.append(n)


print(primos)
print(nprimos)
'''



'''
3) Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = float(input(f'Qual é o valor para [{l},{c}] '))


for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:.2f}', end=' ')
    print( )

'''

'''
4) Faça um programa que leia o nome RA e média final de
uma aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.

dici = dict()

dici['nome'] = str(input('Digite seu nome: '))
dici['RA'] = int(input('Digite seu RA: '))
dici['média'] = float(input('diite sua média final: '))

for k,v in dici.items():
    print(v, end=' ')
print( )
if dici['média'] >= 6:
    print(f'Aprovado!')
elif dici['média'] < 6 and dici['média'] >= 3:
    print(f'Exame!')
else:
    print(f'Reprovado!')
'''

'''
5) Crie um programa que leia nome, sexo, peso e altura de
várias pessoas. guarde os dados de cada pessoa num
dicionário individual e acrescente o IMC da pessoa.
Organize todos os dicionários em uma lista. No final
mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas


dicind = dict()
lista = list()
soma0 = 0
soma1 = 0
simc = 0

while True:
    dicind['nome'] = str(input('Qual é o seu nome? '))
    dicind['sexo'] = str(input('Qual é o seu sexo [F/M]? '))
    dicind['peso'] = float(input('Qual é o seu peso? '))
    soma0 = dicind['peso'] + soma0
    dicind['altura'] = float(input('Qual é o seu altura? '))
    soma1 = dicind['altura'] + soma1
    dicind['IMC'] = dicind['peso'] / (dicind['altura'] ** 2)
    simc += dicind['IMC']
    lista.append(dicind.copy())
    dicind.clear()
    res = str(input('Quer continuar: [S/N] '))
    if res in 'Nn':
        break


print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O peso médio das pessoas é {soma0/len(lista):.2f}')
print(f'O imc médio das pessoas é {simc/len(lista):.2f}')
print(f'A altura media é {soma1/len(lista):.2f}')
'''



