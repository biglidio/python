def geraNovoBit(bits):
    i = 0
    while True:
        bits.append(0)
        bits[i+5] = bits[i+2] ^ bits[i+4] ^ bits[i+3] ^ bits[i]
        yield bits[i+5]
        i = i + 1
    
gerador = geraNovoBit([1,0,0,1,1]);

print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()

# ------------------

print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
