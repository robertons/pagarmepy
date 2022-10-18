# -*- coding: utf-8 -*-
from .lib import *

class CreditCard(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.installments = Int()
		cls.statement_descriptor = String(max=13)
		cls.operation_type = String(max=20)
		cls.card = Obj(context=cls, key='card', name='Card')
		cls.card_id = String(max=40)
		cls.card_token = String(max=40)
		cls.network_token = String(max=40)
		cls.recurrence = Boolean()
		cls.metadata = Dict()
		cls.extended_limit_enabled = Boolean()
		cls.extended_limit_code = String(max=30)
		cls.merchant_category_code = Int()
		cls.authentication = Obj(context=cls, key='authentication', name='Authentication')
		cls.capture = Boolean()
		cls.auto_recovery = Boolean()
		cls.payload = Dict()


		super().__init__(**kw)
