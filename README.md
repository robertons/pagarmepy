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

##  Operações em Centavos

Todos os campos referente a valores operacionais Pagar.Me são em centavos as funções abaixo facilitam a conversão e reversão em caso dos Webhooks para utilização dos valores em outros formatos.

### Qualquer valor em Float ou Decimal para Centavos Inteiro
```python
  valor_centavos_int = pagarmepy.DecimalToCents(valor)
```

### Qualquer Inteiro em centavos para Float
```python
  valor_float = pagarmepy.CentsToFloat(valor)
```

### Qualquer Inteiro em centavos para Decimal (decimal.Decimal)
```python
  valor_decimal = pagarmepy.CentsToDecimal(valor)
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

### Obter
```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Get()
```

### Capturar Valor Integral

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Capture()
```

### Capturar Valor Parcial

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Capture(amount=10)
```

### Editar cartão de cobrança

```python
  cobranca = pagarmepy.Charge(id="ch_Pr5R4D5izhEbyNQY").ChangeCard(pagarmepy.Card(
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
      })))
```

### Editar data de vencimento da cobrança

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").ChangeDueDate('2022-10-21')
```


### Editar método de pagamento

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").ChangePaymentMethod(pagarmepy.Payment(**{
         "amount" : 3000,
         "payment_method":"boleto",
         "boleto": {
            "instructions": "Instrução de boleto de teste",
            "due_at" : "2022-10-20T14:30:22",
            "document_number" : "123456",
            "type": "DM"
         }
    }))
```

```python
 cobranca = pagarmepy.Charge(id="ch_Pr5R4D5izhEbyNQY").ChangePaymentMethod(pagarmepy.Payment(**{
       "amount" : 3000,
       "payment_method":"credit_card",
       "credit_card": {
          'card_id': "card_G4QnR6ck7cgBn8XR",
       }
  }))
```

### Cancelar Cobrança

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Delete()
```

### Listar

```python
  cobrancas = pagarmepy.Charge().List()
```

### Retentar uma cobrança manualmente

```python
  cobranca =  pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Retry()
```


### Confirmar cobrança (cash)

```python
  cobranca = pagarmepy.Charge(id="ch_Rz8oL2vcjwc3D1OQ").Confirm()
```

# RECORRÊNCIA

