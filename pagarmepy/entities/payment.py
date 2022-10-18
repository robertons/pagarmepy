# -*- coding: utf-8 -*-
from .lib import *

class Payment(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.payment_method = String(max=20)
		cls.credit_card = Obj(context=cls, key='credit_card', name='CreditCard')
		cls.debit_card = Obj(context=cls, key='debit_card', name='DebitCard')
		cls.voucher = Obj(context=cls, key='voucher', name='Voucher')
		cls.boleto = Obj(context=cls, key='boleto', name='Boleto')
		cls.bank_transfer = Obj(context=cls, key='bank_transfer', name='BankTransfer')
		cls.checkout = Obj(context=cls, key='checkout', name='Checkout')
		cls.cash = Obj(context=cls, key='cash', name='Cash')
		cls.pix = Obj(context=cls, key='pix', name='Pix')
		cls.amount = Int()
		cls.metadata = Dict()
		cls.gateway_affiliation_id = String(max=256)


		super().__init__(**kw)
