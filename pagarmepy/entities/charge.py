# -*- coding: utf-8 -*-
from .lib import *
from pagarmepy.entities.payment import Payment
from pagarmepy.entities.creditcard import CreditCard

class Charge(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/charges'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=25)
		cls.code = String(max=55)
		cls.gateway_id = String(max=25)
		cls.amount = Int()
		cls.paid_amount = Int()
		cls.paid_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.currency =  String(max=25)
		cls.payment_method = String(max=25)
		cls.status = String(max=25)
		cls.due_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.invoice = Obj(context=cls, key='invoice', name='Invoice')
		cls.last_transaction = Obj(context=cls, key='last_transaction', name='Transaction')
		cls.order = Obj(context=cls, key='order', name='Order')
		cls.metadata = Dict()


		super().__init__(**kw)

	def Capture(self, **kw):
		addHeader, route = self.FormatRoute(True, **kw)
		data = {}
		if 'amount' in kw:
			data['amount'] = kw['amount']
		if 'code' in kw:
			data['code'] = kw['code']
		if 'split' in kw:
			data['split'] = kw['split']
		response = Post(f"{route}/capture", data, addHeader)
		self.load(**response)
		return self

	def ChangeCard(self, creditcard:CreditCard):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/card", {'card': creditcard.toJSON()}, addHeader)
		self.load(**response)
		return self

	def ChangeDueDate(self, due_at:str):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/due-date", {'due_at': due_at}, addHeader)
		self.load(**response)
		return self

	def ChangePaymentMethod(self, payment:Payment):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/payment-method", payment.toJSON(), addHeader)
		self.load(**response)
		return self

	def Retry(self):
		addHeader, route = self.FormatRoute(True, **{})
		response = Post(f"{route}/retry", {}, addHeader)
		self.load(**response)
		return self

	def Confirm(self):
		addHeader, route = self.FormatRoute(True, **{})
		response = Post(f"{route}/confirm-payment", {}, addHeader)
		self.load(**response)
		return self