**Mais detalhes em [Documentação Oficial](https://docs.pagar.me/reference/vis%C3%A3o-geral-da-recorr%C3%AAncia)**

## PLANOS

### Criar

```python
plano = pagarmepy.Plan()
  plano.name = "Plano Mensal Teste"
  plano.description = "Plano de teste de integração API"
  plano.shippable = False
  plano.payment_methods.add('credit_card')
  plano.statement_descriptor = 'Assinatura'
  plano.currency = 'BRL'
  plano.interval = 'month'
  plano.interval_count = 1
  plano.billing_type = 'prepaid'
  plano.quantity = 1
  plano.pricing_scheme = pagarmepy.PricingScheme(**{
          "scheme_type": "unit",
          "price": 5000,
          "minimum_price": 5000,
      })
  plano.Create()
```

### Obter

```python
  plano = pagarmepy.Plan(id="plan_ODjw15Af9WUgzwkg").Get()
```

### Listar

```python
  plano = pagarmepy.Plan().List()
```

### Excluir

```python
  pagarmepy.Plan(id="plan_ODjw15Af9WUgzwkg").Delete()
```

### Atualizar

```python
  plano = pagarmepy.Plan(id="plan_ODjw15Af9WUgzwkg").Get()
  plano.statement_descriptor = "AST Test"
  plano.Update()
```

### Modificar Metadata

```python
plano = pagarmepy.Plan(id="plan_VR92ne8UEUGWNMAa").ChangeMetadata(
      campo1 = 'valor 1',
      campo2 = 'valor 2',
      camponumero = 3
  )
```


## Items do Plano

### Adicionar Item

```python
  items_planos = pagarmepy.Plan(id="plan_brJdw1jTlTa89zyQ").AddItem(pagarmepy.Item(**{
          "description": "Chaveiro do Alternativo",
          "quantity": 1,
          "pricing_scheme": {
              "price": 2000,
              "scheme_type": "unit"
          }
      }))
```

### Atualizar Item

```python
  items_planos = pagarmepy.Plan(id="plan_brJdw1jTlTa89zyQ").UpdateItem(pagarmepy.Item(**{
          "id": "pi_d478RMAS3bC74PrL",
          "description": "Chaveiro do Tesseract Antigo",
          "status": "active",
          "quantity": 1,
          "pricing_scheme": {
              "price": 3000,
              "scheme_type": "unit"
          }
      }))
```

### Excluir Item

```python
  pagarmepy.Plan(id="plan_brJdw1jTlTa89zyQ").DeleteItem("pi_d478RMAS3bC74PrL")
```

## ASSINATURAS

### Criar Assinatura Avulsa

```python
  assinatura = pagarmepy.Subscription()
  assinatura.code = '1234'
  assinatura.customer_id = "cus_bjgeDobsLsEO48nw"
  assinatura.interval = 'month'
  assinatura.interval_count = 1
  assinatura.currency = 'BRL'
  assinatura.payment_method = "credit_card"
  assinatura.billing_type = 'prepaid'
  assinatura.installments = 1
  assinatura.statement_descriptor = "AST Gofans"
  assinatura.items.add(pagarmepy.Item(**{
          "id": "oi_d478RMAS3bC74PrL",
          "description": "Chaveiro do Tesseract",
          "amount": 2900,
          "quantity": 1,
          "status": "active",
          "code":"abc",
          "pricing_scheme":{
              "scheme_type": "Unit",
              "price": 2900
          }
      }))
  assinatura.card = pagarmepy.Card(**{
      "number": "4000000000000010",
      "holder_name": "Tony Stark",
      "exp_month": 1,
      "exp_year": 30,
      "cvv": "3531",
      "billing_address": {
          "line_1": "10880, Malibu Point, Malibu Central",
          "zip_code": "90265",
          "city": "Malibu",
          "state": "CA",
          "country": "US"
      }
  })

  assinatura.Create()
```

### Criar Assinatura de um Plano

```python
  assinatura = pagarmepy.Subscription()
  assinatura.code = '1234'
  assinatura.customer_id = "cus_bjgeDobsLsEO48nw"
  assinatura.plan_id = "plan_VR92ne8UEUGWNMAa"
  assinatura.interval = 'month'
  assinatura.interval_count = 1
  assinatura.currency = 'BRL'
  assinatura.payment_method = "credit_card"
  assinatura.billing_type = 'prepaid'
  assinatura.installments = 1
  assinatura.statement_descriptor = "AST Gofans"    
  assinatura.card = pagarmepy.Card(**{
      "number": "4000000000000010",
      "holder_name": "Tony Stark",
      "exp_month": 1,
      "exp_year": 30,
      "cvv": "3531",
      "billing_address": {
          "line_1": "10880, Malibu Point, Malibu Central",
          "zip_code": "90265",
          "city": "Malibu",
          "state": "CA",
          "country": "US"
      }
  })

  assinatura.Create()
```

### Obter

```python
  assinaturas = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").Get()
```

### Listar

```python
  assinaturas = pagarmepy.Subscription().List()
```

### Cancelar

```python
  assinaturas = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").Delete()
```


### Editar cartão da assinatura

```python
  assinatura = pagarmepy.Subscription(id="sub_Gdg4m3BTrqTyoK01").ChangePaymentMethod(pagarmepy.Payment(**{
       "payment_method":"credit_card",
       'card_id': "card_G4QnR6ck7cgBn8XR",
  }))
```

### Editar metadados da assinatura

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").ChangeMetadata(
      campo1 = 'valor 1',
      campo2 = 'valor 2',
      camponumero = 3
  )
```

### Editar meio de pagamento da assinatura

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").ChangePaymentMethod(pagarmepy.Payment(**{
         "payment_method":"boleto",
         "boleto": {
            "instructions": "Instrução de boleto de teste",
            "due_at" : "2022-10-20T14:30:22",
            "document_number" : "123456",
            "type": "DM"
         }
    }))
```
ou

