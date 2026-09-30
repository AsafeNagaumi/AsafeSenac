from Produto import Produto 
import os
from Cliente import Cliente

os.system('cls')

listaCliente = []

def MenuPrincipal():
       while True:
        print(f"\n|------------------------------|"
              f"\n|------- Menu Principal -------|"
              f"\n|1 ----- Menu Clientes  -------|"
              f"\n|2 ----- Menu Produtos  -------|"
              f"\n|3 ----- Finalizar ------------|"
              f"\n|------------------------------|")
        opcs = input("Inserir Opcção:")

        if opcs =="1": MenuClientes()

        elif opcs =="2": MenuProdutos()

        elif opcs =="3": break
              
       
def MenuClientes():
    
    while True:
        print(f"\n|-------------------------------------------|"
              f"\n|----------- Menu Do Cliente ---------------|"
              f"\n|1 --------- Cadastrar Cliente -------------|"
              f"\n|2 --------- Listar Clientes ---------------|"
              f"\n|3 --------- Voltar ao Menu Principal ------|"
              f"\n|-------------------------------------------|")
        opc = input("Opção:")

        if opc =="1":
                novocli = Cliente(input("Nome:"), input("Telefone:"), input("Endereço:"))
                listaCliente.append(novocli)
                print("Cliente cadastrado com sucesso!")
                
        elif opc =="2":
                for novocli in listaCliente:
                    novocli.imprimir() 
                
        elif opc =="3": break


def MenuProdutos():
     print(f"\n|-------------------------------------|"
           f"\n|--------- Menu dos Produtos ---------|"
           f"\n|1 ------- Cadastrar Produto ---------|"
           f"\n|2 ------- Listar Produtos -----------|"
           f"\n|3 ----- Voltar ao Menu Principal ----|"
           f"\n|-------------------------------------|")
