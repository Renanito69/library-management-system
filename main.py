import json
import os
class Livro:
    def __init__(self, titulo, autor, codigo, ano):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ano = ano
        self.disponivel = True
        
    def converte_para_dicionario(self):
        return {
            "Titulo": self.titulo,
            "Autor": self.autor,
            "Lancamento": self.ano,
            "Codigo": self.codigo,
            "Disponivel": self.disponivel
        }
        
class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.arquivo_livros = "Livros.json"
        self.usuario = []
        

    def cadastro_livro(self):
        if os.path.exists("Livros.json"):
            with open("Livros.json", "r") as arquivo:
                cadastrados = json.load(arquivo)
        else:
            cadastrados = {"Livros": []}
        livros = dict()
        print("Cadastro de livro")
        livros["Titulo"] = input("Titulo: ").title()
        livros["Autor"] = input("Autor: ").title()
        livros["Lancamento"] = int(input("Ano de Lançamento: "))
        if not os.path.exists("Livros.json"):
            livros["Codigo"] = 1
        else:
            livros["Codigo"] = len(cadastrados["Livros"]) + 1
        livros["Disponivel"] = True
        cadastrados["Livros"].append(livros)
        
        with open("Livros.json", 'w') as arquivo:
            json.dump(cadastrados, arquivo, indent=4)
            
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
        input("Pessione qualquer tecla para voltar")
    
def limpar_tela():
    os.system("cls")

def main():
    biblioteca = Biblioteca()
    
    
    while True:
        limpar_tela()
        print("1 - Cadastros")
        print("2 - Listar livros")
        print("3 - sair")
        
        option = input("Escolha: ")
        
        if option == '1':
            limpar_tela()
            biblioteca.cadastro_livro()
        
        elif option == '2':
            limpar_tela()
            biblioteca.listar_livros()
        
        elif option == '3':
            print("Saindo")
            break
        
        else:
            print("opção invalida")
            
if __name__ == "__main__":
    main()