```python
 assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").ChangePaymentMethod(pagarmepy.Payment(**{
       "payment_method":"credit_card",
       "credit_card": {
          'card_id': "card_G4QnR6ck7cgBn8XR",
       }
  }))
```

### Editar data de início da assinatura

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").ChangeStarteDate('2022-10-21')
```


### Editar preço mínimo da assinatura

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").ChangeMinimumPrice(10000)
```


### Ativar faturamento manual

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").SetManualBilling(True)
```


### Desativar faturamento manual

```python
  assinatura = pagarmepy.Subscription(id="sub_9ZVy143Hd1HODql1").SetManualBilling(False)
```


## Items de Assinatura

### Adicionar Item

```python
  items_asssinaturas = pagarmepy.Subscription(id="sub_brJdw1jTlTa89zyQ").AddItem(pagarmepy.Item(**{
          "description": "Chaveiro do Alternativo",
          "quantity": 1,
          "pricing_scheme": {
              "price": 2000,
              "scheme_type": "unit"
          }
      }))
```

### Atualizar Item

```python
  items_asssinaturas = pagarmepy.Subscription(id="sub_brJdw1jTlTa89zyQ").UpdateItem(pagarmepy.Item(**{
          "id": "oi_d478RMAS3bC74PrL",
          "description": "Chaveiro do Tesseract Antigo",
          "status": "active",
          "quantity": 1,
          "pricing_scheme": {
              "price": 3000,
              "scheme_type": "unit"
          }
      }))
```

### Listar Items

```python
  items_asssinaturas = pagarmepy.Subscription(id="sub_brJdw1jTlTa89zyQ").ListItems()
```

### Excluir Item

```python
  pagarmepy.Subscription(id="sub_brJdw1jTlTa89zyQ").DeleteItem("oi_d478RMAS3bC74PrL")
```

## Uso de Items de Assinatura

### Incluir Uso

```python
  uso = pagarmepy.Usage()
  uso.quantity = 1
  uso.description = "Uso de teste"
  uso.Create(subscription_id="sub_brJdw1jTlTa89zyQ", item_id="si_Ww2DP2eHzHnolqbn")
```

### Remover Uso

```python
  pagarmepy.Usage(id="usage_2VBDB53fWfjgnZpX").Delete(subscription_id="sub_1VRDB5AfWfjBnZpx", item_id="si_QjGb0BZUkUD0Eyag")
```

### Listar Uso

```python
  usos = pagarmepy.Usage().List(subscription_id="sub_1VRDB5AfWfjBnZpx", item_id="si_QjGb0BZUkUD0Eyag")
