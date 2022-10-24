# -*- coding: utf-8 -*-
from .lib import *

class PricingScheme(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.price = Int()
		cls.mininum_price = Int()
		cls.scheme_type = String(max=30)
		cls.price_brackets =  ObjList(context=cls, key='price_brackets', name='PriceBracket')
		
		super().__init__(**kw)
