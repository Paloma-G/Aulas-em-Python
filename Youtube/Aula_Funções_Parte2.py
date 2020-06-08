'''
help(): ajuda iterativa - digite essa função no Python console.
        Depois digite as funções que você gostaria de saber mais sobre.
        Para sair, basta digitar 'quit'.
        Ou 
        digitar help(nome da função) no arquivo do código.
        
        
Docstrings: quando você fa um maual para a sua função.

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    """
    c=i
    while c<=f:
        print(f'{c} ',end='..')
        c+=p
    print('FIM!')



contador(2,10,2)
help(contador)
'''



'''
#Parâmetros Opcionais

def somar(a=0,b=0,c=0): #se não tiver número para o c, ele assume o valor de zero.
    s = a+b+c
    print(a,b,c)
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar(c=2,b=9)
somar()
'''

'''
#Escopo de Variáveis

#local onde a variável vai existir ou não vai mais existir.

def teste(b): #parâmetro formal
#Escopo Local
    #Aqui eu poderia add uma variável 'a' com outro valor, mas ela só servirá para o escopo local.
    # 'global a' com esse comando, eu posso add uma variável a local e ela passará a ser global.
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')


#Escopo global
a = 2
teste(a) #parâmetro real
print(f'A fora vale {a}')
#print(f'B fora vale {b}') os dois comandos dão erro por falta de escopo
#print(f'C fora vale {c}') ou seja, só valem para o escopo local

'''

'''
#Retorno de Valores

def somar(a=0,b=0,c=0):
    s=a+b+c
    return s


resp1 = somar(3,2,5)
resp2 = somar(1,7)
resp3 = somar(4)
print(f'Meus cálculos deram {resp1}, {resp2} e {resp3}.')

'''

'''
#Exemplo 1 da aula:

def fatorial(num=1):
    f =1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores de fatorial são {f1}, {f2} e {f3}.')
'''


'''
#Exemplo 2 da aula:

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))
if par(num):
    print(f'{num} É par!')
else:
    print(f'{num} Não é par')
'''
