"""Demonstrações das cifras de Mateus com chave de Hill escolhida pelo usuário."""

import argparse
import numpy as np

from minhas_cifras import (
    cifra_hill, decifra_hill, validar_chave_hill,
    cifra_transposicao, decifra_transposicao,
    cifra_fluxo, decifra_fluxo,
)

MENSAGEM = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
MATRIZ_EXEMPLO = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])


def matriz_sugerida(dimensao):
    """Gera uma chave triangular com determinante 1 para qualquer dimensão aceita."""
    if dimensao == 3:
        return MATRIZ_EXEMPLO.copy()
    matriz = np.eye(dimensao, dtype=int)
    for i in range(dimensao - 1):
        matriz[i, i + 1] = 1
    return matriz


def escolher_matriz():
    while True:
        try:
            dimensao = int(input("Dimensão da matriz de Hill (2 a 8) [3]: ").strip() or "3")
            if 2 <= dimensao <= 8:
                break
        except ValueError:
            pass
        print("Informe um número inteiro entre 2 e 8.")

    sugestao = matriz_sugerida(dimensao)
    print(f"Matriz sugerida {dimensao}x{dimensao} (invertível módulo 26):\n{sugestao}")
    if input("Usar a matriz sugerida? [S/n]: ").strip().lower() not in ("n", "nao", "não"):
        return sugestao

    while True:
        linhas = []
        for i in range(dimensao):
            while True:
                entrada = input(f"Linha {i + 1} ({dimensao} inteiros separados por espaços): ").split()
                try:
                    linha = [int(valor) for valor in entrada]
                except ValueError:
                    linha = []
                if len(linha) == dimensao:
                    linhas.append(linha)
                    break
                print(f"Informe exatamente {dimensao} números inteiros.")
        matriz = np.array(linhas, dtype=object)
        try:
            validar_chave_hill(matriz)
            return matriz
        except ValueError as erro:
            print(f"{erro} Digite outra matriz.")


def main(interativo=True):
    print("=" * 65)
    print(f"TEXTO ORIGINAL: {MENSAGEM}")
    print("=" * 65)
    chave_hill = escolher_matriz() if interativo else MATRIZ_EXEMPLO

    print(f"\n--- [1] CIFRA DE HILL ({chave_hill.shape[0]}x{chave_hill.shape[0]}) ---")
    print(f"Matriz-chave:\n{chave_hill}")
    cifrado_h = cifra_hill(MENSAGEM, chave_hill)
    print(f"Texto Cifrado   : {cifrado_h}")
    print(f"Texto Decifrado : {decifra_hill(cifrado_h, chave_hill)}")

    print("\n--- [2] CIFRA DE TRANSPOSIÇÃO ---")
    chave_transp = "SECURE"
    cifrado_t = cifra_transposicao(MENSAGEM, chave_transp)
    print(f"Chave utilizada : {chave_transp}")
    print(f"Texto Cifrado   : {cifrado_t}")
    print(f"Texto Decifrado : {decifra_transposicao(cifrado_t, chave_transp)}")

    print("\n--- [3] CIFRA DE FLUXO (XOR) ---")
    cifrado_f, chave_stream = cifra_fluxo(MENSAGEM)
    print(f"Fluxo Cifrado (Hex) : {cifrado_f.hex()}")
    print(f"Chave Usada   (Hex) : {chave_stream.hex()}")
    print(f"Texto Decifrado     : {decifra_fluxo(cifrado_f, chave_stream)}")
    print("=" * 65)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--padrao", action="store_true", help="Executa com a matriz 3x3 de exemplo sem pedir dados")
    main(interativo=not parser.parse_args().padrao)
