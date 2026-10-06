from afim import cifrar_afim, decifrar_afim
from vigenere import cifrar_vigenere, decifrar_vigenere


def testar_cifra_afim():
    print("=" * 60)
    print("TESTE DA CIFRA AFIM")
    print("=" * 60)

    texto_original = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
    # Na cifra afim, 'a' precisa ser coprimo com 26 (ex: 5, 7, 11, 15, etc.) e 'b' é o deslocamento (ex: 8)
    a = 5
    b = 8

    print(f"Texto Claro:  {texto_original}")
    print(f"Chaves:       a = {a}, b = {b}")

    try:
        cifrado = cifrar_afim(texto_original, a, b)
        print(f"Texto Cifrado: {cifrado}")

        decifrado = decifrar_afim(cifrado, a, b)
        print(f"Texto Decifrado: {decifrado}")

        assert texto_original == decifrado, "Erro: O texto decifrado é diferente do original!"
        print("Sucesso! A decifragem recuperou o texto perfeitamente.\n")
    except Exception as e:
        print(f"Erro durante o teste da Cifra Afim: {e}\n")


def testar_cifra_vigenere():
    print("=" * 60)
    print("TESTE DA CIFRA DE VIGENÈRE")
    print("=" * 60)

    texto_original = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
    chave = "TECHSECURE"

    print(f"Texto Claro:  {texto_original}")
    print(f"Chave:        {chave}")

    try:
        cifrado = cifrar_vigenere(texto_original, chave)
        print(f"Texto Cifrado: {cifrado}")

        decifrado = decifrar_vigenere(cifrado, chave)
        print(f"Texto Decifrado: {decifrado}")

        assert texto_original == decifrado, "Erro: O texto decifrado é diferente do original!"
        print("Sucesso! A decifragem recuperou o texto perfeitamente.\n")
    except Exception as e:
        print(f"Erro durante o teste da Cifra de Vigenère: {e}\n")


if __name__ == "__main__":
    print("Iniciando testes da Missão 2 - Criptografia Clássica\n")
    testar_cifra_afim()
    testar_cifra_vigenere()