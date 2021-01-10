def Valida_Venda(nomeprod,qtd,produtos,cpfCliente,cpfVendedor):
    for obj in produtos:
        if(obj.nomeProduto == nomeprod):
            if(obj.qtdProduto>=qtd):
                obj.qtdProduto-=qtd
                return Venda(obj.nomeProduto, obj.idProduto, qtd, cpfCliente, cpfVendedor)
            else:
                print("Quantidade excede o estoque!")
                return False
    print("Produto não localizado!")
    return False

class Venda:
    def __init__ (self, nomeProduto, qtdProduto, cliente, vendedor):
        self._nomeProduto=nomeProduto
        self._qtdProduto=qtdProduto
        self._cliente=cliente
        self._vendedor=vendedor

    @property
    def nomeProduto(self):
        return self._nomeProduto
    
    @property
    def qtdProduto(self):
        return self._qtdProduto
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def vendedor(self):
        return self._vendedor