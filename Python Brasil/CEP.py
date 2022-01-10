import requests
import json

class BuscaEndereco:

	def __init__(self, cep):
		cep = str(cep)
		if self.cep_e_valido(cep):
			self.cep = cep
		else:
			raise ValueError('CEP inválido!')

	def __str__(self):
		return self.format_cep()

	def cep_e_valido(self,cep):
		if len(cep) == 8:
			return True
		else:
			return False

	def format_cep(self):
		return f'{self.cep[0:5]}-{self.cep[5:]}'

	def retorna_endereco(self):
		endereco = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()
		return f'Cep: {endereco["cep"]}\nEndereço: {endereco["logradouro"]}\nComplemento: {endereco["complemento"]}\nBairro: {endereco["bairro"]}\nCidade: {endereco["localidade"]}/{endereco["uf"]}'
