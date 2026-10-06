"""Inverso Multiplicativo.

Criador: Guilherme Aguiar Moreira
"""

from euclides_estendido import euclides_estendido

__all__ = ["inverso_multiplicativo"]


def inverso_multiplicativo(a: int, m: int) -> int:
    """Retorna x tal que (a * x) mod m = 1. Só existe se mdc(a, m) = 1."""
    # O coeficiente x de Bézout é candidato ao inverso de a.
    mdc, x, _ = euclides_estendido(a, m)

    # O inverso só existe quando a e m são coprimos.
    if mdc != 1:
        raise ValueError(f"Inverso de {a} mod {m} não existe (mdc = {mdc}).")

    # Normaliza o inverso para o intervalo de 0 a m - 1.
    return x % m


# Testes
if __name__ == "__main__":
    for a, m in [(23, 60), (9, 40), (31, 97)]:
        inv = inverso_multiplicativo(a, m)
        print(f"inverso_multiplicativo({a}, {m}) = {inv}")
        assert (a * inv) % m == 1

    try:
        inverso_multiplicativo(8, 12)
    except ValueError as e:
        print(f"Erro esperado: {e}")

