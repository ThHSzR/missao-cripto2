import numpy as np
from minhas_cifras import (
    cifra_hill, decifra_hill,
    cifra_transposicao, decifra_transposicao,
    cifra_fluxo, decifra_fluxo
)

# Mensagem confidencial descrita na Missão 2
mensagem = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"

print("=" * 65)
print(f"TEXTO ORIGINAL: {mensagem}")
print("=" * 65)


# -------------------------------------------------------------
# 1. TESTE CIFRA DE HILL (Matriz 3x3)
# -------------------------------------------------------------
print("\n--- [1] CIFRA DE HILL ---")
# Matriz inversível em mod 26: det = 25, mdc(25, 26) = 1
chave_hill = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

cifrado_h = cifra_hill(mensagem, chave_hill)
decifrado_h = decifra_hill(cifrado_h, chave_hill)

print(f"Texto Cifrado   : {cifrado_h}")
print(f"Texto Decifrado : {decifrado_h}")


# -------------------------------------------------------------
# 2. TESTE TRANSPOSIÇÃO COLUNAR
# -------------------------------------------------------------
print("\n--- [2] CIFRA DE TRANSPOSIÇÃO ---")
chave_transp = "SECURE"

cifrado_t = cifra_transposicao(mensagem, chave_transp)
decifrado_t = decifra_transposicao(cifrado_t, chave_transp)

print(f"Chave utilizada : {chave_transp}")
print(f"Texto Cifrado   : {cifrado_t}")
print(f"Texto Decifrado : {decifrado_t}")


# -------------------------------------------------------------
# 3. TESTE CIFRA DE FLUXO (Vernam / One-Time Pad)
# -------------------------------------------------------------
print("\n--- [3] CIFRA DE FLUXO (STREAM CIPHER) ---")
cifrado_f, chave_stream = cifra_fluxo(mensagem)
decifrado_f = decifra_fluxo(cifrado_f, chave_stream)

print(f"Fluxo Cifrado (Hex) : {cifrado_f.hex()}")
print(f"Chave Usada   (Hex) : {chave_stream.hex()}")
print(f"Texto Decifrado     : {decifrado_f}")
print("=" * 65)