'''
EStrutura condicional: só funiona um dos blocos

if carro.esquera():
    bloco True
else:
    bloco False

ex.
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
        print('Carro novo')
else:
        print('Carro velho')
print('--FIM--')

ou
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')

ex2.
nome = str(input('Qual se nome?'))
if nome == 'Paloma':   # se não for esse nome ele não faz o print
    print('Que nome lindo vc tem!')
print('Bom dia, {}!'.format(nome))


ex.3
n1 = float(input('Qual a sua nota 1?'))
n2 = float(input('Qual a sua nota 1?'))
m = (n1+n2)/2
print('A sua média foi {:.2f}!'.format(m))
if m>=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Precisa estudar mais!')
print('Parabéns!' if m>=6 else 'Estude mais!')
'''


