# -*- coding: utf-8 -*-
from .lib import *

class Option(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.liable = Boolean()
		cls.charge_processing_fee = Boolean()
		cls.charge_remainder_fee = Boolean()

		super().__init__(**kw)
