# -*- coding: utf-8 -*-
from .lib import *

class Customer(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.name = String(max=64)
		cls.email = String(max=64)
		cls.code = String(max=52)
		cls.document = String(max=16)
		cls.document_type = String(max=8)
		cls.type = String(max=10)
		cls.gender = String(max=6)
		cls.address = Obj(context=cls, key='address', name='Address')
		cls.phones = Obj(context=cls, key='phones', name='Phones')
		cls.birthdate = DateTime(format="%Y-%m-%d")
		cls.fb_id = Int()
		cls.fb_access_token = String(max=155)
		cls.metadata = Dict()
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.delinquent = Boolean()

		super().__init__(**kw)
