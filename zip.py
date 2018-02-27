def exemplo():
    pal1 = 'FATEC'
    pal2 = ['FACULDADE', 'ACADEMICA', 'TECNOLOGIA', 'ENTRETENIMENTO', 'CURSO']
    result = zip(pal1, pal2)
    
    # for i in result:
    #     print i
    
    # for (x,y) in result:
    #     print x + y
    
    d = {}
    for (x,y) in result:
        d[x] = y;
        
    print d
# exemplo()

# CONTANDO A FREQUENCIA DAS VOGAIS USANDO UM DICIONARIO

def freq(word):
    d = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    
    for letra in word:
        if letra in 'AEIOU':
            d[letra] += 1
    
    print d
    
# freq('OUVIRAM DO IPIRANGA AS MARGENS PLACIDAS')

# Verificar a maior letra dentro de cada posicao de duas palavras

def maiores(word1, word2):
    z = zip(word1, word2)
    aux = ""
    
    for (x, y) in z:
        aux += x if (ord(x) > ord(y)) else y
        
    print aux
# maiores('FATEC', 'LUCAS')

