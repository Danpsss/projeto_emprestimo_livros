from view_livro import View
from control_livro import Controller

def main():
    view = View()
    controller = Controller(view)

    controller.adicionar_estudante(1, "Ana")
    controller.adicionar_estudante(2, "João")

    controller.adicionar_livro(101, "Python Básico")
    controller.adicionar_livro(102, "Engenharia de Software")

    controller.realizar_emprestimo(1, 101)
    controller.realizar_emprestimo(2, 101)  # tenta emprestar livro já emprestado

    controller.listar_tudo()

if __name__ == "__main__":
    main()