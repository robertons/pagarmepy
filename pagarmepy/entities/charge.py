# -*- coding: utf-8 -*-
from .lib import *

class Charge(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)
		cls.code = String(max=25)
		cls.gateway_id = String(max=25)
		cls.amount = Int()
		cls.payment_method = String(max=25)
		cls.status = String(max=25)
		cls.due_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.invoice = Obj(context=cls, key='invoice', name='Invoice')
		cls.last_transaction = Obj(context=cls, key='last_transaction', name='Transaction')
		cls.metadata = Dict()


		super().__init__(**kw)
