"""Algoritmo Estendido de Euclides.

Criador: Guilherme Aguiar Moreira
"""

from mdc import calcular_mdc

__all__ = ["euclides_estendido"]


def euclides_estendido(a: int, b: int) -> tuple[int, int, int]:
    """Retorna (mdc, x, y) tais que a*x + b*y = mdc(a, b)."""
    # Mantém os restos e os coeficientes de Bézout de duas etapas.
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    # Atualiza restos e coeficientes usando o mesmo quociente.
    while r != 0:
        quociente = old_r // r
        old_r, r = r, old_r - quociente * r
        old_x, x = x, old_x - quociente * x
        old_y, y = y, old_y - quociente * y

    # Confere o MDC e devolve os coeficientes finais.
    mdc = old_r
    assert mdc == calcular_mdc(a, b)
    return mdc, old_x, old_y


# Testes
if __name__ == "__main__":
    casos = [(1071, 462), (252, 105), (81, 57), (101, 13)]
    for a, b in casos:
        mdc, x, y = euclides_estendido(a, b)
        print(f"euclides_estendido({a}, {b}) = (mdc={mdc}, x={x}, y={y})")
        assert a * x + b * y == mdc

