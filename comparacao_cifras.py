"""Comparação das cifras clássicas: espaço de chaves e principal ataque.

Criador: Guilherme Aguiar Moreira
"""

__all__ = ["COMPARACAO", "imprimir_comparacao"]

# (cifra, chaves possíveis, como quebra)
COMPARACAO = [
    ("César",        "26",             "Força bruta"),
    ("Afim",         "312",            "Força bruta"),
    ("Substituição", "26! (~4·10^26)", "Análise de frequência"),
    ("Vigenère",     "26^t",           "Frequência por coluna"),
    ("Hill",         "~157 mil (2x2)", "Texto claro conhecido"),
    ("Transposição", "t!",             "Testar permutações"),
    ("Fluxo",        "2^n",            "Só segura se a chave não se repete"),
]


def imprimir_comparacao() -> None:
    print(f"{'Cifra':<14}{'Chaves possíveis':<19}Como quebra")
    for cifra, chaves, ataque in COMPARACAO:
        print(f"{cifra:<14}{chaves:<19}{ataque}")


if __name__ == "__main__":
    imprimir_comparacao()