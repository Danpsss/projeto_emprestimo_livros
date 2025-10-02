class View:
    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_estudantes(self, estudantes):
        print("\n--- Estudantes ---")
        for e in estudantes:
            print(e)

    def listar_livros(self, livros):
        print("\n--- Livros ---")
        for l in livros:
            print(l)

    def listar_emprestimos(self, emprestimos):
        print("\n--- Empréstimos ---")
        for emp in emprestimos:
            print(emp)