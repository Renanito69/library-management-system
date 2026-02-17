import json
import os
class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True
        
    def converte_para_dicionario(self):
        return {
            "Titulo": self.titulo,
            "Autor": self.autor,
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
        self.livros = []
        self.usuario = []
        

def cadastro_livro(self):
    if os.path.exists("Livros.json"):
        with open("Livros.json", "r") as arquivo:
            cadastrados = json.load(arquivo)
    else:
        cadastrados = {"Livros": []}
    livros = dict()
    print("Cadastro de livro")
    livros["Titulo"] = input("Titulo: ")
    livros["Autor"] = input("Autor: ")
    if not os.path.exists("Livros.json"):
        livros["Codigo"] = 1
    else:
        livros["Codigo"] = len(cadastros) + 1
    livros["Disponvel"] = False
    cadastros["Usuarios cadastrados"].append(livros)
    
    with open("Livros.json", 'w') as arquivo:
        json.dump(cadastrados, arquivo, indent=4)

def main():
    
    
    while True:
        print("1 - Cadastros")
        print("2 - Listar livros")
        print("3 - sair")
        
        option = input("Escolha: ")
        
        if option == 1:
            pass
        
        elif option == 2:
            pass
        
        elif option == 3:
            print("Saindo")
            break
        
        else:
            print("opção invalida")
            
if __name__ == "__main__":
    main()