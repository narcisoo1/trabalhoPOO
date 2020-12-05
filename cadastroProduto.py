class CadastroProduto:

	__quantidade_Estoque = 0
	
	__slots__ = ['__codigo', '__nome', '__preco']


	def __init__(self, codigo, nome, preco):
		self.__codigo = codigo
		self.__nome = nome
		self.__preco = preco
		CadastroProduto.__quantidade_Estoque += 1

	@staticmethod
	def quantidade_estoque():
		return CadastroProduto.__quantidade_Estoque

	@property
	def codigo(self):
		return self.__codigo

	@codigo.setter
	def codigo(self, codigo):
		self.__codigo = codigo

	@property
	def nome(self):
		return self.__nome
	@nome.setter
	def nome(self, nome):
		self.__nome = nome

	@property
	def preco(self):
		return self.__preco
	@preco.setter
	def preco(self, preco):
		self.__preco = preco
	
