# SDK Python3 para Integração com Pagar.ME

Esta SDK foi desenvolvida para abstrair aos desenvolvedores os principais detalhes da comunicação com API v5 da Pagar.ME tanto em produção quanto ambiente sandbox.

Você pode acessar a documentação base da api aqui: [Api V5 Pagar.ME](https://docs.pagar.me/reference/).

![Licença](https://img.shields.io/github/license/robertons/pagarmepy) ![image](https://img.shields.io/pypi/v/pagarmepy) ![image](https://img.shields.io/pypi/status/pagarmepy) ![image](https://img.shields.io/badge/python-v3.7-blue) ![image](https://img.shields.io/badge/build-passing-brightgreen) ![image](https://img.shields.io/badge/coverage-100%25-brightgreen) ![image](https://img.shields.io/github/last-commit/robertons/pagarmepy)

# Instalação
Instalação utilizando Pip
```bash
pip install pagarmepy
```
Git/Clone
```
git clone https://github.com/robertons/pagarmepy
cd pagarme
pip install -r requirements.txt
python setup.py install
```
# Objetos

Os objetos neste SDK podem ser criados em 3 (três) formas distintas a critério do utilizador.

## Criação

**Método 1 - Construtor**
```python
objeto = Objeto(campo1 = 'valor', campo2 = 'valor 2', campo_datetime = datetime.now(), campo_float = 10.1)
```
**Método 2 - Construtor com Dict**
```python
objeto = Objeto(**{'campo1':'valor', 'campo2':'valor 2', 'campo_datetime':datetime.now(), 'campo_float' = 10.1})
```
**Método 3 - Preenchimento Individual de Campos**
```python
objeto = Objeto()
objeto.campo1 = 'valor'
objeto.campo2 = 'valor 2'
objeto.campo_datetime = datetime.now()
objeto.campo_float = 10.1
```
##  Método toJSON

Método toJSON() retorna os dados do Objeto em formato *dicionário* não codificados.

```python
objeto = Objeto(...)
print(objeto.toJSON())
```

## Configuração Inicial
|posição  | campo |  obrigatório | padrão | descrição |
|--|--|--|--|--|
| 1 | idAccount | **sim** |  |ID da Conta Pagar.ME
| 2 | publicKey | **sim** |  | Chave Pública
| 3 | privateKey | **sim** |  | Chave Secreta
| 4 | sandbox | **não** | **False** | Ambiente Produção/Sandbox
| 5 | debug | **não** | **False** | Depuração de Request Post, Get, Put, Patch e Delete e Resposta Pagar.ME

```python
import pagarme

pagarmepy.PagarMe('idAccount', 'publicKey', 'privateKey', sandbox=True)
```

**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/autentica%C3%A7%C3%A3o-2)**


## Suporte Oficial da Pagar.ME

Em caso de dúvidas, problemas ou sugestões:  [relacionamento@pagar.me](mailto:relacionamento@pagar.me)

## Change log

Veja em  [CHANGELOG](CHANGELOG.md) para maiores informações sobre as mudanças recentes

## Contribuições

As contribuições  por meio de `Pull Requests` são bem-vindas e serão totalmente creditadas.

## Segurança

Se você descobrir qualquer problema relacionado à segurança, envie um e-mail para robertonsilva@gmail.com

## Créditos

- Autor [Roberto Neves](https://github.com/robertons)

## Licença
Veja em  [LICENÇA](LICENSE) para maiores informações sobre a licença de uso.
