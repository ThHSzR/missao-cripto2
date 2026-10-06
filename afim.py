# Importando as funções matemáticas da Missão 1
from mdc import calcular_mdc
from inverso_multiplicativo import inverso_multiplicativo


def cifrar_afim(texto: str, a: int, b: int) -> str:
    """Cifra um texto usando a Cifra Afim, preservando maiúsculas/minúsculas e caracteres especiais."""
    if calcular_mdc(a, 26) != 1:
        raise ValueError(f"A chave 'a' ({a}) deve ser coprimo com 26 (MDC deve ser 1).")

    texto_cifrado = []
    for char in texto:
        if 'A' <= char <= 'Z':
            x = ord(char) - ord('A')
            c = (a * x + b) % 26
            texto_cifrado.append(chr(c + ord('A')))
        elif 'a' <= char <= 'z':
            x = ord(char) - ord('a')
            c = (a * x + b) % 26
            texto_cifrado.append(chr(c + ord('a')))
        else:
            texto_cifrado.append(char)  # Mantém espaços, acentos e pontuações
    return "".join(texto_cifrado)


def decifrar_afim(texto_cifrado: str, a: int, b: int) -> str:
    """Decifra um texto usando a Cifra Afim, preservando maiúsculas/minúsculas."""
    if calcular_mdc(a, 26) != 1:
        raise ValueError(f"A chave 'a' ({a}) não possui inverso módulo 26.")

    a_inv = inverso_multiplicativo(a, 26)
    if a_inv is None:
        raise ValueError(f"Não foi encontrado inverso multiplicativo para a={a} mod 26.")

    texto_claro = []
    for char in texto_cifrado:
        if 'A' <= char <= 'Z':
            y = ord(char) - ord('A')
            p = (a_inv * (y - b)) % 26
            texto_claro.append(chr(p + ord('A')))
        elif 'a' <= char <= 'z':
            y = ord(char) - ord('a')
            p = (a_inv * (y - b)) % 26
            texto_claro.append(chr(p + ord('a')))
        else:
            texto_claro.append(char)
    return "".join(texto_claro)