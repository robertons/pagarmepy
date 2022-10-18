# -*- coding: utf-8 -*-
from .lib import *

class Address(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers/{customer_id}/addresses'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.line_1 = String(max=150)
		cls.line_2 = String(max=150)
		cls.city = String(max=25, required=True)
		cls.state = String(max=6, required=True)
		cls.country = String(max=2, required=True)
		cls.zip_code = String(max=8, required=True)
		cls.status = String(max=15)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.metadata = Dict()

		super().__init__(**kw)
