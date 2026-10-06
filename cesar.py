def cesar_cifrar(texto, chave):
    resultado = ""

    for caractere in texto:
        if caractere.isalpha():
            inicio = ord('A') if caractere.isupper() else ord('a')

            novo_caractere = chr(
                (ord(caractere) - inicio + chave) % 26 + inicio
            )

            resultado += novo_caractere
        else:
            resultado += caractere

    return resultado


def cesar_decifrar(texto, chave):
    return cesar_cifrar(texto, -chave)
