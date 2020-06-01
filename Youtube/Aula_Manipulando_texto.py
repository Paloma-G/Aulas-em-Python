frase = 'Curso em vídeo Python'
print(frase) #print da string inteira
print(frase[3]) #print da 4 letra da string inteira
print(frase[3:13]) #print da 4 a 13 string inteira (índice começa no 0)
print(frase[:13]) #print do início a letra 13 string inteira
print(frase[1::2]) #print da 2 letra a última, pulando dastring inteira

'''print("""
texto grande
""") '''

print(frase.count('o')) #print quantas vezes tem 'o' na # string inteira
print(frase.upper().count('o')) #muda a string inteira em formato maiusculo e conta o 'o' minusculo
print(frase.upper().count('O')) #muda a string inteira em formato maiusculo e conta o 'O' maiusulo
print(len(frase)) #quantidade de caracter que tem a string
print(len(frase.strip())) #quantidade de caracter sem espaço em excesso que tem a string
print(frase.replace('Python','Android')) #troca a 1 plavra pela 2
print('Curso' in frase) #varifica se curso está na string
# se aparecer -1 é falso
print(frase.lower().find('vídeo')) #muda pra minusculo e encontra'vídeo', mostra o 1 índice da palavra
print(frase.split()) #separa a string
d = frase.split()
print(d[0]) #mostra a 1 paavra da string
print(d[2]) #mostra a 3 paavra da string
print(d[2][3]) #mostra a letra 4 da 3 paavra da string