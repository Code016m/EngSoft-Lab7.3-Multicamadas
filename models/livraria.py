"""Dados e consultas do catálogo da livraria."""

LIVROS = [
    {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "preco": 30.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "O Cortiço",
        "autor": "Aluísio Azevedo",
        "preco": 35.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "preco": 32.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "Grande Sertão: Veredas",
        "autor": "João Guimarães Rosa",
        "preco": 45.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "Capitães da Areia",
        "autor": "Jorge Amado",
        "preco": 38.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "A Hora da Estrela",
        "autor": "Clarice Lispector",
        "preco": 28.0,
        "disponivel": True,
        "lojas": {"Loja Centro": True},
    },
    {
        "titulo": "Vidas Secas",
        "autor": "Graciliano Ramos",
        "preco": 34.0,
        "disponivel": False,
        "lojas": {"Loja Centro": False},
    },
]

HORARIO_FUNCIONAMENTO = "Não informado."
LOCALIZACAO = "Não informada."


def listar_livros():
    """Retorna os livros cadastrados."""
    return [livro.copy() for livro in LIVROS]


def pesquisar_livros(termo):
    """Pesquisa por trecho do título ou do autor."""
    if not isinstance(termo, str) or not termo.strip():
        return []

    consulta = termo.strip().casefold()

    return [
        livro.copy()
        for livro in LIVROS
        if consulta in livro["titulo"].casefold()
        or consulta in livro["autor"].casefold()
    ]


def consultar_livro(titulo):
    """Retorna um livro ou None se não for encontrado."""
    if not isinstance(titulo, str):
        return None

    titulo = titulo.strip().casefold()

    for livro in LIVROS:
        if livro["titulo"].casefold() == titulo:
            return livro.copy()

    return None


def consultar_disponibilidade(titulo):
    """Verifica a disponibilidade geral de um livro."""
    livro = consultar_livro(titulo)
    return bool(livro and livro["disponivel"])


def consultar_disponibilidade_loja(titulo, loja):
    """Verifica a disponibilidade de um livro em uma loja."""
    livro = consultar_livro(titulo)

    if not livro or not isinstance(loja, str):
        return False

    disponibilidade = livro["lojas"].get(loja.strip())
    return bool(disponibilidade)


def consultar_preco(titulo):
    """Retorna o preço do livro ou None se não existir."""
    livro = consultar_livro(titulo)
    return livro["preco"] if livro else None


def consultar_horario():
    """Retorna o horário de funcionamento."""
    return HORARIO_FUNCIONAMENTO


def consultar_localizacao():
    """Retorna a localização da livraria."""
    return LOCALIZACAO


def recomendar_livros():
    """Retorna os livros disponíveis como recomendações."""
    return [
        livro.copy()
        for livro in LIVROS
        if livro["disponivel"]
    ]