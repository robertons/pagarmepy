# -*- coding: utf-8 -*-
from .lib import *
from pagarmepy.entities.creditcard import CreditCard
from pagarmepy.entities.payment import Payment
from pagarmepy.entities.item import Item

class Subscription(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/subscriptions'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=40)
		cls.code = String(max=40)
		cls.payment_method = String(max=40)
		cls.currency = String(max=4)
		cls.start_at =  DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.interval = String(max=20)
		cls.interval_count = Int()
		cls.billing_type = String(max=20)
		cls.billing_day = Int()
		cls.current_period = Obj(context=cls, key='current_period', name='Period')
		cls.next_billing_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.installments = Int()
		cls.statement_descriptor = String(max=20)
		cls.customer_id = String(max=26)
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.plan_id  = String(max=26)
		cls.plan = Obj(context=cls, key='plan', name='Plan')
		cls.card = Obj(context=cls, key='card', name='Card')
		cls.discounts = ObjList(context=cls, key='discounts', name='Discount')
		cls.increments = ObjList(context=cls, key='increments', name='Increment')
		cls.setup = Obj(context=cls, key='setup', name='Setup')
		cls.minimum_price = Int()
		cls.items = ObjList(context=cls, key='items', name='Item')
		cls.status = String(max=56)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.canceled_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.metadata = Dict()
		cls.gateway_affiliation_id = String(max=156)
		cls.split = ObjList(context=cls, key='split', name='Split')
		cls.current_cycle = Obj(context=cls, key='current_cycle', name='Cycle')

		super().__init__(**kw)

	def ChangeCard(self, creditcard:CreditCard):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/card", {'card': creditcard.toJSON()}, addHeader)
		self.load(**response)
		return self

	def ChangeMetadata(self, **kw):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/metadata", {'metadata': kw}, addHeader)
		self.load(**response)
		return self

	def ChangePaymentMethod(self, payment:Payment):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/payment-method", payment.toJSON(), addHeader)
		self.load(**response)
		return self

	def ChangeSplitRule(self, enabled:bool):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/split", {'enabled': enabled, 'rules': self.split}, addHeader)
		self.load(**response)
		return self

	def ChangeStarteDate(self, start_at:str):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/start-at", {'start_at': start_at}, addHeader)
		self.load(**response)
		return self

	def ChangeMinimumPrice(self, minimum_price:int):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/minimum_price", {'minimum_price': minimum_price}, addHeader)
		self.load(**response)
		return self

	def SetManualBilling(self, active:bool):
		addHeader, route = self.FormatRoute(True, **{})
		if active:
			response = Post(f"{route}/manual-billing", {}, addHeader)
		else:
			response = Delete(f"{route}/manual-billing", addHeader)
		self.load(**response)
		return self

	def AddItem(self, item:Item):
		addHeader, route = self.FormatRoute(True, **{})
		response = Post(f"{route}/items", item.toJSON(), addHeader)
		return Item(**response)

	def UpdateItem(self, item:Item):
		addHeader, route = self.FormatRoute(True, **{})
		response = Put(f"{route}/items/{item.id}", item.toJSON(), addHeader)
		return Item(**response)

	def DeleteItem(self, item_id:String):
		addHeader, route = self.FormatRoute(True, **{})
		response = Delete(f"{route}/items/{item_id}", addHeader)
		return None

	def ListItems(self, filters=None, **kw):
		if hasattr(self, '__route__'):
			addHeader, route = self.FormatRoute(True, **kw)
			qs =''
			if filters:
				qs = '?' + '&'.join([f'{k}={v}' for k,v in filters.items()])
			route = f"{route}/items{qs}"
			response = Get(route, addHeader)
			return ListType(Item).add([Item(**item) for item in response['data']]) if 'data' in response else ListType(Item)
		else:
			raise Exception(f"[{self.__class__.__name__}] Method Get not allowed this object")
		return self
