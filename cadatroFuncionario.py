class OpcoesFuncionario:
    __slots__ = ['_lista_funcionarios']

    def __init__(self):
        self._lista_funcionarios=[]

    def cadastra(self, funcionario):
        existe=self.busca(funcionario.cpf)
        if(existe==None):
            self._lista_funcionarios.append(funcionario)
            return True
        else:
            return False
    
    def busca(self,cpf):
        for x in self._lista_funcionarios:
            if x.cpf==cpf:
                return x
        return None
    
    def login(self,usuario,senha):
        for x in self._lista_funcionarios:
            if ((x.login==usuario) and (x.senha==senha)):
                return x
        return None