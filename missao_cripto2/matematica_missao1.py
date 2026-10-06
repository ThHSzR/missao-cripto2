"""Aritmética modular da Missão 1, preservada para uso local.

Fonte: ThHSzR/missao-cripto, aritmetica_modular.py, commit
c7bbf16585cefa2cb1d817da6b1d1c7088e0ccf6.
Autoria indicada no README da Missão 1: Nicole Noleto.
"""


def aritmetica_modular(a: int, b: int, m: int) -> dict:
    """Calcula a soma, subtração e multiplicação de dois números
    no módulo m.

    Args:
        a: Primeiro número inteiro.
        b: Segundo número inteiro.
        m: Módulo, que deve ser maior que zero.
    """
    # O módulo precisa ser positivo para que a operação seja válida.
    if m <= 0:
        raise ValueError("O módulo deve ser maior que zero.")

    # Reduz cada operação ao intervalo definido pelo módulo.
    return {
        "soma": (a + b) % m,
        "subtracao": (a - b) % m,
        "multiplicacao": (a * b) % m
    }


if __name__ == "__main__":

    print("=== TESTES DE ARITMÉTICA MODULAR ===")

    a = 17
    b = 8
    m = 5

    resultado = aritmetica_modular(a, b, m)

    print(f"\nValores: a = {a}, b = {b}, m = {m}")

    print(f"Soma:          ({a} + {b}) mod {m} = "
          f"{resultado['soma']}")

    print(f"Subtração:     ({a} - {b}) mod {m} = "
          f"{resultado['subtracao']}")

    print(f"Multiplicação: ({a} * {b}) mod {m} = "
          f"{resultado['multiplicacao']}")
