# -*- coding: utf-8 -*-
from .lib import *

class BankTransfer(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.bank = String(max=5)
		cls.metadata = Dict()


		super().__init__(**kw)
