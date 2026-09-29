# Projeto Lanchonete 
Esse projeto estou trabalhado na aprendizagem da criação e o desenvolvimento do diagrama de classes no **Senac** no curso de **Técinco de Desenvolvimento de Software**

## ▶️ Como Rodar o Projeto ##
1. Instale a versão mais recente do Python
2. Faça git clone https://github.com/AsafeNagaumi/AsafeSenac.git
3. Abra a pasta do projeto:
    - Digite CMD na barra de endereço do MS Explorer;
    - Digite: code . no terminal (Tem que ter espaço do code e o ponto);
4. Abra o arquivo main.py e clique em executar;

```python
class Pedido:
    def __init__(self, numero, data, hora, cliente, itens, pagamento):
        self.numero = numero
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.itens = itens
        self.pagamento = pagamento
        self.status = "Aguardando"

    def imprimir(self):
        print(f"--- Pedido nº {self.numero} ---")
        print(f"Data: {self.data} | Hora: {self.hora}")
        print(f"Cliente: {self.cliente}")
        print(f"Itens: {', '.join(self.itens)}")
        print(f"Pagamento: {self.pagamento}")
        print(f"Status: {self.status}")
        print("-----------------------------")

    def atualizarPedido(self, novo_status):
        self.status = novo_status
        print(f"Status atualizado para: {self.status}")


# Exemplo de uso
novoPedido = Pedido(
    numero=1,
    data="14/09/26",
    hora="21:10",
    cliente="João",
    itens=["X-Salada", "X-Bacon"],
    pagamento="Pix"
)

# Acessando atributos
print(novoPedido.cliente)   # João
print(novoPedido.status)    # Aguardando

# Alterando atributos
novoPedido.cliente = "Calebe"
print(novoPedido.cliente)   # Calebe 

# Usando métodos
novoPedido.imprimir()
novoPedido.atualizarPedido("Em preparação")
novoPedido.imprimir()
```