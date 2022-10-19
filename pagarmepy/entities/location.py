# -*- coding: utf-8 -*-
from .lib import *

class Location(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.latitude = String(max=256)
		cls.longitude = String(max=256)
		
		super().__init__(**kw)
