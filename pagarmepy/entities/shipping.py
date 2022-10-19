# -*- coding: utf-8 -*-
from .lib import *

class Shipping(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.amount = Int()
		cls.description = String(max=25)
		cls.recipient_name =  String(max=25)
		cls.recipient_phone =  String(max=25)
		cls.address = Obj(context=cls, key='address', name='Address')
		cls.max_delivery_date =  DateTime(format="%Y-%m-%d")
		cls.estimated_delivery_date = DateTime(format="%Y-%m-%d")
		cls.type = String(max=25)

		super().__init__(**kw)
