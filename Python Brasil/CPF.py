from validate_docbr import CPF

class Cpf:
	#Métodos Especiais
	def __init__(self,documento):
		documento = str(documento)
		if self.validar_cpf(documento):
			self.cpf = documento
		else:
			raise ValueError('CPF INVÁLIDO')

	def __str__(self):
		return self.formatar_cpf()

	#Métodos Criados
	def validar_cpf(self,cpf):
		if len(cpf) == 11:
			validador = CPF()
			return validador.validate(cpf)
		else:
			raise ValueError('Quantidade de dígitos inválida!')

	def formatar_cpf(self):
		mascara = CPF()
		return mascara.mask(self.cpf)