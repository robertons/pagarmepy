# -*- coding: utf-8 -*-
from .lib import *

class Voucher(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.statement_descriptor = String(max=22)
		cls.card = Obj(context=cls, key='card', name='Card')
		cls.card_id = String(max=40)
		cls.card_token = String(max=40)
		cls.metadata = Dict()


		super().__init__(**kw)
