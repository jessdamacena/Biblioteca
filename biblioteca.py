# Sistema de cadastro de biblioteca
# Permite cadastrar, listar, buscar, emprestar e devolver livros
# além de contar o acervo e remover livros (funcionalidades extras)

import json
import os

def carregar_livros():
    # Carrega a lista de livros do arquivo livros.json, se existir, ou retorna uma lista vazia
    if os.path.exists("livros.json"):
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []
        
livros = carregar_livros()

def salvar_livros():
    # Grava a lista atual no livros.json (chamada sempre que algo muda)
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)

def cadastrar_livro():
    # Pede os dados e adiciona o livro na lista, começando como disponível
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ").strip()
    livros.append({"titulo": titulo, "autor": autor, "ano": ano, "disponivel": "Sim"})
    salvar_livros()
    print("Livro cadastrado!")

def exibir_livro(livro):
    # Mostra os dados de um livro
    print("Título:", livro["titulo"], "Autor:", livro["autor"], "Ano:", livro["ano"], "Disponível:", livro["disponivel"])

def listar_livros():
    # Mostra todos os livros cadastrados
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        exibir_livro(livro)

def buscar_livro(): 
    # Procura o termo no título ou no autor, sem diferenciar maiúsculas de minúsculas
    termo = input("Buscar por título ou autor: ").strip().lower()
    encontrado = False # vira True se algum livro bater com a busca
    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            exibir_livro(livro)
            encontrado = True
    if not encontrado:
        print("Livro não encontrado.")

def emprestar_livro():
    # Procura o livro pelo título exato e marca como emprestado, se estiver disponível
    titulo = input("Digite o titulo do livro que deseja emprestar: ").strip().lower()
    encontrado = False

    for livro in livros:
        if titulo == livro["titulo"].lower():
            encontrado = True
            if livro["disponivel"] == "Não":
                print("Livro indisponível para empréstimo.")
            else:
                livro["disponivel"] = "Não"
                salvar_livros()
                print("Livro emprestado com sucesso!")
            break
    if not encontrado:
        print("Livro não encontrado.")

def devolver_livro():
    # Procura o livro pelo título exato e marca como disponível, se estiver emprestado
    titulo = input("Digite o titulo do livro que deseja devolver: ").strip().lower()
    encontrado = False

    for livro in livros:
        if titulo == livro["titulo"].lower():
            encontrado = True
            if livro["disponivel"] == "Sim":
                print("Livro já está disponível na biblioteca.")
            else:
                livro["disponivel"] = "Sim"
                salvar_livros()
                print("Livro devolvido com sucesso!")
            break
    if not encontrado:
        print("Livro não encontrado.")

def contar_acervo():
    # EXTRA 1: mostra o total de livros, quantos estão disponíveis e quantos emprestados
    disponiveis = 0
    for livro in livros:
        if livro["disponivel"] == "Sim":
            disponiveis += 1

    emprestados = len(livros) - disponiveis
    print("Total de livros:", len(livros))
    print("Disponíveis:", disponiveis)
    print("Emprestados:", emprestados)

def remover_livro():
    # EXTRA 2: remove um livro da lista pelo título exato e atualiza o arquivo
    titulo = input("Digite o título do livro que deseja remover: ").strip().lower()
    encontrado = False

    for livro in livros:
        if titulo == livro["titulo"].lower():
            livros.remove(livro)
            salvar_livros()
            print("Livro removido com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Livro não encontrado.")

def menu():
    print("\n=== BIBLIOTECA ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("6. Contar acervo")
    print("7. Remover livro")
    print("0. Sair")

# Loop principal do programa, que exibe o menu e chama as funções correspondentes às opções escolhidas pelo usuário
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        emprestar_livro()
    elif opcao == "5":
        devolver_livro()
    elif opcao == "6":
        contar_acervo()
    elif opcao == "7":
        remover_livro()
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")