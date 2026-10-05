"""Análise de frequência: descobre a chave pela letra mais comum.

Criador: Guilherme Aguiar Moreira
"""

from frequencia_pt import ALFABETO, contar_frequencias

__all__ = ["quebrar_cesar_por_frequencia"]


def quebrar_cesar_por_frequencia(cifrado: str, decifrar_cesar) -> tuple:
    """Supõe que a letra mais comum do cifrado é o 'A' (mais comum do português).

    Calcula a chave direto, sem testar todas as possibilidades.
    """
    freq = contar_frequencias(cifrado)
    mais_comum = max(freq, key=freq.get)

    # Distância entre a letra mais comum e o 'A' é o deslocamento do César.
    chave = (ALFABETO.index(mais_comum) - ALFABETO.index("A")) % 26

    return chave, decifrar_cesar(cifrado, chave)


# Testes
if __name__ == "__main__":
    from cesar import decifrar_cesar  # ajustar para o nome real (Nicole)

    # Mensagem curta (38 letras), César chave 7
    c_curto = "AYHUZMLYPYKVJBTLUAVWHYHZLYCPKVYJLUAYHS"

    # Texto maior, César chave 11
    c_longo = (
        "LPXACPDLACPNTDLACZEPRPCZDOZNFXPYEZDNZYQTOPYNTLTDLCXLKPYLOZDYZDPCGTOZCNP"
        "YECLWAZTDLWRFYDLCBFTGZDQZCLXLNPDDLOZDAZCAPDDZLDDPXLFEZCTKLNLZPFXNZYECL"
    )

    # Frequência só funciona bem com texto grande.
    print("Texto curto:", quebrar_cesar_por_frequencia(c_curto, decifrar_cesar))  # erra
    print("Texto longo:", quebrar_cesar_por_frequencia(c_longo, decifrar_cesar))  # acerta