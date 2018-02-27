def getKey():
    key={}
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    beta = 'PYDCLKHMZXREGVWAUFTSQNOJBI'
    z = zip(alfa, beta)
    for x,y in z:
        key[x] = y
    print key

# 1. E(k, "FATEC") = KPSLD
# 1. E(k, "PRAIA") = AFPZP
# 1. D(k, "XPNP") = JAVA
# 1. D(k, "ABSMWV") = PYTHON

def g():
    i = 0
    while True:
        i = i + 1
        yield i
        
def lfsr(x):
    i=0
    while True:
        x.append(0)
        x[i+5] = x[i] ^ x[i+1]
        yield x[i+4]
        i = i+1
        
# l = lfsr([0,0,0,1,1])

# print l.next()
# print l.next()
# print l.next()
# print l.next()
# print l.next()

# 2. (seed) x = C = 0011
# 2. REGRA N1 [ X(i+5) = X(i) xor x(i+1) ]
# 2. Gerado: 10010 = R, ou seja, CR
# 2. C xor M = 3 xor 13 = 00011 xor 01101 = 01110 = 14 = N
# 2. R xor P = 18 xor 16 = 10010 xor 10000 = 00010 = 2 = B
# 2. CS xor MP = "NB"

# VX MLNSLOZKR
# FATEC???????
# ????????????

#VX ML xor FATEC
# V xor F = 22 xor 6 = 10110 xor 00110 = 10000 = P
# X xor A = 24 xor 1 = 11000 xor 00001 = 11001 = Y
#   xor T = 0 xor 20 = 00000 xor 10100 = 10100 = T
# M xor E = 13 xor 5 = 01101 xor 00101 = 01000 = H
# L xor C = 12 xor 3 = 01100 xor 00011 = 01111 = O

# VX MLNSLOZKR
# FATEC???????
# PYTHON??????

# N xor N = 0 = " "

# VX MLNSLOZKR
# FATEC ??????
# PYTHON ?????

# S xor ' ' = 19 xor 0 = 10011 xor 00000 = 10011 = S

# VX MLNSLOZKR = SLOZKR
# FATEC S????? = SANTOS?
# PYTHON ????? =  

# L xor A = 12 xor 1  = 01100 xor 00001 = 01101 = 13 = M
# O xor N = 15 xor 14 = 01111 xor 01110 = 00001 = 1  = A
# Z xor T = 26 xor 20 = 11010 xor 10100 = 01110 = 14 = N
# K xor O = 11 xor 15 = 01011 xor 01111 = 00100 = 4  = D
# R xor S = 18 xor 19 = 10010 xor 10011 = 00001 = 1  = A

# VX MLNSLOZKR
# FATEC SANTOS
# PYTHON MANDA 

