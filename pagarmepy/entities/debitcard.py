# -*- coding: utf-8 -*-
from .lib import *

class DebitCard(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.statement_descriptor = String(max=22)
		cls.card = Obj(context=cls, key='card', name='Card')
		cls.card_id = String(max=40)
		cls.card_token = String(max=40)
		cls.recurrence = Boolean()
		cls.merchant_category_code = Int()
		cls.authentication = Obj(context=cls, key='authentication', name='Authentication')
		cls.payload = Dict()
		cls.metadata = Dict()

		super().__init__(**kw)
