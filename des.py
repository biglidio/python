from Crypto.Cipher import DES

key = 'ABCDEFGH'
#Initializaton vector, seed inicial.
#Ele n eh usado (ignorado) no MODO
#ECB
#No modo CBC, ele eh usado
iv = "ABCDEFGW"
cipher = DES.new(key, DES.MODE_CBC, iv)
plaintext = 'OLAFATEC'
cifrado = cipher.encrypt(plaintext)
print cifrado.encode("hex")