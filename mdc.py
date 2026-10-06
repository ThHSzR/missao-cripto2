"""Módulo de operações aritméticas: MDC e Coprimos.

Criador: Mateus Afonso Miranda de Oliveira
"""

__all__ = ["calcular_mdc", "coprimos"]


def calcular_mdc(a: int, b: int) -> int:
    """Calcula o Máximo Divisor Comum (MDC) entre dois inteiros utilizando o Algoritmo de Euclides.

    """
    # O sinal não altera os divisores comuns.
    a, b = abs(a), abs(b)

    # Repete divisões sucessivas até o resto ser zero.
    while b != 0:
        a, b = b, a % b
    return a


def coprimos(a: int, b: int) -> bool:
    """Verifica se dois números inteiros são coprimos (primos entre si).

    Dois números são coprimos se o único divisor positivo comum entre eles for 1.

    """
    # Dois números são coprimos quando o único divisor comum é 1.
    return calcular_mdc(a, b) == 1


# Bloco de testes no escopo local
if __name__ == "__main__":
    print("--- Testes de MDC ---")
    print(f"MDC(48, 18) = {calcular_mdc(48, 18)}")  # 6
    print(f"MDC(35, 10) = {calcular_mdc(35, 10)}")  # 5

    print("\n--- Testes de Primos entre si ---")
    print(f"14 e 15 são primos entre si? {coprimos(14, 15)}")  # True (MDC = 1)
    print(f"14 e 21 são primos entre si? {coprimos(14, 21)}")  # False (MDC = 7)