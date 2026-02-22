#MINI SISTEMA DE LOJA
from modulo1 import Loja as lj

def add_produtos():
    produto = input("Digite o nome do produto: ")
    preço = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    lj().add_produtos(produto, preço, quantidade)

def listar_produtos():
    lj().carregar_produtos()

def vender_produtos():
    Nome = input("Digite o nome completo do cliente: ")
    ID = int(input("Digite o id do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    lj().valor_total(Nome, ID, quantidade)

def mostrar_historico():
    with open("historico.txt", "r") as f:
        historico = f.read()
        print(historico)

def loja():
    try:
        while True:
            print("\n\033[92mMINI SISTEMA DE LOJA\033[0m\n")
            print(" \033[94m1-Adicionar produtos\n 2-Listar os produtos\n 3-Fazer a venda\n 4-Mostrar historico de vendas\n 5-Sair\033[0m")
            opcao = int(input("Escolha uma das opções acima para continuar: "))
            print("")
            
            if opcao == 1:
                passw = input(" \nDigite a pass para continuar: ")
                if passw == "556789":
                    add_produtos()
                else:
                    print("\033[91mSenha incorrecta!\033[0m")
                    
            elif opcao == 2:
                listar_produtos()
            elif opcao == 3:
                vender_produtos()
            elif opcao == 4:
                mostrar_historico()
            elif opcao == 5:
                break
            else:
                print("\033[91mOpçao Invalida!\033[0m")
    except (ValueError, TypeError, FileNotFoundError):
        print("Erro opção invalida!")
loja()