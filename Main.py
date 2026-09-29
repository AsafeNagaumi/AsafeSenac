import os

from Cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido
from Pedido import Pedido

os.system('cls')

# Cliente
novoCli = Cliente(nome="João", endereco="Rua boa, nº00", telefone="67 (+55) 7265-1233")

# Produtos
siri = Produto(cod=1, desc="Hambúrguer de Siri", categoria="Lanche", preco=20.55)
refri = Produto(cod=2, desc="Tubaina", categoria="Bebida", preco=5.60)

# Itens do pedido
Item1 = ItemPedido(produto=siri, obs="Cebola Extra", qtd=2, desconto=2)
Item2 = ItemPedido(produto=refri, obs="Motoboy morreu no caminho", qtd=2, desconto=0)

# Lista de itens
itens = [Item1, Item2]

# Pedido
pedido = Pedido(num=1, data="10/09/11", hora="20:30", cliente=novoCli, itens=itens, pagamento="Pix")
pedido.imprimir()
