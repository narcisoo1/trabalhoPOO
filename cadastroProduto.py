class CadastroProduto:
    __slots__=['_lista_produtos','_lista_vendas']

    def __init__(self):
        self._lista_produtos=[]
        self._lista_vendas=[]
    
    def cadastra(self, produto):
        existe=self.busca(produto.idProduto)
        if(existe==None):
            self._lista_produtos.append(produto)
            return True
        else:
            for x in range(0,len(self._lista_produtos)):
                if self._lista_produtos[x].nomeProduto==produto.nomeProduto:
                    self._lista_produtos[x].qtdProduto+=produto.qtdProduto
                    print(self._lista_produtos[x].qtdProduto)
                    return True
        return False
    
    def busca(self,idProduto):
        for x in self._lista_produtos:
            if x.idProduto==idProduto:
                return x
        return None
    
    def venda(self,venda):
        for x in range(0,len(self._lista_produtos)):
            if venda.nomeProduto == self._lista_produtos[x].nomeProduto:
                if venda.qtdProduto <= self._lista_produtos[x].qtdProduto:
                    self._lista_vendas.append(venda)
                    self._lista_produtos[x].qtdProduto-=venda.qtdProduto
                    return True
        return False