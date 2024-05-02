class Invoice:
    def __init__(self):
        self.numero_item = None
        self.descricao_item = None
        self.quantidade_compra = 0
        self.preco = 0.0 

    def setNumero(self, newNumero):
        self.numero_item = newNumero

    def setDescricao(self, newDesc):
        self.numero_item = newDesc

    def setQuantidade(self, newQuantidade):
        self.quantidade_compra = newQuantidade

    def setPreco(self, newValor):
        self.preco = newValor

    def getNumero(self):
        return self.numero_item

    def getDescricao(self):
        return self.descricao_item

    def getQuantidade(self):
        return self.quantidade_compra

    def getPreco(self):
        return self.preco

    def getInvoiceAmount(self):
        self.valorFatura = (self.quantidade_compra * self.preco)
        return self.valorFatura

faturaUm = Invoice()

faturaUm.numero_item = 4
faturaUm.descricao_item = "È um item"
faturaUm.quantidade_compra = 0
faturaUm.preco = 5

fatura = faturaUm.getInvoiceAmount()

print("O preço da fatura é {}".format(fatura))
print(faturaUm.preco)
print(faturaUm.quantidade_compra)