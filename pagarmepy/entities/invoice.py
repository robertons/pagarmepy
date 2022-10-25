# -*- coding: utf-8 -*-
from .lib import *

class Invoice(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/invoices'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=25)
		cls.url =  String(max=256)
		cls.amount = Int()
		cls.payment_method =  String(max=25)
		cls.installments = Int()
		cls.status =  String(max=25)
		cls.billing_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.seen_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.due_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.created_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.canceled_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.period = Obj(context=cls, key='period', name='Period')
		cls.items = ObjList(context=cls, key='items', name='Item')
		cls.subscription = Obj(context=cls, key='subscription', name='Subscription')
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.metadata  = Dict()
		cls.total_discount = Int()
		cls.total_increment = Int()

		super().__init__(**kw)

	def Create(self, **kw):
		if not 'subscription_id' in kw:
			raise Exception(f"Param (subscription_id) is required on method Create")
		if not 'cycle_id' in kw:
			raise Exception(f"Param (cycle_id) is required on method Create")
		data = Post(f"/subscriptions/{kw['subscription_id']}/cycles/{kw['cycle_id']}/pay", self.toJSON(), None)
		self.load(**data)
		return self

	def ChangeMetadata(self, **kw):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/metadata", {'metadata': kw}, addHeader)
		self.load(**response)
		return self
