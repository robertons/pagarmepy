# -*- coding: utf-8 -*-
from .lib import *

class Antifraud(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.provider_name = String(max=256)
		cls.return_code = String(max=100)
		cls.status = String(max=100)
		cls.return_message = String(max=256)
		cls.score = Int()

		super().__init__(**kw)
