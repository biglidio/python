import random

def rolar():
    freq = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    times = 1000000
    
    for i in range(times):
        dado = random.randint(1,6)
        freq[dado] = freq[dado] + 1
        
    for f in freq:
        print str(f) + " -> " + str(100*freq[f]/times) + "%"

rolar()