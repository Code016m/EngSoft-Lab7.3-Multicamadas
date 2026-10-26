"""Testes automatizados das funções da livraria."""

import unittest

from models.livraria import (
    pesquisar_livros,
    consultar_livro,
    consultar_disponibilidade,
    consultar_disponibilidade_loja,
    consultar_preco,
    consultar_horario,
    consultar_localizacao,
    recomendar_livros,
)


class TestLivraria(unittest.TestCase):

    def test_pesquisar_livro(self):
        resultado = pesquisar_livros("Dom Casmurro")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

    def test_pesquisar_por_autor(self):
        resultado = pesquisar_livros("Machado de Assis")

        self.assertGreaterEqual(len(resultado), 2)

    def test_consultar_informacoes_livro(self):
        livro = consultar_livro("Dom Casmurro")

        self.assertIsNotNone(livro)
        self.assertEqual(livro["titulo"], "Dom Casmurro")
        self.assertEqual(livro["autor"], "Machado de Assis")
        self.assertEqual(livro["preco"], 30.0)

    def test_livro_inexistente(self):
        self.assertIsNone(consultar_livro("Livro Inexistente"))

    def test_consultar_disponibilidade(self):
        self.assertTrue(
            consultar_disponibilidade("Dom Casmurro")
        )

    def test_livro_indisponivel(self):
        self.assertFalse(
            consultar_disponibilidade("Vidas Secas")
        )

    def test_consultar_disponibilidade_loja(self):
        resultado = consultar_disponibilidade_loja(
            "Dom Casmurro",
            "Loja Centro",
        )

        self.assertTrue(resultado)

    def test_consultar_preco(self):
        self.assertEqual(
            consultar_preco("Dom Casmurro"),
            30.0,
        )

    def test_preco_livro_inexistente(self):
        self.assertIsNone(
            consultar_preco("Livro Inexistente")
        )

    def test_consultar_horario(self):
        self.assertIsNotNone(consultar_horario())

    def test_consultar_localizacao(self):
        self.assertIsNotNone(consultar_localizacao())

    def test_recomendar_livros(self):
        resultado = recomendar_livros()

        self.assertGreater(len(resultado), 0)

        for livro in resultado:
            self.assertTrue(livro["disponivel"])


if __name__ == "__main__":
    unittest.main()
