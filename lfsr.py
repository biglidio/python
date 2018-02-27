#LFSR

#Usando o algoritmo
# E(k,m) = LFSR(k) xor m
# |k|<|m|

#                                 x0 x1 x2 x3 x4 x5 x6 x7 
#Encripte m="FA" com a chave k=F= 0  1  0  0  0  1  1  0

#g is a generator, cause there are 5 backs to the function
def g():
    i = 0
    while True:
        i = i + 1
        yield i
        
def lfsr(x):
    i=0
    while True:
        x.append(0)
        x[i+8] = x[i+7] ^ x[i+4] ^ x[i]
        yield x[i+8]
        i = i+1
        
l = lfsr([0,1,0,0,0,1,1,0])

print l.next()
print l.next()
print l.next()
print l.next()
print l.next()
print l.next()
print l.next()
print l.next()

# ger = g()

# print ger.next()
# print ger.next()
# print ger.next()
# print ger.next()