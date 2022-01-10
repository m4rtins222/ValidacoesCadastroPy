from validate_docbr import CNPJ

class Cnpj:
	#Métodos Especiais
	def __init__(self,documento):
		documento = str(documento)
		if self.validar_cnpj(documento):
			self.cnpj = documento
		else:
			raise ValueError('CNPJ INVÁLIDO')

	def __str__(self):
		return self.formatar_cnpj()

	#Métodos Criados
	def validar_cnpj(self,cnpj):
		if len(cnpj) == 14:
			validador = CNPJ()
			return validador.validate(cnpj)
		else:
			raise ValueError('Quantidade de dígitos inválida')

	def formatar_cnpj(self):
		mascara = CNPJ()
		return mascara.mask(self.cnpj)