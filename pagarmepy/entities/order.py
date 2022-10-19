# -*- coding: utf-8 -*-
from .lib import *

class Order(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/orders'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=22)
		cls.currency = String(max=5)
		cls.status = String(max=20)
		cls.code = String(max=20)
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.customer_id = String(max=22)
		cls.shipping = Obj(context=cls, key='shipping', name='Shipping')
		cls.antifraud = Obj(context=cls, key='antifraud', name='Antifraud')
		cls.payments = ObjList(context=cls, key='payments', name='Charge')
		cls.items = ObjList(context=cls, key='items', name='Item')
		cls.closed = Boolean()
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.device =  Obj(context=cls, key='device', name='Device')
		cls.location =  Obj(context=cls, key='location', name='Location')
		cls.ip =  String(max=20)
		cls.session_id =  String(max=120)
		cls.antifraud_enabled = Boolean()
		cls.SubMerchant = Obj(context=cls, key='SubMerchant', name='SubMerchant')
		cls.Recurrence = Boolean()
		cls.metadata = Dict()

		super().__init__(**kw)
