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
cd pagarmepy
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
import pagarmepy

pagarmepy.PagarMe('idAccount', 'publicKey', 'privateKey', sandbox=True)
```

**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/autentica%C3%A7%C3%A3o-2)**

## Cliente

### Criar

```python
  cliente = pagarmepy.Customer()
  cliente.name = 'Fulano Beltrano'
  cliente.email = 'fulano@email.com'
  cliente.birthdate = '1980-01-30'
  cliente.phones = pagarmepy.Phones(**{'mobile_phone': { "country_code": 55, "area_code": 27, "number": 999999999}})
  cliente.Create()

```

### Obter
```python
	cliente = pagarmepy.Customer(id='cus_bjgeDobdLsEO48nw').Get()
```

### Atualizar


```python
  cliente = pagarmepy.Customer(id='cus_bjgeDobsLsEO48nw').Get()
  cliente.address = pagarmepy.Address(line_1='Rua Capitao Domingos Correa da Rocha, 80, Sala 116', line_2='Ed Master Place, Santa Lucia', city='Vitória', state='ES', country='BR', zip_code='29056220')
  client.Update()
```

### Listar

```python
  clientes = pagarmepy.Customer().List(filters={'page':1, 'size':10, 'gender':'female'})
```
**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/clientes-1)**



## Cartões

### Criar

```python
  card = pagarmepy.Card()
  card.first_six_digits = "400000"
  card.last_four_digits = "0010"
  card.brand = "Mastercard"
  card.holder_name = "Tony Stark"
  card.holder_document = "93095135270"
  card.number = "4000000000000010"
  card.exp_month = 1
  card.exp_year = 2030
  card.cvv = 123
  card.billing_address = pagarmepy.Address(**{
    "zip_code": "22000111",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "country": "BR",
    "line_1": "375, Av. General Osorio, Centro",
    "line_2": "7º Andar"
  })
  card.Create(customer_id='cus_bjgeDobsLsEO48nw')

```

### Obter
```python
	card = pagarmepy.Card(id="card_MJYE2GDSLHjjkawL").Get(customer_id="cus_bjgeDobsLsEO48nw")
```

### Atualizar

```python
  card = pagarmepy.Card(id="card_MJYE2GDSLHjjkawL").Get(customer_id="cus_bjgeDobsLsEO48nw")
  card.exp_month = 2
  card.exp_year = 2035
  card.billing_address = pagarmepy.Address(**{'line_1':'Rua Capitao Domingos Correa da Rocha, 80, Sala 116', 'line_2':'Ed Master Place, Santa Lucia', 'city':'Vitória', 'state':'ES', 'country':'BR', 'zip_code':'29056220'})
  card.Update(customer_id="cus_bjgeDobsLsEO48nw")
  print(card.toJSON())
```

### Listar

```python
  cards = pagarmepy.Card().List(customer_id='cus_bjgeDobsLsEO48nw')
```

### Excluir

```python
  pagarmepy.Card(id="card_MJYE2GDSLHjjkawL").Delete(customer_id="cus_bjgeDobsLsEO48nw")
```

### Renovar

```python
  card = pagarmepy.Card(id="card_G4QnR6ck7cgBn8XR").Renew(customer_id="cus_bjgeDobsLsEO48nw")
```


### Criar Token

```python
  token = pagarmepy.Token()
  token.type = "card"
  token.card = pagarmepy.Card(
      first_six_digits = "400000",
      last_four_digits = "0010",
      brand = "Mastercard",
      holder_name = "Tony Stark",
      holder_document = "93095135270",
      number = "4000000000000010",
      exp_month = 1,
      exp_year = 2030,
      cvv = 123,
      billing_address = pagarmepy.Address(**{
        "zip_code": "22000111",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "country": "BR",
        "line_1": "375, Av. General Osorio, Centro",
        "line_2": "7º Andar"
      })
  )

  token.Create(appId='pk_test_Y479412hrHMQ956j')
```

**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/cart%C3%B5es-1)**

## Endereços

### Criar

```python
  address = pagarmepy.Address(**{
    "zip_code": "22000111",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "country": "BR",
    "line_1": "375, Av. General Osorio, Centro",
    "line_2": "7º Andar"
  })
  address.Create(customer_id='cus_bjgeDobsLsEO48nw')

```

### Obter
```python
  address = pagarmepy.Address(id="addr_lOAgNqH1wCxD6eYd").Get(customer_id="cus_bjgeDobsLsEO48nw")
```

### Atualizar

```python
  address = pagarmepy.Address(id="addr_BNwDJk2TPTmXGArR").Get(customer_id="cus_bjgeDobsLsEO48nw")
  address.line_2 = 'Master Place, Itararé'
  address.Update(customer_id='cus_bjgeDobsLsEO48nw')
```

### Listar

```python
  addresses = pagarmepy.Address().List(customer_id='cus_bjgeDobsLsEO48nw')
```

### Excluir

```python
  pagarmepy.Address(id="addr_lOAgNqH1wCxD6eYd").Delete(customer_id="cus_bjgeDobsLsEO48nw")
```

## BIN

Os seis primeiros dígitos de um número de cartão (incluindo o dígito MII inicial) são conhecidos como o número de identificação do emissor (IIN) ou número de identificação do banco (BIN). Estes números identificam a instituição que emitiu o cartão ao titular do cartão. O restante do número é alocado pelo emissor. Para obter as informações do Emissor:

### Obter

```python
  bin = pagarmepy.BIN().Get(bin='555566')
```

## PEDIDOS

Veja a documentação oficial para pedidos com pagamentos multimeios, pedidos com multicompradores.

**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/pedidos-1)**


### Criar

Exemplo Pedido com Checkout:

```python
  pedido = pagarmepy.Order()
  pedido.customer_id = "cus_bjgeDobsLsEO48nw"
  pedido.code =  "62LVFN7I4R"
  pedido.amount = 2900
  pedido.currency =  "BRL"
  pedido.items.add(pagarmepy.Item(**{
          "id": "oi_d478RMAS3bC74PrL",
          "description": "Chaveiro do Tesseract",
          "amount": 2900,
          "quantity": 1,
          "status": "active",
          "code":"abc"
      }))

  pedido.shipping = pagarmepy.Shipping(**{
      "amount": 100,
      "description": "Stark",
      "recipient_name": "Tony Stark",
      "recipient_phone": "24586787867",
      "address": {
          "line_1": "10880, Malibu Point, Malibu Central",
          "zip_code": "90265",
          "city": "Malibu",
          "state": "CA",
          "country": "US"
      }})

  pedido.payments.add(pagarmepy.Payment(**{
       "amount" : 3000,
       "payment_method":"checkout",
       "checkout": {
          "expires_in":120,
          "billing_address_editable" : False,
          "customer_editable" : False,
          "accepted_payment_methods": ["credit_card"],
          "success_url": "https://www.pagar.me",
       }
       }))

  pedido.Create()
```

### Obter
```python
  pedido = pagarmepy.Order(id="or_jP82N8VUpXhyYr4b").Get()
```

### Listar

```python
  pedidos = pagarmepy.Order().List(customer_id='cus_bjgeDobsLsEO48nw')
```


```python
  pedidos = pagarmepy.Order().List()
```

### Fechar um Pedido

```python
  pedido = pagarmepy.Order(id="or_jP82N8VUpXhyYr4b").Close()
```

### Excluir

```python
  pagarmepy.Address(id="addr_lOAgNqH1wCxD6eYd").Delete(customer_id="cus_bjgeDobsLsEO48nw")
```

## COBRANÇAS


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
