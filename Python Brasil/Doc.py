from CPF import Cpf
from CNPJ import Cnpj

#Factory Para CPF e CNPJ
class Documento:
	@staticmethod
	def cria_documento(documento):
		if len(documento) == 11:
			return Cpf(documento)

		elif len(documento) == 14:
			return Cnpj(documento)

		else:
			raise ValueError('Quantidade de dígitos está incorreta!')