import unittest
from calculadora import adicionar, subtrair, multiplicar, dividir, porcentagem


class TestCalculadora(unittest.TestCase):
    """Testes automatizados para validar todas as operações da calculadora."""

    def test_adicionar(self):
        self.assertEqual(adicionar(10, 5), 15)
        self.assertEqual(adicionar(-4, 9), 5)
        self.assertAlmostEqual(adicionar(2.5, 3.2), 5.7)

    def test_subtrair(self):
        self.assertEqual(subtrair(20, 8), 12)
        self.assertEqual(subtrair(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(6, 7), 42)
        self.assertEqual(multiplicar(12.5, 4), 50.0)
        self.assertEqual(multiplicar(99, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(7, 2), 3.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_porcentagem(self):
        self.assertEqual(porcentagem(200, 15), 30.0)
        self.assertEqual(porcentagem(50, 50), 25.0)
        self.assertEqual(porcentagem(150, 10), 15.0)
        self.assertEqual(porcentagem(80, 0), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
