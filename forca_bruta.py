"""Ataque de força bruta: testa todas as chaves possíveis.

Criador: Guilherme Aguiar Moreira
"""

from mdc import coprimos  # Missão 1
from frequencia_pt import pontuar

__all__ = ["forca_bruta", "quebrar_cesar", "quebrar_afim"]


def forca_bruta(cifrado: str, decifrar, chaves) -> tuple:
    """Testa todas as chaves e retorna (chave, texto) que mais parece português."""
    # Decifra com cada chave e dá uma nota para o resultado.
    tentativas = [(pontuar(decifrar(cifrado, k)), k) for k in chaves]

    # A menor nota é a tentativa mais parecida com português.
    melhor_nota, melhor_chave = min(tentativas)

    return melhor_chave, decifrar(cifrado, melhor_chave)


def quebrar_cesar(cifrado: str, decifrar_cesar) -> tuple:
    """César tem só 26 chaves possíveis."""
    return forca_bruta(cifrado, decifrar_cesar, range(26))


def quebrar_afim(cifrado: str, decifrar_afim) -> tuple:
    """Afim: 'a' precisa ser coprimo com 26 (12 valores) e 'b' vai de 0 a 25.

    Total: 12 * 26 = 312 chaves.
    """
    chaves = [(a, b) for a in range(26) if coprimos(a, 26) for b in range(26)]
    return forca_bruta(cifrado, decifrar_afim, chaves)


# Testes
if __name__ == "__main__":
    from cesar import cesar_decifrar as decifrar_cesar
    from afim_vigenere import CifraAfim

    # A função da marini recebe (texto, a, b); a força bruta passa a chave como (a, b).
    def decifrar_afim(texto, chave):
        a, b = chave
        return CifraAfim.decifrar(texto, a, b)

    # "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL" cifrada
    c_cesar = "AYHUZMLYPYKVJBTLUAVWHYHZLYCPKVYJLUAYHS"  # César, chave 7
    c_afim = "ZPIVUHCPWPXASEQCVZAFIPIUCPJWXAPSCVZPIL"   # Afim, chave (5, 8)

    print("Força bruta César:", quebrar_cesar(c_cesar, decifrar_cesar))
    print("Força bruta Afim: ", quebrar_afim(c_afim, decifrar_afim))
