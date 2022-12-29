from validate_docbr import CPF, CNPJ

class Documento:

  def cria_documento(documento):
    if len(documento) == 11:
      return DocCpf(documento)
    elif len(documento) == 14:
      return DocCnpj(documento)
    else:
      raise ValueError("Quantidade de dígitos inválida!")

class DocCpf:
  def __init__(self, documento):
    documento = str(documento)
    if self.valida(documento):
      self.cpf = documento
    else:
      raise ValueError('CPF Inválido!')

  def valida(self, cpf):
    if len(cpf) == 11:
      validador = CPF()
      return validador.validate(cpf)
    else:
      raise ValueError('Quantidade de dígitos inválida!')

  def format_cpf(self):
    mascara = CPF()
    return mascara.mask(self.cpf)

  def __str__(self):
    return self.format_cpf()

class DocCnpj:
  def __init__(self, documento):
    documento = str(documento)
    if self.valida(documento):
      self.cnpj = documento
    else:
      raise ValueError('CNPJ Inválido!')

  def valida(self, cnpj):
    if len(cnpj) == 14:
      validador = CNPJ()
      return validador.validate(cnpj)
    else:
      raise ValueError('Quantidade de dígitos inválida!')

  def format_cnpj(self):
    mascara = CNPJ()
    return mascara.mask(self.cnpj)

  def __str__(self):
    return self.format_cnpj()