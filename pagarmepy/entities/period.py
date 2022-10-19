# -*- coding: utf-8 -*-
from .lib import *

class Period(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)


		super().__init__(**kw)
