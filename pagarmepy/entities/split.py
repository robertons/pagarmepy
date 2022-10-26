# -*- coding: utf-8 -*-
from .lib import *

class Split(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)
		cls.amount = Int()
		cls.type = String(max=25)
		cls.recipient_id = String(max=30)
		cls.recipient = Obj(context=cls, key='recipient', name='Recipient')
		cls.options = Obj(context=cls, key='options', name='Option')


		super().__init__(**kw)
