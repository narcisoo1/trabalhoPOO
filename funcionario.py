from pessoa import Pessoa


class Funcionario(Pessoa):
    __slots__ = ['_nome', '_cpf', '_endereco', '_telefone', '_login', '_senha']

    def __init__(self, nome=0, cpf=0, endereco=0, telefone=0, senha=0, login=0):
        super().__init__(nome, cpf, endereco, telefone)
        self._login = login
        self._senha = senha

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
