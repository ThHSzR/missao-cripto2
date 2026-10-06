"""Ponto de entrada unificado da Missao Cripto 2.

O arquivo integra todas as implementacoes existentes no repositorio: cifras
classicas, criptoanalise, matematica modular e o exemplo conceitual. Execute
``python main.py`` para abrir o menu ou ``python main.py --demo`` para rodar
uma demonstracao completa sem entrada do usuario.
"""

from __future__ import annotations

import argparse
import string
from collections.abc import Callable

import numpy as np

from afim import cifrar_afim, decifrar_afim
from analise_frequencia import quebrar_cesar_por_frequencia
from cesar import cesar_cifrar, cesar_decifrar
from comparacao_cifras import imprimir_comparacao
from euclides_estendido import euclides_estendido
from forca_bruta import quebrar_afim, quebrar_cesar
from frequencia_pt import contar_frequencias, pontuar
from inverso_multiplicativo import inverso_multiplicativo
from mdc import calcular_mdc, coprimos
from minhas_cifras import (
    cifra_fluxo,
    cifra_hill,
    cifra_transposicao,
    decifra_fluxo,
    decifra_hill,
    decifra_transposicao,
    validar_chave_hill,
)
from missao_cripto2.exemplo_conceitual import calcular_exemplo
from missao_cripto2.matematica_missao1 import aritmetica_modular
from substituicao import substituicao_cifrar, substituicao_decifrar
from vigenere import cifrar_vigenere, decifrar_vigenere


MENSAGEM_PADRAO = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
CHAVE_SUBSTITUICAO = "QWERTYUIOPASDFGHJKLZXCVBNM"
MATRIZ_HILL_PADRAO = np.array(
    [[6, 24, 1], [13, 16, 10], [20, 17, 15]], dtype=int
)
ALFABETO = string.ascii_uppercase


def _titulo(texto: str) -> None:
    print(f"\n{'=' * 68}\n{texto}\n{'=' * 68}")


def _validar_chave_alfabetica(chave: str, nome: str = "chave") -> str:
    """Aceita somente letras ASCII, evitando resultados indefinidos nos modulos."""
    if not chave or any(letra not in string.ascii_letters for letra in chave):
        raise ValueError(f"A {nome} deve conter somente letras de A a Z.")
    return chave


def _validar_chave_substituicao(chave: str) -> str:
    chave = chave.upper()
    if len(chave) != 26 or set(chave) != set(ALFABETO):
        raise ValueError(
            "A chave de substituicao deve ser uma permutacao das 26 letras A-Z."
        )
    return chave


def _validar_chave_transposicao(chave: str) -> str:
    if not chave:
        raise ValueError("A chave de transposicao nao pode estar vazia.")
    return chave.upper()


def _ler_inteiro(mensagem: str, padrao: int | None = None) -> int:
    sufixo = f" [{padrao}]" if padrao is not None else ""
    while True:
        entrada = input(f"{mensagem}{sufixo}: ").strip()
        if not entrada and padrao is not None:
            return padrao
        try:
            return int(entrada)
        except ValueError:
            print("Informe um numero inteiro.")


def _ler_acao() -> str:
    while True:
        acao = input("Escolha (C)ifrar ou (D)ecifrar: ").strip().upper()
        if acao in {"C", "D"}:
            return acao
        print("Acao invalida. Digite C ou D.")


def _executar_substituicao(
    nome: str,
    cifrar: Callable[..., str],
    decifrar: Callable[..., str],
    pedir_chave: Callable[[], tuple],
) -> None:
    """Fluxo comum das cifras que preservam espacos e pontuacao."""
    _titulo(nome)
    acao = _ler_acao()
    texto = input("Texto: ")
    chave = pedir_chave()
    resultado = cifrar(texto, *chave) if acao == "C" else decifrar(texto, *chave)
    print(f"Resultado: {resultado}")


def _menu_cesar() -> None:
    _executar_substituicao(
        "CIFRA DE CESAR",
        cesar_cifrar,
        cesar_decifrar,
        lambda: (_ler_inteiro("Deslocamento", 3),),
    )


def _menu_substituicao() -> None:
    def chave() -> tuple[str]:
        valor = input(
            f"Permutacao de A-Z [{CHAVE_SUBSTITUICAO}]: "
        ).strip() or CHAVE_SUBSTITUICAO
        return (_validar_chave_substituicao(valor),)

    _executar_substituicao(
        "SUBSTITUICAO MONOALFABETICA",
        substituicao_cifrar,
        substituicao_decifrar,
        chave,
    )


