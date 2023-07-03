# -*- coding: utf-8 -*-
from .lib import *

class Period(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=25)
		cls.start_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.end_at = DateTime(format="%Y-%m-%dT%H:%M:%S")


		super().__init__(**kw)
