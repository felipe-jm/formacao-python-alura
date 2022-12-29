import pytest
from pytest import mark

from codigo.bytebank import Funcionario

class TestClass:
  def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
    # Given When Then

    # Given - Contexto
    entrada = '13/03/2000' 
    esperado = 22

    funcionario_teste = Funcionario('Teste', entrada, 1111)

    # When - Ação
    resultado = funcionario_teste.idade()

    # Then - Desfecho
    assert resultado == esperado

  def test_quando_sobrenome_recebe_Felipe_Jung_deve_retornar_Jung(self):
    entrada = ' Felipe Jung ' # Given
    esperado = 'Jung'

    felipe = Funcionario(entrada, '27/01/2000', 1111)
    resultado = felipe.sobrenome() # When

    assert resultado == esperado # Then

  def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
    entrada_salario = 100000 # Given
    entrada_nome = 'Paulo Bragança'
    esperado = 90000

    funcionario_teste = Funcionario(entrada_nome, '27/01/2000', entrada_salario)
    funcionario_teste.decrescimo_salario() # When
    resultado = funcionario_teste.salario

    assert resultado == esperado # Then

  @mark.calcular_bonus
  def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
    entrada = 1000 # Given
    esperado = 100

    funcionario_teste = Funcionario('Teste', '27/01/2000', entrada)
    resultado = funcionario_teste.calcular_bonus() # When

    assert resultado == esperado # Then

  @mark.calcular_bonus
  def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
    with pytest.raises(Exception):
      entrada = 1000000 # Given

      funcionario_teste = Funcionario('Teste', '27/01/2000', entrada)
      resultado = funcionario_teste.calcular_bonus() # When

      assert resultado # Then
