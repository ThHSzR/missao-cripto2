"""Mostra texto claro, chave, transformação e recuperação em um símbolo.

Este módulo ilustra os conceitos do resumo. Não implementa uma cifra para
mensagens nem faz criptoanálise.
"""

from dataclasses import dataclass

from .matematica_missao1 import aritmetica_modular


@dataclass(frozen=True)
class ExemploConceitual:
    indice_claro: int
    chave: int
    modulo: int
    indice_cifrado: int
    indice_recuperado: int


def calcular_exemplo(indice_claro: int, chave: int, modulo: int = 26) -> ExemploConceitual:
    """Aplica (m + k) mod n e (c - k) mod n com a biblioteca da Missão 1."""
    if any(type(valor) is not int for valor in (indice_claro, chave, modulo)):
        raise TypeError("Índice, chave e módulo devem ser inteiros.")
    if modulo <= 1:
        raise ValueError("O módulo deve ser maior que 1.")
    if not 0 <= indice_claro < modulo:
        raise ValueError("O índice deve estar entre 0 e módulo - 1.")

    indice_cifrado = aritmetica_modular(indice_claro, chave, modulo)["soma"]
    indice_recuperado = aritmetica_modular(indice_cifrado, chave, modulo)[
        "subtracao"
    ]
    return ExemploConceitual(
        indice_claro, chave, modulo, indice_cifrado, indice_recuperado
    )


def main() -> None:
    exemplo = calcular_exemplo(19, 3)
    print("Regra pública: c = (m + k) mod 26; m = (c - k) mod 26")
    print(f"Texto claro: T (índice {exemplo.indice_claro})")
    print(f"Chave do exemplo: {exemplo.chave}")
    print(f"Texto cifrado: W (índice {exemplo.indice_cifrado})")
    print(f"Texto recuperado: T (índice {exemplo.indice_recuperado})")
    print("A reversibilidade, sozinha, não demonstra segurança.")


if __name__ == "__main__":
    main()
