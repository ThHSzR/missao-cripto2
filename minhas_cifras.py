# Feito por: Mateus Afonso 
import sys
from pathlib import Path
import numpy as np
import os
import math

# Garante que a pasta missao-cripto seja encontrada para importação
sys.path.append(str(Path(__file__).resolve().parent / "missao-cripto"))

# Importando as funções desenvolvidas na Missão 1
from mdc import calcular_mdc, coprimos
from inverso_multiplicativo import inverso_multiplicativo


# ==========================================================
# 1. CIFRA DE HILL (Blocos / Álgebra Linear)
# ==========================================================
def preparar_texto_hill(texto, tamanho_bloco):
    texto_limpo = "".join([c.upper() for c in texto if c.isalpha()])
    while len(texto_limpo) % tamanho_bloco != 0:
        texto_limpo += "X"  # Padding
    return [ord(c) - ord('A') for c in texto_limpo]

def validar_chave_hill(matriz_chave):
    tamanho_alfabeto = 26
    det = int(round(np.linalg.det(matriz_chave))) % tamanho_alfabeto
    
    # Validação com a função coprimos da Missão 1
    if not coprimos(det, tamanho_alfabeto):
        raise ValueError(
            f"Chave inválida! Determinante mod 26 ({det}) e 26 não são coprimos."
        )
    return det

def matriz_inversa_modular(matriz_chave, modulo=26):
    det = validar_chave_hill(matriz_chave)
    
    # Inverso multiplicativo modular vindo da Missão 1
    det_inv = inverso_multiplicativo(det, modulo)
    
    # Matriz adjunta (transposta da matriz de cofatores)
    n = matriz_chave.shape[0]
    matriz_adj = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            submatriz = np.delete(np.delete(matriz_chave, i, axis=0), j, axis=1)
            cofator = ((-1) ** (i + j)) * int(round(np.linalg.det(submatriz)))
            matriz_adj[j][i] = cofator % modulo  # Já transpondo j, i
            
    matriz_inv = (det_inv * matriz_adj) % modulo
    return matriz_inv

def cifra_hill(texto, matriz_chave):
    validar_chave_hill(matriz_chave)
    bloco_tam = matriz_chave.shape[0]
    vetor_numeros = preparar_texto_hill(texto, bloco_tam)
    
    cifrado = ""
    for i in range(0, len(vetor_numeros), bloco_tam):
        bloco = np.array(vetor_numeros[i:i + bloco_tam])
        resultado = np.dot(matriz_chave, bloco) % 26
        cifrado += "".join(chr(int(n) + ord('A')) for n in resultado)
    return cifrado

def decifra_hill(texto_cifrado, matriz_chave):
    matriz_inv = matriz_inversa_modular(matriz_chave, modulo=26)
    bloco_tam = matriz_chave.shape[0]
    vetor_numeros = [ord(c) - ord('A') for c in texto_cifrado]
    
    decifrado = ""
    for i in range(0, len(vetor_numeros), bloco_tam):
        bloco = np.array(vetor_numeros[i:i + bloco_tam])
        resultado = np.dot(matriz_inv, bloco) % 26
        decifrado += "".join(chr(int(n) + ord('A')) for n in resultado)
    return decifrado


# ==========================================================
# 2. CIFRA DE TRANSPOSIÇÃO (Colunar com Palavra-Chave)
# ==========================================================
def cifra_transposicao(texto, chave):
    texto_limpo = "".join([c.upper() for c in texto if c.isalpha()])
    num_colunas = len(chave)
    num_linhas = math.ceil(len(texto_limpo) / num_colunas)
    
    grid = [['X'] * num_colunas for _ in range(num_linhas)]
    idx = 0
    for r in range(num_linhas):
        for c in range(num_colunas):
            if idx < len(texto_limpo):
                grid[r][c] = texto_limpo[idx]
                idx += 1
                
    ordem_colunas = sorted(range(len(chave)), key=lambda k: chave[k])
    texto_cifrado = ""
    for c in ordem_colunas:
        for r in range(num_linhas):
            texto_cifrado += grid[r][c]
            
    return texto_cifrado

def decifra_transposicao(texto_cifrado, chave):
    num_colunas = len(chave)
    num_linhas = math.ceil(len(texto_cifrado) / num_colunas)
    ordem_colunas = sorted(range(len(chave)), key=lambda k: chave[k])
    
    grid = [[''] * num_colunas for _ in range(num_linhas)]
    idx = 0
    for c in ordem_colunas:
        for r in range(num_linhas):
            grid[r][c] = texto_cifrado[idx]
            idx += 1
            
    texto_decifrado = ""
    for r in range(num_linhas):
        for c in range(num_colunas):
            texto_decifrado += grid[r][c]
            
    return texto_decifrado


# ==========================================================
# 3. CIFRAS DE FLUXO (Vernam / One-Time Pad com XOR)
# ==========================================================
def cifra_fluxo(texto_claro, chave_bytes=None):
    texto_bytes = texto_claro.encode('utf-8')
    if chave_bytes is None:
        chave_bytes = os.urandom(len(texto_bytes))
    elif len(chave_bytes) < len(texto_bytes):
        raise ValueError("A chave de fluxo deve ser pelo menos do tamanho do texto.")
        
    cifrado_bytes = bytes([b ^ k for b, k in zip(texto_bytes, chave_bytes)])
    return cifrado_bytes, chave_bytes

def decifra_fluxo(cifrado_bytes, chave_bytes):
    decifrado_bytes = bytes([b ^ k for b, k in zip(cifrado_bytes, chave_bytes)])
    return decifrado_bytes.decode('utf-8')