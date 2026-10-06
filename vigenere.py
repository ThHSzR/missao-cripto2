def cifrar_vigenere(texto: str, chave: str) -> str:
    """Cifra um texto usando a Cifra de Vigenère, preservando maiúsculas/minúsculas."""
    if not chave:
        raise ValueError("A chave não pode estar vazia.")

    resultado = []
    chave = chave.upper()
    i = 0

    for char in texto:
        if 'A' <= char <= 'Z':
            p = ord(char) - ord('A')
            k = ord(chave[i % len(chave)]) - ord('A')
            c = (p + k) % 26
            resultado.append(chr(c + ord('A')))
            i += 1
        elif 'a' <= char <= 'z':
            p = ord(char) - ord('a')
            k = ord(chave[i % len(chave)]) - ord('A')
            c = (p + k) % 26
            resultado.append(chr(c + ord('a')))
            i += 1
        else:
            resultado.append(char)
    return "".join(resultado)


def decifrar_vigenere(texto_cifrado: str, chave: str) -> str:
    """Decifra um texto usando a Cifra de Vigenère, preservando maiúsculas/minúsculas."""
    if not chave:
        raise ValueError("A chave não pode estar vazia.")

    resultado = []
    chave = chave.upper()
    i = 0

    for char in texto_cifrado:
        if 'A' <= char <= 'Z':
            c = ord(char) - ord('A')
            k = ord(chave[i % len(chave)]) - ord('A')
            p = (c - k) % 26
            resultado.append(chr(p + ord('A')))
            i += 1
        elif 'a' <= char <= 'z':
            c = ord(char) - ord('a')
            k = ord(chave[i % len(chave)]) - ord('A')
            p = (c - k) % 26
            resultado.append(chr(p + ord('a')))
            i += 1
        else:
            resultado.append(char)
    return "".join(resultado)