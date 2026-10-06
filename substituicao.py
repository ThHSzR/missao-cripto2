def substituicao_cifrar(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave = chave.upper()

    if len(chave) != 26:
        raise ValueError("A chave deve possuir exatamente 26 letras.")

    if len(set(chave)) != 26:
        raise ValueError("A chave não pode possuir letras repetidas.")

    resultado = ""

    for caractere in texto:
        if caractere.isalpha():
            maiusculo = caractere.isupper()

            indice = alfabeto.index(caractere.upper())
            novo_caractere = chave[indice]

            if not maiusculo:
                novo_caractere = novo_caractere.lower()

            resultado += novo_caractere
        else:
            resultado += caractere

    return resultado


def substituicao_decifrar(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave = chave.upper()

    if len(chave) != 26:
        raise ValueError("A chave deve possuir exatamente 26 letras.")

    if len(set(chave)) != 26:
        raise ValueError("A chave não pode possuir letras repetidas.")

    resultado = ""

    for caractere in texto:
        if caractere.isalpha():
            maiusculo = caractere.isupper()

            indice = chave.index(caractere.upper())
            novo_caractere = alfabeto[indice]

            if not maiusculo:
                novo_caractere = novo_caractere.lower()

            resultado += novo_caractere
        else:
            resultado += caractere

    return resultado
