import unittest
import numpy as np

from minhas_cifras import cifra_hill, decifra_hill, matriz_inversa_modular, validar_chave_hill
from test_cifras import matriz_sugerida


class TestHillMatriz(unittest.TestCase):
    def test_escolha_das_dimensoes(self):
        for dimensao in (2, 3, 4, 6, 8):
            with self.subTest(dimensao=dimensao):
                chave = matriz_sugerida(dimensao)
                self.assertEqual(chave.shape, (dimensao, dimensao))
                identidade = np.eye(dimensao, dtype=int)
                inversa = matriz_inversa_modular(chave)
                np.testing.assert_array_equal((chave @ inversa) % 26, identidade)
                original = "TRANSFERIRDOCUMENTOPARASERVIDORCENTRAL"
                cifrado = cifra_hill(original, chave)
                recuperado = decifra_hill(cifrado, chave)
                self.assertEqual(recuperado, original + "X" * (-len(original) % dimensao))

    def test_chave_invalida(self):
        for chave in ([[2, 0], [0, 2]], [[1, 2, 3]], [[1.5, 0], [0, 1]]):
            with self.subTest(chave=chave), self.assertRaises(ValueError):
                validar_chave_hill(chave)

    def test_valor_grande_e_determinante_exato(self):
        chave = [[26000001, 26000000], [26000000, 26000001]]
        self.assertEqual(validar_chave_hill(chave), 1)
        self.assertEqual(decifra_hill(cifra_hill("ABC", chave), chave), "ABCX")


if __name__ == "__main__":
    unittest.main()
