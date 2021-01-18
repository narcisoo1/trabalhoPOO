class Produto:
	
	__slots__ = ['__idProduto', '__nomeProduto', '__precoProduto', '__qtdProduto']

	"""
	Inicializa atributos do objeto
	"""

	def __init__(self, idProduto, nomeProduto, precoProduto, qtdProduto):
		"""
		:param idProduto: String
		:param nomeProduto: String
		:param precoProduto: Float
		:param qtdProduto: Int
		"""
		self.__idProduto = idProduto
		self.__nomeProduto = nomeProduto
		self.__precoProduto = precoProduto
		self.__qtdProduto = qtdProduto
	

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
	
	@property
	def qtdProduto(self):
		return self.__qtdProduto
	@qtdProduto.setter
	def qtdProduto(self,qtdProduto):
		self.__qtdProduto=qtdProduto
