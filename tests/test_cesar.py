"""Verifica a mensagem do enunciado e os limites da implementação."""

import unittest

from missao_cripto2 import cifrar_cesar, decifrar_cesar


MENSAGEM = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
CIFRADA = "WUDQVIHULU GRFXPHQWR SDUD VHUYLGRU FHQWUDO"


class TestCesar(unittest.TestCase):
    def test_vetor_da_missao(self) -> None:
        self.assertEqual(cifrar_cesar(MENSAGEM, 3), CIFRADA)
        self.assertEqual(decifrar_cesar(CIFRADA, 3), MENSAGEM)

    def test_contorno_do_alfabeto_e_chave_negativa(self) -> None:
        self.assertEqual(cifrar_cesar("AZ az", 1), "BA BA")
        self.assertEqual(cifrar_cesar("A Z", -1), "Z Y")
        self.assertEqual(cifrar_cesar("ABC", 29), cifrar_cesar("ABC", 3))

    def test_entrada_fora_do_alfabeto_nao_e_alterada_silenciosamente(self) -> None:
        with self.assertRaises(ValueError):
            cifrar_cesar("AÇÃO", 3)
        with self.assertRaises(ValueError):
            cifrar_cesar("OI!", 3)
        with self.assertRaises(TypeError):
            cifrar_cesar(MENSAGEM, True)


if __name__ == "__main__":
    unittest.main()
