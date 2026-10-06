# ==============================================================================
# PROJETO: SecureDocs - Missão 2: Criptografia Clássica
# AUTOR: Mateus Afonso
#
# CONTEÚDO IMPLEMENTADO:
# 1. Cifra de Hill (Cifra de Bloco baseada em Álgebra Linear Modular)
# 2. Cifra de Transposição (Transposição Colunar com Palavra-Chave)
# 3. Cifra de Fluxo (Stream Cipher baseada no modelo de Vernam / One-Time Pad com XOR)
#
# INTEGRAÇÃO:
# Reutiliza funções da biblioteca matemática da Missão 1 (mdc, inverso_multiplicativo).
# ==============================================================================

import numpy as np
import os
import math

# ------------------------------------------------------------------------------
# Importação dos módulos matemáticos da Missão 1, incluídos nesta raiz
# ------------------------------------------------------------------------------
# Funções desenvolvidas na Missão 1 reutilizadas aqui:
# - calcular_mdc / coprimos: garante que a matriz da Cifra de Hill tem inversa mod 26.
# - inverso_multiplicativo: calcula o inverso modular do determinante para decifrar Hill.
from mdc import calcular_mdc, coprimos
from inverso_multiplicativo import inverso_multiplicativo


# ==============================================================================
# 1. CIFRA DE HILL
# ==============================================================================
# CONCEITO TEÓRICO:
# - Criada por Lester S. Hill em 1929.
# - É uma cifra poligráfica (de bloco): divide o texto em blocos de tamanho 'n'
#   e multiplica cada bloco por uma matriz-chave n x n usando aritmética modular (mod 26).
# - RESISTÊNCIA: Dificulta muito a análise de frequência de letras isoladas (monogramas),
#   pois uma mesma letra no texto claro é cifrada de formas distintas dependendo das
#   letras vizinhas no mesmo bloco.
# ------------------------------------------------------------------------------

def preparar_texto_hill(texto, tamanho_bloco):
    """
    Padroniza a entrada:
    1. Filtra apenas letras (A-Z) e descarta espaços/símbolos.
    2. Converte tudo para maiúsculo.
    3. Aplica padding com 'X' se o tamanho do texto não for múltiplo de tamanho_bloco.
    4. Mapeia caracteres para números inteiros: A -> 0, B -> 1, ..., Z -> 25.
    """
    texto_limpo = "".join([c.upper() for c in texto if c.isalpha()])
    
    # Preenchimento (padding) para completar o último bloco
    while len(texto_limpo) % tamanho_bloco != 0:
        texto_limpo += "X"
        
    return [ord(c) - ord('A') for c in texto_limpo]


def validar_chave_hill(matriz_chave):
    """
    Verificação Matemática Essencial:
    Para que a mensagem possa ser decifrada, a matriz-chave DEVE ter matriz inversa em Z_26.
    Condições necessárias:
    1. det(K) != 0 mod 26
    2. mdc(det(K), 26) == 1 (ou seja, det(K) e 26 DEVEM ser coprimos).
    Caso contrário, não existe o inverso multiplicativo de det(K) mod 26.
    """
    tamanho_alfabeto = 26
    det = int(round(np.linalg.det(matriz_chave))) % tamanho_alfabeto
    
    # Ponto de integração com a Missão 1: validação por coprimos
    if not coprimos(det, tamanho_alfabeto):
        raise ValueError(
            f"Chave inválida! Determinante mod 26 ({det}) e 26 não são coprimos. "
            "A matriz não possui inversa modular, impossibilitando a decifragem."
        )
    return det


def matriz_inversa_modular(matriz_chave, modulo=26):
    """
    Calcula a matriz inversa em aritmética modular mod 26:
        K^(-1) = det(K)^(-1) * adj(K) (mod 26)
    
    Onde:
    - det(K)^(-1) é o inverso multiplicativo modular do determinante (função da Missão 1).
    - adj(K) é a matriz adjunta (transposta da matriz de cofatores).
    """
    det = validar_chave_hill(matriz_chave)
    
    # Ponto de integração com a Missão 1: inverso multiplicativo
    det_inv = inverso_multiplicativo(det, modulo)
    
    n = matriz_chave.shape[0]
    matriz_adj = np.zeros((n, n), dtype=int)
    
    # Cálculo manual da matriz de cofatores transposta (matriz adjunta)
    for i in range(n):
        for j in range(n):
            submatriz = np.delete(np.delete(matriz_chave, i, axis=0), j, axis=1)
            cofator = ((-1) ** (i + j)) * int(round(np.linalg.det(submatriz)))
            # matriz_adj[j][i] já armazena a transposta
            matriz_adj[j][i] = cofator % modulo
            
    # Multiplicação escalar modular: inversa = (det_inv * adj) % 26
    matriz_inv = (det_inv * matriz_adj) % modulo
    return matriz_inv


