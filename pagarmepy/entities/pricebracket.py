# -*- coding: utf-8 -*-
from .lib import *

class PriceBracket(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.start_quantity = Int()
		cls.end_quantity = Int()
		cls.overage_price = Int()
		cls.price = Int()


		super().__init__(**kw)
