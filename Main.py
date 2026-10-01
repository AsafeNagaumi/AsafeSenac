import os

from Cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido
from Pedido import Pedido

os.system('cls')

listaCliente = []
listaProduto = []

def MenuPrincipal():
    while True:
            print(f"\n|=====================================|"
                  f"\n|          MENU DOS PRODUTOS          |"
                  f"\n|=====================================|"
                  f"\n|1 -         Menu Clientes            |"
                  f"\n|2 -         Menu Produtos            |"
                  f"\n|3 -    Voltar ao Menu Principal      |"
                  f"\n|=====================================|")
            opcs = input("\nInserir Opção:")

            if opcs =="1": MenuClientes()

            elif opcs =="2": MenuProdutos()

            elif opcs =="3": break

            else: print("Por favor, escolha uma opção válida.")
              
       
def MenuClientes(): 
    while True:
            print(f"\n|=====================================|"
                  f"\n|          MENU DOS CLIENTES          |"
                  f"\n|=====================================|"
                  f"\n|1 -       Cadastrar Cliente          |"
                  f"\n|2 -        Listar Clientes           |"
                  f"\n|3 -    Voltar ao Menu Principal      |"
                  f"\n|=====================================|")
            opc = input("\nOpção:")

            if opc =="1":
                novocli = Cliente(input("Nome:"), input("Telefone:"), input("Endereço:"))
                listaCliente.append(novocli)
                print("\nCliente cadastrado com sucesso!")

                
            elif opc =="2":
                  for novocli in listaCliente:
                        novocli.imprimir() 
                  
            elif opc =="3": break

            else: print("Por favor, escolha uma opção válida.")


def MenuProdutos():
    while True:
            print(f"\n|=====================================|"
                  f"\n|          MENU DOS PRODUTOS          |"
                  f"\n|=====================================|"
                  f"\n|1 -       Cadastrar Produto          |"
                  f"\n|2 -        Listar Produtos           |"
                  f"\n|3 -    Voltar ao Menu Principal      |"
                  f"\n|=====================================|")
            opcs = input("\nInserir Opção:")

            if opcs =="1": 
                  novoPro = Produto(input("Código:"), input("Descrição:"), input("Categoria:"), input("Preço:"))
                  listaProduto.append(novoPro)
                  print("Produto Cadastrado com sucesso!")
                 
            elif opcs =="2": 
                 for novoPro in listaProduto:
                      novoPro.imprimir()

            elif opcs =="3": break

            else: print("Por favor, escolha uma opção válida.")


if __name__ == "__main__":
     MenuPrincipal()