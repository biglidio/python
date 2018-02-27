# Lista mutavel
lista = [5, "Ola", True, 2.3]
listaVazia = []

# Lista imutavel
tupla = (1, 2, 3, 4)
tuplaVazia = ()


# loop

for i in lista:
    print i
    
for i in tupla:
    print i
    
# exemplo de loop com filtro
texto = raw_input('Digite uma palavra: ')

for letra in texto:
    if letra in "AEIOUaeiou":
        print letra