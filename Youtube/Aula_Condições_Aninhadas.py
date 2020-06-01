'''
Estruturas condicionais dentro de outras estruturas

if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.ré():
    bloco3
else:
    bloco4


ex.1
nome = str(input('Qual se nome?'))
if nome == 'Paloma':   # se não for esse nome ele não faz o print
    print('Que nome lindo vc tem!')
elif nome== 'Pedro' or nome== 'Maria':
    print('Seu nome é bem ppular!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')
print('Bom dia, {}!'.format(nome))
'''

