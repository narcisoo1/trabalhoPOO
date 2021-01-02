class CadastroProduto:
    __slots__=['_lista_produtos']

    def __init__(self):
        self._lista_produtos=[]
    
    def cadastra(self, produto):
        existe=self.busca(produto.idProduto)
        if(existe==None):
            self._lista_produtos.append(produto)
            return True
        else:
            return False
    
    def busca(self,idProduto):
        for x in self._lista_produtos:
            if x.idProduto==idProduto:
                return x
        return None