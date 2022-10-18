# -*- coding: utf-8 -*-
from .lib import *

class Card(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers/{customer_id}/cards'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.number = String(max=19)
		cls.last_four_digits = String(max=4)
		cls.first_six_digits = String(max=6)
		cls.brand =  String(max=52)
		cls.holder_name = String(max=64)
		cls.holder_document = String(max=16)
		cls.exp_month = Int()
		cls.exp_year = Int()
		cls.cvv = Int()
		cls.billing_address_id = String(max=26)
		cls.billing_address = Obj(context=cls, key='billing_address', name='Address')
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.private_label = Boolean()
		cls.type = String(max=16)
		cls.label = String(max=16)
		cls.token = String(max=255)
		cls.status = String(max=26)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.update_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.metadata = Dict()

		super().__init__(**kw)

	def Renew(self, **kw):
		if hasattr(self, '__route__'):
			addHeader, route = self.FormatRoute(True, **kw)
			response = Post(f"{route}/renew", self.toJSON(), addHeader)
			self.load(**response)
		else:
			raise Exception("Method Post not allowed this object")
		return self
