# -*- coding: utf-8 -*-
from .lib import *

class Increment(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/subscriptions/{subscription_id}/increments'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=40)
		cls.value = Int()
		cls.increment_type = String(max=40)
		cls.cycles = Int()
		cls.item_id = String(max=40)
		cls.status = String(max=40)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")

		super().__init__(**kw)