def cifra_hill(texto, matriz_chave):
    """
    Cifragem: C = (K * P) mod 26
    - P: vetor coluna do bloco de texto claro.
    - K: matriz-chave.
    - C: vetor coluna resultante cifrado.
    """
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
    """
    Decifragem: P = (K^(-1) * C) mod 26
    Aplica a multiplicação dos blocos cifrados pela matriz inversa modular.
    """
    matriz_inv = matriz_inversa_modular(matriz_chave, modulo=26)
    bloco_tam = matriz_chave.shape[0]
    vetor_numeros = [ord(c) - ord('A') for c in texto_cifrado]
    
    decifrado = ""
    for i in range(0, len(vetor_numeros), bloco_tam):
        bloco = np.array(vetor_numeros[i:i + bloco_tam])
        resultado = np.dot(matriz_inv, bloco) % 26
        decifrado += "".join(chr(int(n) + ord('A')) for n in resultado)
        
    return decifrado


# ==============================================================================
# 2. CIFRA DE TRANSPOSIÇÃO COLUNAR
# ==============================================================================
# CONCEITO TEÓRICO:
# - Não altera a identidade dos caracteres (não faz substituição).
# - Apenas permuta (reorganiza) a ordem das posições dos caracteres.
# - VULNERABILIDADE: Um criptoanalista consegue identificar a técnica imediatamente
#   porque o histograma de frequências das letras do texto cifrado é IDÊNTICO
#   ao do texto claro original.
# ------------------------------------------------------------------------------

def cifra_transposicao(texto, chave):
    """
    1. Preenche uma matriz (grid) linha por linha com o texto.
    2. Lê as colunas na ordem alfabética da palavra-chave.
    """
    texto_limpo = "".join([c.upper() for c in texto if c.isalpha()])
    num_colunas = len(chave)
    num_linhas = math.ceil(len(texto_limpo) / num_colunas)
    
    # Preenche o grid inicial com padding 'X'
    grid = [['X'] * num_colunas for _ in range(num_linhas)]
    idx = 0
    for r in range(num_linhas):
        for c in range(num_colunas):
            if idx < len(texto_limpo):
                grid[r][c] = texto_limpo[idx]
                idx += 1
                
    # Determina a ordem de leitura das colunas com base na ordem alfabética da chave
    # Exemplo: 'SECURE' -> 'C' (coluna 2), 'E' (coluna 1), etc.
    ordem_colunas = sorted(range(len(chave)), key=lambda k: chave[k])
    
    # Lê as colunas selecionadas de cima para baixo
    texto_cifrado = ""
    for c in ordem_colunas:
        for r in range(num_linhas):
            texto_cifrado += grid[r][c]
            
    return texto_cifrado


def decifra_transposicao(texto_cifrado, chave):
    """
    Reverte o processo de leitura:
    1. Preenche o grid coluna por coluna seguindo a ordem alfabética da chave.
    2. Lê o texto reconstruído linha por linha.
    """
    num_colunas = len(chave)
    num_linhas = math.ceil(len(texto_cifrado) / num_colunas)
    ordem_colunas = sorted(range(len(chave)), key=lambda k: chave[k])
    
    grid = [[''] * num_colunas for _ in range(num_linhas)]
    idx = 0
    for c in ordem_colunas:
        for r in range(num_linhas):
            grid[r][c] = texto_cifrado[idx]
            idx += 1
            
    # Reconstrução do texto original lendo as linhas sequencialmente
    texto_decifrado = ""
    for r in range(num_linhas):
        for c in range(num_colunas):
            texto_decifrado += grid[r][c]
            
    return texto_decifrado


# ==============================================================================
# 3. CIFRAS DE FLUXO (STREAM CIPHER - VERNAM / ONE-TIME PAD)
# ==============================================================================
# CONCEITO TEÓRICO:
# - Opera byte a byte (ou bit a bit) em fluxo contínuo.
# - Utiliza a operação binária XOR (^):
#       C = P ^ K
#       P = C ^ K  (pois (P ^ K) ^ K = P)
# - SEGURANÇA PERFEITA (Shannon, 1949): Se a chave for verdadeiramente aleatória,
#   do mesmo tamanho da mensagem e NUNCA reutilizada, a cifra é matematicamente inquebrável.
# - VULNERABILIDADE CRÍTICA (Two-Time Pad): Se a mesma chave K for usada para cifrar duas mensagens:
#       C1 ^ C2 = (P1 ^ K) ^ (P2 ^ K) = P1 ^ P2
#   A chave é eliminada e os dois textos claros podem ser recuperados por criptoanálise.
# ------------------------------------------------------------------------------

def cifra_fluxo(texto_claro, chave_bytes=None):
    """
    Cifra um texto usando XOR byte a byte com um fluxo de chave (keystream).
    Se nenhuma chave for fornecida, gera uma chave criptograficamente segura via os.urandom.
    """
    texto_bytes = texto_claro.encode('utf-8')
    
    if chave_bytes is None:
        chave_bytes = os.urandom(len(texto_bytes))
    elif len(chave_bytes) < len(texto_bytes):
        raise ValueError("A chave de fluxo deve ser pelo menos do tamanho do texto.")
        
    # Operação XOR byte a byte
    cifrado_bytes = bytes([b ^ k for b, k in zip(texto_bytes, chave_bytes)])
    return cifrado_bytes, chave_bytes


def decifra_fluxo(cifrado_bytes, chave_bytes):
    """
    Decifra o texto aplicando novamente a operação XOR entre o texto cifrado e a chave.
    Propriedade da álgebra booleana: (A ^ B) ^ B = A.
    """
    decifrado_bytes = bytes([b ^ k for b, k in zip(cifrado_bytes, chave_bytes)])
    return decifrado_bytes.decode('utf-8')
