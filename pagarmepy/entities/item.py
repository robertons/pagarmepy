# -*- coding: utf-8 -*-
from .lib import *

class Item(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)
		cls.name = String(max=56)
		cls.amount = Int()
		cls.description = String(max=256)
		cls.quantity = Int()
		cls.cycles = Int()
		cls.interval = String(max=25)
		cls.code = String(max=25)
		cls.category = String(max=25)
		cls.status = String(max=25)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.order = Obj(context=cls, key='order', name='Order')
		cls.pricing_scheme = Obj(context=cls, key='pricing_scheme', name='PricingScheme')
		cls.plan_item_id =  String(max=25)
		cls.plan = Obj(context=cls, key='plan', name='Plan')
		cls.subscription = Obj(context=cls, key='subscription', name='Subscription')
		cls.discounts = ObjList(context=cls, key='discounts', name='Discount')
		cls.increments = ObjList(context=cls, key='increments', name='Increment')

		super().__init__(**kw)