def _menu_afim() -> None:
    def chave() -> tuple[int, int]:
        a = _ler_inteiro("Chave multiplicativa a (coprima com 26)", 5)
        b = _ler_inteiro("Deslocamento b", 8)
        if not coprimos(a, 26):
            raise ValueError("A chave a deve ser coprima com 26.")
        return a, b

    _executar_substituicao(
        "CIFRA AFIM", cifrar_afim, decifrar_afim, chave
    )


def _menu_vigenere() -> None:
    def chave() -> tuple[str]:
        valor = input("Palavra-chave [SECURE]: ").strip() or "SECURE"
        return (_validar_chave_alfabetica(valor),)

    _executar_substituicao(
        "CIFRA DE VIGENERE", cifrar_vigenere, decifrar_vigenere, chave
    )


def _ler_matriz_hill() -> np.ndarray:
    dimensao = _ler_inteiro("Dimensao da matriz (2 a 8)", 3)
    if not 2 <= dimensao <= 8:
        raise ValueError("A dimensao deve estar entre 2 e 8.")

    if dimensao == 3:
        sugestao = MATRIZ_HILL_PADRAO.copy()
    else:
        sugestao = np.eye(dimensao, dtype=int)
        for indice in range(dimensao - 1):
            sugestao[indice, indice + 1] = 1

    print(f"Matriz sugerida:\n{sugestao}")
    usar = input("Usar a matriz sugerida? [S/n]: ").strip().lower()
    if usar not in {"n", "nao", "não"}:
        return sugestao

    linhas: list[list[int]] = []
    for indice in range(dimensao):
        valores = input(
            f"Linha {indice + 1} ({dimensao} inteiros separados por espaco): "
        ).split()
        if len(valores) != dimensao:
            raise ValueError(f"Cada linha deve ter {dimensao} inteiros.")
        linhas.append([int(valor) for valor in valores])

    matriz = np.array(linhas, dtype=object)
    validar_chave_hill(matriz)
    return matriz


def _menu_hill() -> None:
    _titulo("CIFRA DE HILL")
    acao = _ler_acao()
    texto = input("Texto: ")
    matriz = _ler_matriz_hill()
    resultado = cifra_hill(texto, matriz) if acao == "C" else decifra_hill(texto, matriz)
    print(f"Resultado: {resultado}")
    if acao == "D":
        print("Observacao: X no final pode ser preenchimento do ultimo bloco.")


def _menu_transposicao() -> None:
    def decifrar_validado(texto: str, chave_transposicao: str) -> str:
        if len(texto) % len(chave_transposicao):
            raise ValueError(
                "O texto cifrado deve preencher linhas completas para essa chave."
            )
        return decifra_transposicao(texto, chave_transposicao)

    def chave() -> tuple[str]:
        valor = input("Palavra-chave [SECURE]: ").strip() or "SECURE"
        return (_validar_chave_transposicao(valor),)

    _executar_substituicao(
        "TRANSPOSICAO COLUNAR",
        cifra_transposicao,
        decifrar_validado,
        chave,
    )


def _menu_fluxo() -> None:
    _titulo("CIFRA DE FLUXO XOR")
    acao = _ler_acao()
    if acao == "C":
        texto = input("Texto: ")
        cifrado, chave = cifra_fluxo(texto)
        print(f"Cifrado (hex): {cifrado.hex()}")
        print(f"Chave (hex)  : {chave.hex()}")
        print("Guarde a chave: sem ela nao e possivel recuperar a mensagem.")
        return

    cifrado = bytes.fromhex(input("Texto cifrado em hexadecimal: ").strip())
    chave = bytes.fromhex(input("Chave em hexadecimal: ").strip())
    if len(chave) < len(cifrado):
        raise ValueError("A chave deve ter ao menos o tamanho do texto cifrado.")
    print(f"Resultado: {decifra_fluxo(cifrado, chave)}")


def _decifrar_afim_com_tupla(texto: str, chave: tuple[int, int]) -> str:
    return decifrar_afim(texto, *chave)


