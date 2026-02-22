import json
import os


class Livro:
    def __init__(self, titulo, autor, codigo, ano):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ano = ano
        self.status = "Disponivel"

    def converter_livros_para_dicionario(self):
        return {
            "Titulo": self.titulo,
            "Autor": self.autor,
            "Lancamento": self.ano,
            "Codigo": self.codigo,
            "Status": self.status
        }


class Usuario:
    def __init__(self, nome, id_usuario, senha, user_name):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []
        self.senha = senha
        self.user_name = user_name

    def converter_usuario_para_dicionario(self):
        return {
            "Nome": self.nome,
            "User_name": self.user_name,
            "ID_user": self.id_usuario,
            "Senha": self.senha,
            "Livros_emprestados": self.livros_emprestados
        }


class Biblioteca:
    def __init__(self):
        self.arquivo_livros = "Livros.json"
        self.arquivo_usuario = "Usuarios.json"

    def cadastro_livro(self):
        if os.path.exists(self.arquivo_livros):
            with open(self.arquivo_livros, "r") as arquivo:
                cadastrados = json.load(arquivo)
        else:
            cadastrados = {"Livros": []}

        print("Cadastro de livro")
        titulo = input("Titulo: ").title()
        autor = input("Autor: ").title()
        ano = int(input("Ano de Lançamento: "))
        if not os.path.exists(self.arquivo_livros):
            codigo = 1
        else:
            codigo = len(cadastrados["Livros"]) + 1

        livros = Livro(titulo, autor, codigo, ano)

        cadastrados["Livros"].append(livros.converter_livros_para_dicionario())

        with open(self.arquivo_livros, 'w') as arquivo:
            json.dump(cadastrados, arquivo, indent=4)

        print('Livro cadastrado com sucesso')
        input("Pressione qualquer tecla para voltar")

    def listar_livros(self):
        if not os.path.exists(self.arquivo_livros):
            print("Nenhuma livro encontrado\n")
            return

        with open(self.arquivo_livros, "r") as arquivo:
            livros_cadastrados = json.load(arquivo)

        if not livros_cadastrados['Livros']:
            print("Nenhum livro cadastrado")
            input("Pressione qualquer tecla para voltar")
            return

        print("\nListar Livros")
        for livro in livros_cadastrados["Livros"]:
            print(f"Código: #0{livro['Codigo']}")
            print(f"Título: {livro['Titulo']}")
            print(f"Autor: {livro['Autor']}")
            print(f"Lancamento: {livro['Lancamento']}")
            print(f"Status: {livro['Status']}")
            print("-" * 30)

    def cadastro_usuario(self):
        if os.path.exists(self.arquivo_usuario):
            with open(self.arquivo_usuario, 'r') as arquivo:
                cadastrados = json.load(arquivo)
        else:
            cadastrados = {"Usuarios": []}

        print("Cadastro novo usuario")
        nome = str(input("Nome Completo: ")).title()
        user_name = str(input("Usuario: "))
        senha = str(input("Senha: "))

        id_user = len(cadastrados["Usuarios"]) + 1

        usuario = Usuario(nome, id_usuario=id_user,
                          senha=senha, user_name=user_name)

        cadastrados["Usuarios"].append(
            usuario.converter_usuario_para_dicionario())

        with open(self.arquivo_usuario, "w") as arquivo:
            json.dump(cadastrados, arquivo, indent=4)

        print("Novo usuario cadastrado com sucesso")
        input("Pressione qualquer tecla para voltar")

    def login(self):
        if not os.path.exists(self.arquivo_usuario):
            print("Nenhum arquivo encontrado")
            input("Pressione qualquer tecla para continuar")
            return
        with open(self.arquivo_usuario, 'r') as arquivo:
            dados_usuario = json.load(arquivo)
        print("Login de Usuario")
        user_name = str(input("Usuario: "))
        senha = str(input("Senha: "))
        for usuario in dados_usuario["Usuarios"]:
            if user_name == usuario["User_name"] and senha == usuario["Senha"]:
                print(f"Bem vindo, {usuario['Nome']}!")
                input("Pressione qualquer tecla para continuar")
                return usuario

        print("ID ou senha incorretos.")
        input("Pressione qualquer tecla para voltar")
        return None

    def emprestar_livro(self, usuario_logado):
        if not os.path.exists(self.arquivo_livros):
            print("Nenhum livro encontrado")
            input("Pressione qualquer tecla para continuar")
            return
        with open(self.arquivo_livros, 'r') as arquivo:
            dados_livros = json.load(arquivo)

        self.listar_livros()
        codigo = int(input("\nDigite o codigo do livro: "))
        for livro in dados_livros["Livros"]:
            if livro["Codigo"] == codigo:
                livro["Status"] = f"Indisponivel com {usuario_logado['Nome']}"
                usuario_logado["Livros_emprestados"].append(livro["Codigo"])
                with open(self.arquivo_livros, 'w') as arquivo:
                    json.dump(dados_livros, arquivo, indent=4)

                with open(self.arquivo_usuario, "r") as arquivo:
                    dados_usuario = json.load(arquivo)

                for usuario in dados_usuario["Usuarios"]:
                    if usuario["ID_user"] == usuario_logado["ID_user"]:
                        usuario["Livros_emprestados"] = usuario_logado["Livros_emprestados"]
                with open(self.arquivo_usuario, "w") as arquivo:
                    json.dump(dados_usuario, arquivo, indent=4)

                print("Livro emprestado com sucesso!")
                input("Pressione para voltar")
                return


def limpar_tela():
    os.system("cls")


def cadastros():
    biblioteca = Biblioteca()

    while True:
        limpar_tela()
        print("1 - Cadastrar livro")
        print("2 - Cadastrar Usuario")
        print("3 - Login")
        print("0 - Voltar")

        option = input("Escolha: ")

        if option == '1':
            limpar_tela()
            biblioteca.cadastro_livro()
        elif option == '2':
            limpar_tela()
            biblioteca.cadastro_usuario()
        elif option == "0":
            print("Voltando")
            break


def main():
    biblioteca = Biblioteca()

    while True:
        limpar_tela()
        print("1 - Cadastros")
        print("2 - Listar livros")
        print("3 - Login")
        print("0 - sair")

        option = input("Escolha: ")

        if option == '1':
            limpar_tela()
            cadastros()

        elif option == '2':
            limpar_tela()
            biblioteca.listar_livros()
            input("Pressione qualquer tecla para continuar")

        elif option == '3':
            limpar_tela()
            usuario_logado = biblioteca.login()
            if usuario_logado:
                menu_usuario(usuario_logado)

        elif option == '0':
            print("Saindo")
            break

        else:
            print("opção invalida")


def menu_usuario(usuario_logado):
    biblioteca = Biblioteca()
    while True:
        limpar_tela()
        print("Menu de usuario")
        print(f"Usuario: {usuario_logado['Nome']}")
        print("1 - Emprestar livro")
        print("2 - Devolver livro")
        print("3 - Meus livros")
        print("0 - Desconectar")

        option = int(input("Escolha: "))

        if option == 1:
            limpar_tela()
            biblioteca.emprestar_livro(usuario_logado)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 0:
            print("Desconectando")
            break


if __name__ == "__main__":
    main()
