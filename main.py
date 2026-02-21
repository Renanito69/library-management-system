import json
import os
class Livro:
    def __init__(self, titulo, autor, codigo, ano):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ano = ano
        self.disponivel = True
        
    def converter_livros_para_dicionario(self):
        return {
            "Titulo": self.titulo,
            "Autor": self.autor,
            "Lancamento": self.ano,
            "Codigo": self.codigo,
            "Disponivel": self.disponivel
        }
        
class Usuario:
    def __init__(self, nome, id_usuario, senha):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []
        self.senha = senha
    
    def converter_usuario_para_dicionario(self):
        return {
            "Nome": self.nome,
            "ID_user": self.id_usuario,
            "Senha": self.senha,
            "Livros_emprestados": self.livros_emprestados
        }

class Biblioteca:
    def __init__(self):
        self.arquivo_livros = "Livros.json"
        self.arquivo_usuario = "Usuarios.json"
        

    def cadastro_livro(self):
        if os.path.exists("Livros.json"):
            with open("Livros.json", "r") as arquivo:
                cadastrados = json.load(arquivo)
        else:
            cadastrados = {"Livros": []}
        
        print("Cadastro de livro")
        titulo = input("Titulo: ").title()
        autor = input("Autor: ").title()
        ano = int(input("Ano de Lançamento: "))
        if not os.path.exists("Livros.json"):
            codigo = 1
        else:
            codigo = len(cadastrados["Livros"]) + 1
        
        livros = Livro(titulo, autor, codigo, ano)
        
        cadastrados["Livros"].append(livros.converter_livros_para_dicionario())
        
        with open("Livros.json", 'w') as arquivo:
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
            status = "Disponivel" if livro["Disponivel"] else "Indisponivel"
            print(f"Código: #0{livro['Codigo']}")
            print(f"Título: {livro['Titulo']}")
            print(f"Autor: {livro['Autor']}")
            print(f"Lancamento: {livro['Lancamento']}")
            print(f"Status: {status}")
            print("-" * 30)
        input("Pressione qualquer tecla para voltar")
        
    def cadastro_usuario(self):
        if os.path.exists(self.arquivo_usuario):
            with open(self.arquivo_usuario, 'r') as arquivo:
                cadastrados = json.load(arquivo)
        else:
            cadastrados = {"Usuarios": []}
            
        print("Cadastro novo usuario")
        nome = str(input("Usuario: ")).title()
        senha = str(input("Senha: "))

        id_user = len(cadastrados["Usuarios"]) + 1
        
        usuario = Usuario(nome, id_usuario=id_user, senha=senha)
        
        cadastrados["Usuarios"].append(usuario.converter_usuario_para_dicionario())
        
        with open(self.arquivo_usuario, "w") as arquivo:
            json.dump(cadastrados, arquivo, indent=4)
        
        print("Novo usuario cadastrado com sucesso")
        input("Pressione qualquer tecla para voltar")
    
def limpar_tela():
    os.system("cls")
    
def cadastros():
    biblioteca = Biblioteca()
    
    while True:
        limpar_tela()
        print("1 - Cadastrar livro")
        print("2 - Cadastrar Usuario")
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
        print("0 - sair")
        
        option = input("Escolha: ")
        
        if option == '1':
            limpar_tela()
            cadastros()
        
        elif option == '2':
            limpar_tela()
            biblioteca.listar_livros()
        
        elif option == '0':
            print("Saindo")
            break
        
        else:
            print("opção invalida")
            
if __name__ == "__main__":
    main()