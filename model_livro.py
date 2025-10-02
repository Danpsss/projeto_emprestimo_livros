class Estudante:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Estudante({self.id}, {self.nome})"


class Livro:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro({self.id}, {self.titulo}, {status})"


class Emprestimo:
    def __init__(self, estudante, livro):
        if not livro.disponivel:
            raise ValueError(f"O livro '{livro.titulo}' já está emprestado.")
        self.estudante = estudante
        self.livro = livro
        livro.disponivel = False

    def __str__(self):
        return f"Empréstimo({self.estudante.nome} -> {self.livro.titulo})"