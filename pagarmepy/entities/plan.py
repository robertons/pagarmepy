# -*- coding: utf-8 -*-
from .lib import *

class Plan(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/plans'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.name = String(max=26)
		cls.description = String(max=256)
		cls.currency = String(max=100)
		cls.interval = String(max=100)
		cls.interval_count = Int()
		cls.minimum_price = Int()
		cls.billing_type = String(max=100)
		cls.billing_days = ObjList(context=cls, key='billing_days', name='int')
		cls.payment_methods = ObjList(context=cls, key='payment_methods', name='str')
		cls.installments = ObjList(context=cls, key='installments', name='int')
		cls.pricing_scheme = Obj(context=cls, key='pricing_scheme', name='PricingScheme')
		cls.statement_descriptor = String(max=100)
		cls.trial_period_days = Int()
		cls.status = String(max=100)
		cls.shippable = Boolean()
		cls.quantity = Int()
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.items = ObjList(context=cls, key='items', name='Item')
		cls.metadata = Dict()

		super().__init__(**kw)

	def ChangeMetadata(self, **kw):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/metadata", {'metadata': kw}, addHeader)
		self.load(**response)
		return self
