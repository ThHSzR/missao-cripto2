"""Convenções compartilhadas para as cifras de letras da missão."""

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TAMANHO_ALFABETO = len(ALFABETO)


def preparar_texto(texto: str) -> str:
    """Aceita letras A-Z e espaços; devolve letras em maiúsculas.

    A validação evita descartar acentos ou sinais silenciosamente, o que
    poderia alterar o conteúdo original de uma mensagem.
    """
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string.")

    preparado = texto.upper()
    if any(caractere not in ALFABETO + " " for caractere in preparado):
        raise ValueError("Use apenas letras A-Z sem acentos e espaços.")
    return preparado