def _menu_criptoanalise() -> None:
    _titulo("CRIPTOANALISE")
    print("1. Forca bruta de Cesar")
    print("2. Forca bruta da cifra Afim")
    print("3. Analise de frequencia de Cesar")
    print("4. Frequencias e pontuacao de um texto")
    opcao = input("Opcao: ").strip()
    texto = input("Texto cifrado (ou texto para analisar): ")

    if opcao == "1":
        chave, claro = quebrar_cesar(texto, cesar_decifrar)
        print(f"Melhor chave: {chave}\nTexto provavel: {claro}")
    elif opcao == "2":
        chave, claro = quebrar_afim(texto, _decifrar_afim_com_tupla)
        print(f"Melhor chave (a, b): {chave}\nTexto provavel: {claro}")
    elif opcao == "3":
        chave, claro = quebrar_cesar_por_frequencia(texto, cesar_decifrar)
        print(f"Chave estimada: {chave}\nTexto provavel: {claro}")
        print("A estimativa por frequencia e mais confiavel em textos longos.")
    elif opcao == "4":
        frequencias = contar_frequencias(texto)
        usadas = sorted(
            ((letra, valor) for letra, valor in frequencias.items() if valor),
            key=lambda item: item[1],
            reverse=True,
        )
        print("Frequencias: " + ", ".join(f"{l}={v:.1f}%" for l, v in usadas))
        print(f"Qui-quadrado para portugues: {pontuar(texto):.2f} (menor e melhor)")
    else:
        raise ValueError("Opcao de criptoanalise invalida.")


def _menu_matematica() -> None:
    _titulo("MATEMATICA MODULAR")
    print("1. MDC e coprimalidade")
    print("2. Algoritmo estendido de Euclides")
    print("3. Inverso multiplicativo")
    print("4. Soma, subtracao e multiplicacao modulares")
    print("5. Exemplo conceitual de cifragem")
    opcao = input("Opcao: ").strip()

    if opcao == "1":
        a, b = _ler_inteiro("a"), _ler_inteiro("b")
        print(f"MDC({a}, {b}) = {calcular_mdc(a, b)}")
        print(f"Sao coprimos: {'sim' if coprimos(a, b) else 'nao'}")
    elif opcao == "2":
        a, b = _ler_inteiro("a"), _ler_inteiro("b")
        divisor, x, y = euclides_estendido(a, b)
        print(f"mdc={divisor}, x={x}, y={y}; {a}*{x} + {b}*{y} = {divisor}")
    elif opcao == "3":
        a, modulo = _ler_inteiro("a"), _ler_inteiro("modulo")
        print(f"Inverso de {a} mod {modulo}: {inverso_multiplicativo(a, modulo)}")
    elif opcao == "4":
        a = _ler_inteiro("a")
        b = _ler_inteiro("b")
        modulo = _ler_inteiro("modulo", 26)
        print(aritmetica_modular(a, b, modulo))
    elif opcao == "5":
        indice = _ler_inteiro("Indice claro", 19)
        chave = _ler_inteiro("Chave", 3)
        exemplo = calcular_exemplo(indice, chave)
        print(
            f"{exemplo.indice_claro} + {exemplo.chave} mod {exemplo.modulo} "
            f"= {exemplo.indice_cifrado}; recuperado = {exemplo.indice_recuperado}"
        )
    else:
        raise ValueError("Opcao matematica invalida.")


