"""Verifica a conta do resumo e as condições de entrada do exemplo."""

import unittest

from missao_cripto2.exemplo_conceitual import calcular_exemplo
from missao_cripto2.matematica_missao1 import aritmetica_modular


class TestExemploConceitual(unittest.TestCase):
    def test_exemplo_da_apresentacao_usa_modulo_da_missao1(self) -> None:
        exemplo = calcular_exemplo(19, 3)
        self.assertEqual(exemplo.indice_cifrado, 22)
        self.assertEqual(exemplo.indice_recuperado, 19)
        self.assertEqual(aritmetica_modular(19, 3, 26)["soma"], 22)
        self.assertEqual(aritmetica_modular(22, 3, 26)["subtracao"], 19)

    def test_contorno_e_chave_negativa(self) -> None:
        exemplo = calcular_exemplo(0, -1)
        self.assertEqual((exemplo.indice_cifrado, exemplo.indice_recuperado), (25, 0))
        self.assertEqual(calcular_exemplo(25, 1).indice_cifrado, 0)

    def test_entradas_invalidas(self) -> None:
        for argumentos in ((26, 3, 26), (-1, 3, 26), (0, 3, 1)):
            with self.subTest(argumentos=argumentos), self.assertRaises(ValueError):
                calcular_exemplo(*argumentos)
        for argumentos in ((True, 3, 26), (19, 3.0, 26), (19, 3, False)):
            with self.subTest(argumentos=argumentos), self.assertRaises(TypeError):
                calcular_exemplo(*argumentos)


if __name__ == "__main__":
    unittest.main()
