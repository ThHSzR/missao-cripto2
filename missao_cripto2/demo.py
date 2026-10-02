"""Execute com: python -m missao_cripto2.demo"""

from .cesar import cifrar_cesar, decifrar_cesar


def main() -> None:
    mensagem = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
    chave = 3
    cifrado = cifrar_cesar(mensagem, chave)
    recuperado = decifrar_cesar(cifrado, chave)

    print(f"Texto claro:    {mensagem}")
    print(f"Chave:          {chave}")
    print(f"Texto cifrado:  {cifrado}")
    print(f"Texto decifrado:{'  '}{recuperado}")


if __name__ == "__main__":
    main()
