from model_livro import Estudante, Livro, Emprestimo
from view_livro import View

class Controller:
    def __init__(self, view: View):
        self.view = view
        self.estudantes = []
        self.livros = []
        self.emprestimos = []

    def adicionar_estudante(self, id, nome):
        estudante = Estudante(id, nome)
        self.estudantes.append(estudante)
        self.view.mostrar_mensagem(f"Estudante '{nome}' adicionado.")

    def adicionar_livro(self, id, titulo):
        livro = Livro(id, titulo)
        self.livros.append(livro)
        self.view.mostrar_mensagem(f"Livro '{titulo}' adicionado.")

    def realizar_emprestimo(self, id_estudante, id_livro):
        estudante = next((e for e in self.estudantes if e.id == id_estudante), None)
        livro = next((l for l in self.livros if l.id == id_livro), None)

        if not estudante or not livro:
            self.view.mostrar_mensagem("Estudante ou livro não encontrado.")
            return

        try:
            emprestimo = Emprestimo(estudante, livro)
            self.emprestimos.append(emprestimo)
            self.view.mostrar_mensagem(f"Empréstimo realizado: {emprestimo}")
        except ValueError as e:
            self.view.mostrar_mensagem(str(e))

    def listar_tudo(self):
        self.view.listar_estudantes(self.estudantes)
        self.view.listar_livros(self.livros)
        self.view.listar_emprestimos(self.emprestimos)