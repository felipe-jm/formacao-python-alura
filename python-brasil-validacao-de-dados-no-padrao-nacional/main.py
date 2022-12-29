from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

# CPF e CNPJ
cpf_um = Documento.cria_documento('63179379073')
cnpj_um = Documento.cria_documento('70253762000185')

print(cpf_um)
print(cnpj_um)

# Telefones
telefone = '552126481234'

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

# Datas
cadastro = DatasBr()
print('Momento do cadastro: ', cadastro.momento_cadastro)
print('Mês do cadastro: ', cadastro.mes_cadastro())
print('Semana do cadastro: ', cadastro.dia_semana())
print('Tempo do cadastro: ', cadastro.tempo_cadastro())
print(cadastro)

# CEP
cep = 78550514
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
objeto_cep.acessa_via_cep()