def demonstracao_completa() -> None:
    """Executa e confere todas as cifras e tecnicas sem solicitar entrada."""
    texto = MENSAGEM_PADRAO
    _titulo("DEMONSTRACAO COMPLETA - MISSAO CRIPTO 2")
    print(f"Texto original: {texto}")

    exemplos: list[tuple[str, str, str]] = []

    cifrado = cesar_cifrar(texto, 7)
    exemplos.append(("Cesar (k=7)", cifrado, cesar_decifrar(cifrado, 7)))

    cifrado = substituicao_cifrar(texto, CHAVE_SUBSTITUICAO)
    exemplos.append(
        (
            "Substituicao",
            cifrado,
            substituicao_decifrar(cifrado, CHAVE_SUBSTITUICAO),
        )
    )

    cifrado = cifrar_afim(texto, 5, 8)
    exemplos.append(("Afim (a=5, b=8)", cifrado, decifrar_afim(cifrado, 5, 8)))

    cifrado = cifrar_vigenere(texto, "TECHSECURE")
    exemplos.append(
        ("Vigenere (TECHSECURE)", cifrado, decifrar_vigenere(cifrado, "TECHSECURE"))
    )

    cifrado = cifra_hill(texto, MATRIZ_HILL_PADRAO)
    exemplos.append(("Hill (3x3)", cifrado, decifra_hill(cifrado, MATRIZ_HILL_PADRAO)))

    cifrado = cifra_transposicao(texto, "SECURE")
    exemplos.append(
        ("Transposicao (SECURE)", cifrado, decifra_transposicao(cifrado, "SECURE"))
    )

    for nome, cifrado, recuperado in exemplos:
        print(f"\n[{nome}]\nCifrado   : {cifrado}\nRecuperado: {recuperado}")

    for nome, _, recuperado in exemplos[:4]:
        if recuperado != texto:
            raise RuntimeError(f"Falha na verificacao de ida e volta: {nome}.")

    texto_sem_separadores = "".join(letra for letra in texto if letra in ALFABETO)
    for nome, _, recuperado in exemplos[4:]:
        if recuperado.rstrip("X") != texto_sem_separadores:
            raise RuntimeError(f"Falha na verificacao de ida e volta: {nome}.")

    cifrado_bytes, chave_bytes = cifra_fluxo(texto)
    recuperado_fluxo = decifra_fluxo(cifrado_bytes, chave_bytes)
    if recuperado_fluxo != texto:
        raise RuntimeError("Falha na verificacao de ida e volta: fluxo XOR.")
    print(
        "\n[Fluxo XOR / OTP]"
        f"\nCifrado (hex): {cifrado_bytes.hex()}"
        f"\nChave (hex)  : {chave_bytes.hex()}"
        f"\nRecuperado   : {recuperado_fluxo}"
    )

    cesar_cifrado = cesar_cifrar(texto, 7)
    chave_cesar, claro_cesar = quebrar_cesar(cesar_cifrado, cesar_decifrar)
    afim_cifrado = cifrar_afim(texto, 5, 8)
    chave_afim, claro_afim = quebrar_afim(afim_cifrado, _decifrar_afim_com_tupla)
    print(
        "\n[Criptoanalise por forca bruta]"
        f"\nCesar: chave={chave_cesar}, texto={claro_cesar}"
        f"\nAfim : chave={chave_afim}, texto={claro_afim}"
    )

    texto_longo = (
        "A SEGURANCA DA INFORMACAO DEPENDE DE PROCESSOS PESSOAS E TECNOLOGIA "
        "A CRIPTOGRAFIA CLASSICA AJUDA A COMPREENDER OS PRINCIPIOS DE "
        "CONFIDENCIALIDADE E ANALISE DE FREQUENCIA "
    ) * 5
    chave_freq, _ = quebrar_cesar_por_frequencia(
        cesar_cifrar(texto_longo, 11), cesar_decifrar
    )
    print(f"Analise de frequencia (texto longo): chave estimada={chave_freq}")

    exemplo = calcular_exemplo(19, 3)
    print(
        "\n[Matematica modular]"
        f"\nMDC(48, 18)={calcular_mdc(48, 18)}; "
        f"inverso de 5 mod 26={inverso_multiplicativo(5, 26)}"
        f"\nExemplo T(19) + 3 mod 26 = {exemplo.indice_cifrado}; "
        f"recuperado={exemplo.indice_recuperado}"
    )

    print("\n[Comparacao das cifras]")
    imprimir_comparacao()


ACOES: dict[str, Callable[[], None]] = {
    "1": demonstracao_completa,
    "2": _menu_cesar,
    "3": _menu_substituicao,
    "4": _menu_afim,
    "5": _menu_vigenere,
    "6": _menu_hill,
    "7": _menu_transposicao,
    "8": _menu_fluxo,
    "9": _menu_criptoanalise,
    "10": _menu_matematica,
    "11": imprimir_comparacao,
}


def menu() -> None:
    while True:
        _titulo("SECUREDOCS - MISSAO 2: CRIPTOGRAFIA CLASSICA")
        print("1. Demonstracao completa")
        print("2. Cifra de Cesar")
        print("3. Substituicao monoalfabetica")
        print("4. Cifra Afim")
        print("5. Cifra de Vigenere")
        print("6. Cifra de Hill")
        print("7. Transposicao colunar")
        print("8. Cifra de fluxo XOR")
        print("9. Criptoanalise")
        print("10. Matematica modular")
        print("11. Comparacao das cifras")
        print("0. Sair")
        opcao = input("Opcao: ").strip()
        if opcao == "0":
            print("Programa encerrado.")
            return

        acao = ACOES.get(opcao)
        if acao is None:
            print("Opcao invalida.")
            continue

        try:
            acao()
        except (ValueError, TypeError, UnicodeDecodeError) as erro:
            print(f"Erro: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nOperacao cancelada.")
            return

        input("\nPressione Enter para voltar ao menu...")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="executa todas as demonstracoes sem abrir o menu interativo",
    )
    argumentos = parser.parse_args(argv)
    demonstracao_completa() if argumentos.demo else menu()


if __name__ == "__main__":
    main()
