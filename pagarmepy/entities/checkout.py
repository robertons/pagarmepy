# -*- coding: utf-8 -*-
from .lib import *

class Checkout(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.accepted_payment_methods = Obj(context=cls, key='accepted_payment_methods', name='str')
		cls.accepted_multi_payment_methods = Obj(context=cls, key='accepted_payment_methods', name='str')
		cls.default_payment_method = String(max=40)
		cls.success_url = String(max=256)
		cls.debit_card = Obj(context=cls, key='debit_card', name='DebitCard')
		cls.credit_card = Obj(context=cls, key='credit_card', name='CreditCard')
		cls.boleto = Obj(context=cls, key='boleto', name='Boleto')
		cls.skip_checkout_success_page = Boolean()
		cls.customer_editable = Boolean()
		cls.metadata = Dict()
		cls.bank_transfer = Obj(context=cls, key='bank_transfer', name='BankTransfer')
		cls.expires_in = Int()
		cls.billing_address_editable = Boolean()
		cls.billing_address = Obj(context=cls, key='billing_address', name='Address')
		cls.voucher = Obj(context=cls, key='voucher', name='Voucher')
		cls.pix = Obj(context=cls, key='pix', name='Pix')

		super().__init__(**kw)
