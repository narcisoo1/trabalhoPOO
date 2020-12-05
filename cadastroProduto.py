class CadastroProduto:

	__quantidade_Estoque = 0
	
	__slots__ = ['__idProduto', '__nomeProduto', '__precoProduto']


	def __init__(self, idProduto, nomeProduto, precoProduto):
		self.__idProduto = idProduto
		self.__nomeProduto = nomeProduto
		self.__precoProduto = precoProduto
		CadastroProduto.__quantidade_Estoque += 1

	@staticmethod
	def quantidade_estoque():
		return CadastroProduto.__quantidade_Estoque
	@staticmethod
	def retiraEstoque():
		CadastroProduto.__quantidade_Estoque -= 1

	@property
	def idProduto(self):
		return self.__idProduto
	@idProduto.setter
	def idProduto(self, idProduto):
		self.__idProduto = idProduto

	@property
	def nomeProduto(self):
		return self.__nomeProduto
	@nomeProduto.setter
	def nomeProduto(self, nomeProduto):
		self.__nomeProduto = nomeProduto

	@property
	def precoProduto(self):
		return self.__precoProduto
	@precoProduto.setter
	def precoProduto(self, precoProduto):
		self.__precoProduto = precoProduto
	
