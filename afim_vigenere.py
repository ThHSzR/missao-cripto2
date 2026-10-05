"""
Módulo de Cifras Clássicas - Projeto SecureDocs
Autora: Marini Luzia
Contém a implementação interativa das cifras Afim e Vigenère.
"""

def mdc(a: int, b: int) -> int:
    """Calcula o Máximo Divisor Comum (MDC) usando o Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def inverso_modular(a: int, m: int) -> int:
    """Calcula o inverso multiplicativo modular de a módulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"O inverso modular para a={a} e m={m} não existe (m, a não são coprimos).")

class CifraAfim:
    @staticmethod
    def cifrar(texto: str, a: int, b: int) -> str:
        if mdc(a, 26) != 1:
            raise ValueError(f"A chave 'a' ({a}) deve ser coprimo de 26.")

        resultado = []
        for char in texto.upper():
            if 'A' <= char <= 'Z':
                x = ord(char) - ord('A')
                cifrado = (a * x + b) % 26
                resultado.append(chr(cifrado + ord('A')))
            else:
                resultado.append(char) # Mantém espaços e pontuação
        return "".join(resultado)

    @staticmethod
    def decifrar(texto_cifrado: str, a: int, b: int) -> str:
        a_inv = inverso_modular(a, 26)
        resultado = []
        for char in texto_cifrado.upper():
            if 'A' <= char <= 'Z':
                y = ord(char) - ord('A')
                decifrado = (a_inv * (y - b)) % 26
                resultado.append(chr(decifrado + ord('A')))
            else:
                resultado.append(char)
        return "".join(resultado)


class CifraVigenere:
    @staticmethod
    def _ajustar_chave(texto: str, chave: str) -> str:
        chave = chave.upper()
        chave_ajustada = []
        j = 0
        for char in texto.upper():
            if 'A' <= char <= 'Z':
                chave_ajustada.append(chave[j % len(chave)])
                j += 1
            else:
                chave_ajustada.append(char)
        return "".join(chave_ajustada)

    @staticmethod
    def cifrar(texto: str, chave: str) -> str:
        if not chave.isalpha():
            raise ValueError("A chave de Vigenère deve conter apenas letras.")
        chave_expandida = CifraVigenere._ajustar_chave(texto, chave)
        resultado = []
        for p, k in zip(texto.upper(), chave_expandida):
            if 'A' <= p <= 'Z':
                p_num = ord(p) - ord('A')
                k_num = ord(k) - ord('A')
                cifrado = (p_num + k_num) % 26
                resultado.append(chr(cifrado + ord('A')))
            else:
                resultado.append(p)
        return "".join(resultado)

    @staticmethod
    def decifrar(texto_cifrado: str, chave: str) -> str:
        if not chave.isalpha():
            raise ValueError("A chave de Vigenère deve conter apenas letras.")
        chave_expandida = CifraVigenere._ajustar_chave(texto_cifrado, chave)
        resultado = []
        for c, k in zip(texto_cifrado.upper(), chave_expandida):
            if 'A' <= c <= 'Z':
                c_num = ord(c) - ord('A')
                k_num = ord(k) - ord('A')
                decifrado = (c_num - k_num) % 26
                resultado.append(chr(decifrado + ord('A')))
            else:
                resultado.append(c)
        return "".join(resultado)


if __name__ == "__main__":
    print("==========================================")
    print("       SECUREDOCS - MÓDULO DE CIFRAS      ")
    print("==========================================")

    while True:
        print("\nEscolha a cifra:")
        print("1. Cifra Afim")
        print("2. Cifra de Vigenère")
        print("0. Sair")

        opcao = input("Opção desejada: ").strip()

        if opcao == "0":
            print("Encerrando o programa...")
            break

        elif opcao == "1":
            print("\n--- CIFRA AFIM ---")
            acao = input("Deseja (C)ifrar ou (D)ecifrar? ").strip().upper()
            texto = input("Digite a mensagem: ")
            try:
                a = int(input("Digite a chave 'a' (inteiro coprimo de 26, ex: 5): "))
                b = int(input("Digite a chave 'b' (inteiro, ex: 8): "))

                if acao == "C":
                    resultado = CifraAfim.cifrar(texto, a, b)
                    print(f"\n[Texto Cifrado]: {resultado}")
                elif acao == "D":
                    resultado = CifraAfim.decifrar(texto, a, b)
                    print(f"\n[Texto Decifrado]: {resultado}")
                else:
                    print("Opção inválida!")
            except Exception as e:
                print(f"[Erro]: {e}")

        elif opcao == "2":
            print("\n--- CIFRA DE VIGENÈRE ---")
            acao = input("Deseja (C)ifrar ou (D)ecifrar? ").strip().upper()
            texto = input("Digite a mensagem: ")
            chave = input("Digite a palavra-chave (ex: SECURE): ")
            try:
                if acao == "C":
                    resultado = CifraVigenere.cifrar(texto, chave)
                    print(f"\n[Texto Cifrado]: {resultado}")
                elif acao == "D":
                    resultado = CifraVigenere.decifrar(texto, chave)
                    print(f"\n[Texto Decifrado]: {resultado}")
                else:
                    print("Opção inválida!")
            except Exception as e:
                print(f"[Erro]: {e}")
        else:
            print("Opção inválida! Escolha 1, 2 ou 0.")