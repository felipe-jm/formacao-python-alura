# Como rodar os testes :test_tube: :white_check_mark:

```bash
# Rodar todos os testes
pytest -v

# Rodar apenas testes relacionados ao método calcular_bonus()
pytest -v -m calcular_bonus

# Gerar relatório de cobertura de testes em hmtl
pytest --cov=codigo tests/ --cov-report html

# Gerar relatório de testes em xml
pytest --junitxml report.xml

# Gerar relatório de cobertura de testes em xml
pytest --cov-report xml
```
