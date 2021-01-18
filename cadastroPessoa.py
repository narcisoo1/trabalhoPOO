class CadastroPessoa:
    __slots__=['_lista_pessoas']

    """
    Inicializa self._lista_pessoas como lista vazia
    """
    def __init__(self):
        self._lista_pessoas=[]
    
    def cadastra(self, pessoa):
        """
        Cadastra uma pessoa

        Retorna True se conseguiu cadastrar pessoa e False caso contrário.
        :param pessoa: Objeto
        :return: Booleano True ou False
        """
        existe=self.busca(pessoa.cpf)
        if(existe==None):
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False
    
    def busca(self,cpf):
        """
        Busca por uma pessoa

        Retorna um objeto se conseguiu encontrar o cpf na self._lista_pessoas, caso contrário retorna None
        :param cpf: String
        :return: String ou None
        """
        for x in self._lista_pessoas:
            if x.cpf==cpf:
                return x
        return None

    def vazio(self):
        """
        Testa se lista está vazia
        
        Retorna False se a lista self._lista_pessoas estiver vazia, True caso contrário 
        :return: Booleano True ou Falso
        """
        if len(self._lista_pessoas)==0:
            return True
        else:
            return False
