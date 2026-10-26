"""Controladores e rotas da aplicação da livraria."""

from flask import Blueprint, jsonify, request

from models.livraria import (
    consultar_horario,
    consultar_livro,
    consultar_localizacao,
    consultar_disponibilidade_loja,
    listar_livros,
    pesquisar_livros,
    recomendar_livros,
)

livraria_bp = Blueprint("livraria", __name__)


@livraria_bp.get("/api/livros")
def api_livros():
    """Lista ou pesquisa livros."""
    busca = request.args.get("q", "")

    livros = (
        pesquisar_livros(busca)
        if busca.strip()
        else listar_livros()
    )

    return jsonify({"livros": livros})


@livraria_bp.get("/api/livros/<path:titulo>")
def api_livro(titulo):
    """Consulta os dados de um livro."""
    livro = consultar_livro(titulo)

    if livro is None:
        return jsonify({"erro": "Livro não encontrado."}), 404

    return jsonify(livro)


@livraria_bp.get("/api/livros/<path:titulo>/disponibilidade")
def api_disponibilidade(titulo):
    """Consulta a disponibilidade de um livro."""
    livro = consultar_livro(titulo)

    if livro is None:
        return jsonify({"erro": "Livro não encontrado."}), 404

    loja = request.args.get("loja")

    if loja:
        disponivel = consultar_disponibilidade_loja(
            titulo, loja
        )
    else:
        disponivel = livro["disponivel"]

    return jsonify({
        "disponivel": disponivel,
        "loja": loja,
    })


@livraria_bp.get("/api/horario")
def api_horario():
    """Consulta o horário de funcionamento."""
    return jsonify({"horario": consultar_horario()})


@livraria_bp.get("/api/localizacao")
def api_localizacao():
    """Consulta a localização da livraria."""
    return jsonify({"localizacao": consultar_localizacao()})


@livraria_bp.get("/api/recomendacoes")
def api_recomendacoes():
    """Retorna os livros recomendados."""
    return jsonify({"livros": recomendar_livros()})
