class CadastroPessoa:
    __slots__=['_lista_pessoas']

    def __init__(self):
        self._lista_pessoas=[]
    
    def cadastra(self, pessoa):
        existe=self.busca(pessoa.cpf)
        if(existe==None):
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False
    
    def busca(self,cpf):
        for x in self._lista_pessoas:
            if x.cpf==cpf:
                return x
        return None

    def vazio(self):
        if len(self._lista_pessoas)==0:
            return True
        else:
            return False