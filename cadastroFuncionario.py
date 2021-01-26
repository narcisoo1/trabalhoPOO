class OpcoesFuncionario:
    __slots__ = ['_lista_funcionarios']

    """
    Inicia self._lista_funcionario como lista vazia
    """

    def __init__(self):
        self._lista_funcionarios=[]

    def cadastra(self, funcionario):
        """
        Cadastra um funcionário

        Retorna True caso consiga cadastrar funcionário e False caso contrário    
        :param funcionario: Objeto
        :return: Booleano True ou False
        """
        existe=self.busca(funcionario.cpf)
        if(existe==None):
            self._lista_funcionarios.append(funcionario)
            return True
        else:
            return False
    
    def busca(self,cpf):
        """
        Busca por um funcionário cadastrado

        Retorna o objeto funcionário caso esse funcionário exista na lista self._lista_funcionario, None caso contrário
        :param cpf: String
        :return: Objeto ou None
        """
        for x in self._lista_funcionarios:
            if x.cpf==cpf:
                return x
        return None
    
    def login(self,usuario,senha):
        """
        Verifica se usuário está cadastrado no sistema

        Retorna o objeto funcionário, caso esse existe na lista ou None caso contrário
        :param usuario: String
        :param senha: String
        :return: Objeto ou None
        """
        for x in self._lista_funcionarios:
            if ((x.login==usuario) and (x.senha==senha)):
                return x
        return None
