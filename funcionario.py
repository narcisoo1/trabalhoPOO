from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, login, senha):
        super().__init__(nome,cpf,endereco,telefone)
        self._login=login
        self._senha=senha

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self,usuario):
        self._login=login
    
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha=senha