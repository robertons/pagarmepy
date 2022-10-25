# -*- coding: utf-8 -*-
from .lib import *

class Cycle(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/subscriptions/{subscription_id}/cycles'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=25)
		cls.billing_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.cycle = Int()
		cls.start_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.end_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.duration = Int()
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.status = String(max=56)
		cls.metadata = Dict()

		super().__init__(**kw)

	def Renew(self, **kw):
		if hasattr(self, '__route__'):
			addHeader, route = self.FormatRoute(False, **kw)
			response = Post(route, self.toJSON(), addHeader)
			self.load(**response)
		else:
			raise Exception("Method Post not allowed this object")
		return self
