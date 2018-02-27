def somar(x,y):
    return x+y
    
def main():
    print 'Soma: ' + str(somar(2,5))
    print '-----------------------'
    
#main()
    
def dicionario():
    dictVazio = {}
    dictNaoVazio = {'Ida': 'Teste', 'Idb': 23, 'Sobre': 'legal'}
    
    for campo in dictNaoVazio:
        print dictNaoVazio[campo]

#dicionario()