```


## Descontos

### Incluir

```python
  desconto = pagarmepy.Discount()
  desconto.uso.value = 100
  desconto.increment_type = 'flat'
  desconto.Create(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Obter

```python
  desconto = pagarmepy.Discount(id="dis_2VBDB53fWfjgnZpX").Get(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Remover

```python
  pagarmepy.Discount(id="dis_2VBDB53fWfjgnZpX").Delete(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Listar

```python
  descontos = pagarmepy.Discount().List(subscription_id="sub_brJdw1jTlTa89zyQ")
```


## Incremento

### Incluir

```python
  incremento = pagarmepy.Increment()
  desconto.uso.value = 100
  desconto.increment_type = 'flat'
  desconto.Create(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Obter

```python
  incremento = pagarmepy.Increment(id="inc_2VBDB53fWfjgnZpX").Get(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Remover

```python
  pagarmepy.Increment(id="inc_2VBDB53fWfjgnZpX").Delete(subscription_id="sub_brJdw1jTlTa89zyQ")
```

### Listar

```python
  incrementos = pagarmepy.Increment().List(subscription_id="sub_brJdw1jTlTa89zyQ")
```


## Modificar Regras Split


```python
  assinatura = pagarmepy.Subscription()
  assinatura.id = "sub_brJdw1jTlTa89zyQ"
  assinatura.split.add(pagarmepy.Split(**{
                "amount": 50,
                "recipient_id": "rp_n9voQ2QT0SQrMwOL",
                "type": "percentage",
                "options": {
                    "charge_processing_fee": True,
                    "charge_remainder_fee": True,
                    "liable": True
                }
            }))

  assinatura.split.add(pagarmepy.Split(**{
                "amount": 50,
                "type": "percentage",
                "recipient_id": "rp_6gyn5oIvAcwjrNej",
                "options": {
                    "charge_processing_fee": False,
                    "charge_remainder_fee": False,
                    "liable": False
                }
            }))

  assinatura.ChangeSplitRule(enabled=True)
```



## Ciclos

### Renovar Ciclo

```python
  ciclo = pagarmepy.Cycle(id="cycle_brJdw1jTlTa89zyQ").Renew()
```

### Obter

```python
  ciclos = pagarmepy.Cycle(id="cycle_VWk4gY6TMPHN7A0g").Get(subscription_id="sub_9ZVy143Hd1HODql1")
```

### Listar

```python
  ciclos = pagarmepy.Cycle().List(subscription_id="sub_9ZVy143Hd1HODql1")
```

## Faturas

### Criar

```python
  fatura = pagarmepy.Invoice().Create(subscription_id='sub_brJdw1jTlTa89zyQ', cycle_id='cycle_v0dxrO3i2iyr5J9X')
```

### Obter

```python
  fatura = pagarmepy.Invoice(id="in_VWk4gY6TMPHN7A0g").Get()
```

### Listar

```python
  fatura = pagarmepy.Invoice().List()
```

### Modificar Metadata

```python
  fatura = pagarmepy.Invoice(id="in_VWk4gY6TMPHN7A0g").ChangeMetadata(
      campo1 = 'valor 1',
      campo2 = 'valor 2',
      camponumero = 3
  )
```

### Cancelar Fatura

```python
  fatura = pagarmepy.Invoice(id="in_VWk4gY6TMPHN7A0g").Delete()
```


## Recebedores

### Criar

```python
  recebedor = pagarmepy.Recipient()
  recebedor.name = 'Joao da Silva'
  recebedor.email = "joaodasilva@gmail.com"
  recebedor.document = '000011233000'
  recebedor.description = 'Recebedor teste de cadastro'
  recebedor.type = 'individual'
  recebedor.default_bank_account = pagarmepy.BankAccount(**{
      "holder_name": "Joao da Silva",
      "holder_type": "individual",
      "holder_document": '000011233000',
      "bank": "033",
      "type": "checking",
      "branch_number": "4444",
      "branch_check_digit": "0",
      "account_number": "11223344",
      "account_check_digit": "5",
  })
  recebedor.Create()
  print(recebedor.toJSON())
```

### Obter

```python
  recebedor = pagarmepy.Recipient(id="rp_JPx17b8H9HgwY5zo").Get()
```

### Atualizar

```python
  recebedor = pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").Get()
  recebedor.description = "Descrição Alterada de Recebedor"
  recebedor.Update()
```

### Listar

```python
  recebedores = pagarmepy.Recipient().List()
```

### Saldo

```python
  saldo = pagarmepy.Recipient(id="rp_JPx17b8H9HgwY5zo").GetBalance()
```

### Alterar Conta Bancária Padrão

```python
  recebedor = pagarmepy.Recipient(id="rp_JPx17b8H9HgwY5zo").ChangeDefaultBankAccount(pagarmepy.BankAccount(**{
      "holder_name": "Roberto Neves da Silva",
      "holder_type": "individual",
      "holder_document": '09292800752',
      "bank": "033",
      "type": "checking",
      "branch_number": "4316",
      "branch_check_digit": "0",
      "account_number": "01001647",
      "account_check_digit": "3",
  }))  
```
### Alterar Configurações de Transferência

```python
  recebedor = pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").ChangeTransferSettings(transfer_enabled=True, transfer_interval="monthly", transfer_day="1")
```

### Alterar Configurações de Antecipação de Recebíveis

```python
  pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").ChangeAnticipationSettings(enabled=True, type="full", volume_percentage="100", days=["1","2"], delay="1")
```

### Criar Saque

```python
saque = pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").DoWithdraw(100)
```

### Obter Saque

```python
saque = pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").GetWithdraw("with_LR4Wxpqt68ul2W9M")
```

### Listar Saques

```python
  saques = pagarmepy.Recipient(id="rp_WGAn6Q4SySWZBlRy").ListWithdrawals()
```

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
