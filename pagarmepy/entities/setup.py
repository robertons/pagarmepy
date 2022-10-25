# -*- coding: utf-8 -*-
from .lib import *

class Setup(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.amount = Int()
		cls.description = String(max=256)
		cls.payment = Obj(context=cls, key='payment', name='Payment')


		super().__init__(**kw)
