"""Frequência das letras em português e pontuação de textos.

Criador: Guilherme Aguiar Moreira
"""

import unicodedata

__all__ = ["ALFABETO", "FREQ_PT", "limpar", "contar_frequencias", "pontuar"]

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Frequência das letras em português (%)
FREQ_PT = {
    'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57, 'F': 1.02,
    'G': 1.30, 'H': 1.28, 'I': 6.18, 'J': 0.40, 'K': 0.02, 'L': 2.78,
    'M': 4.74, 'N': 5.05, 'O': 10.73, 'P': 2.52, 'Q': 1.20, 'R': 6.53,
    'S': 7.81, 'T': 4.34, 'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21,
    'Y': 0.01, 'Z': 0.47,
}


def limpar(texto: str) -> str:
    """Remove acentos, espaços e pontuação; deixa só letras maiúsculas A-Z."""
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return "".join(c for c in texto.upper() if c in ALFABETO)


def contar_frequencias(texto: str) -> dict:
    """Retorna a porcentagem de cada letra no texto."""
    texto = limpar(texto)

    # Texto vazio: todas as letras com frequência 0.
    if not texto:
        return {l: 0.0 for l in ALFABETO}

    return {l: texto.count(l) * 100 / len(texto) for l in ALFABETO}


def pontuar(texto: str) -> float:
    """Mede o quanto o texto parece português (qui-quadrado).

    Quanto MENOR a nota, mais parecido com português.
    """
    texto = limpar(texto)

    # Texto vazio não parece português: nota infinita.
    if not texto:
        return float("inf")

    nota = 0

    # Compara quantas vezes cada letra aparece com o esperado no português.
    for l in ALFABETO:
        esperado = FREQ_PT[l] * len(texto) / 100
        nota += (texto.count(l) - esperado) ** 2 / esperado

    return nota


# Testes
if __name__ == "__main__":
    portugues = "TRANSFERIRDOCUMENTOPARASERVIDORCENTRAL"
    embaralhado = "XQZWKYJXQZWKYJXQZWKYJXQZWKYJXQZWKYJXQZ"

    print(f"Nota texto em português: {pontuar(portugues):.1f}")    # baixa
    print(f"Nota texto sem sentido:  {pontuar(embaralhado):.1f}")  # muito alta
