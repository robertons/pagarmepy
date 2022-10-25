# -*- coding: utf-8 -*-
from .lib import *

class Usage(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/subscriptions/{subscription_id}/items/{item_id}/usages'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=40)
		cls.quantity = Int()
		cls.description = String(max=40)
		cls.status = String(max=40)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.used_at = DateTime(format="%Y-%m-%dT%H:%M:%S")

		super().__init__(**kw)
