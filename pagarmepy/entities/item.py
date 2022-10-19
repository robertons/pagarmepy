# -*- coding: utf-8 -*-
from .lib import *

class Item(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)
		cls.amount = Int()
		cls.description = String(max=256)
		cls.quantity = Int()
		cls.code = String(max=25)
		cls.category = String(max=25)
		cls.status = String(max=25)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.order = Obj(context=cls, key='order', name='Order')

		super().__init__(**kw)
