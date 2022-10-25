# -*- coding: utf-8 -*-
from .lib import *

class Discount(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=40)
		cls.value = Int()
		cls.discount_type = String(max=40)
		cls.cycles = Int()
		cls.item_id = String(max=40)
		cls.status = String(max=40)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")

		super().__init__(**kw)
