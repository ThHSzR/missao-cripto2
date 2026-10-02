"""Cifra de César para demonstração didática, inadequada para segurança real."""

from .alfabeto import ALFABETO, TAMANHO_ALFABETO, preparar_texto


def _validar_chave(chave: int) -> None:
    if isinstance(chave, bool) or not isinstance(chave, int):
        raise TypeError("A chave deve ser um número inteiro.")


def _deslocar(texto: str, chave: int) -> str:
    _validar_chave(chave)
    preparado = preparar_texto(texto)
    return "".join(
        ALFABETO[(ord(caractere) - ord("A") + chave) % TAMANHO_ALFABETO]
        if caractere != " " else " "
        for caractere in preparado
    )


def cifrar_cesar(texto_claro: str, chave: int) -> str:
    """Desloca as letras da mensagem, preservando os espaços."""
    return _deslocar(texto_claro, chave)


def decifrar_cesar(texto_cifrado: str, chave: int) -> str:
    """Desfaz o deslocamento da mesma chave."""
    return _deslocar(texto_cifrado, -chave)
