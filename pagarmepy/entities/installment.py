# -*- coding: utf-8 -*-
from .lib import *

class Installment(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.number = Int()
		cls.total = Int()

		super().__init__(**kw)
