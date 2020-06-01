'''
for c in range(1,10):
    passo
pega


for c in range(0,3):
    passo
    pula
passo
pega


for c in range(0,3):
    se moeda:
        pega
    passo
    pula
passo
pega
'''
'''
for c in range(0,6): # faz 6 vezes
    print('Oi')
    print(c) # c é a variável contador
print('FIM')

for c in range(6,0,-1): # faz 6 vezes
    print('Oi')
print('FIM')

for c in range(0,6,2): # faz 6 vezes
    print('Oi')
    print(c) # c é a variável contador
print('FIM')



n = int(input('Início '))
f = int(input('Fim '))
p = int(input('Passo '))
for c in range(n,f+1,p):
    print(c)
print('FIM')


s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n # somatório de todos os valores
print('O somatório de todos os valores foi {}'.format(s))
print('Fim')

'''


n = int(input("Digite um numero "))
d = 0
for i in range(1, n):
    if n % i == 0:
        d = d + 1
        if d > 1:
          break
if d > 1:
  print("não é primo")
else:
  print("é primo")



