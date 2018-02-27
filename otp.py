#sifer text only attack PESQUISAR AULA PASSADA

# Pesquisar sobre a criptografia ONE TIME PAD

# e(k, m) = k XOR m
# d(k, c) = k XOR c

# K = {0,1}^n = C = M

# 1 - Transforme K e M em INT
# 2 - Realize o XOR (INT -> BINÁRIO)
# 3 - Transforme INT em STRING
# 4 - Transforme STRING em HEXA

# Fato: O OTP é consistente
# Demonstração: D(k, E(k, m)) = k XOR E(k, m) = k XOR k XOR m = 0 XOR m = m

# A(65) F(70) = (64, 1) xor (64, 4, 2) = 7 = 07
# C(67) A(65) = (64, 2, 1) xor (64, 1) = 2 = 02
# W(87) T(84) = (64, 16, 4, 2, 1) xor (64, 16, 4) = 3 = 03
# P(80) E(69) = (64, 16) xor (64, 4, 1) = 21 = 15
# Z(90) C(67) = (64, 16, 8, 2) xor (64, 2, 1) = 25 = 19
# 07 02 03 15 19
# HEX(ACWPZ xor FATEC) = 0702031519

# TWO TIME PAD - TTP

# Suponha que você tenha obtido dois textos cifrados (c1 e c2)
