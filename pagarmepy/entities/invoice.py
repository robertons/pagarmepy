# -*- coding: utf-8 -*-
from .lib import *

class Invoice(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

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
