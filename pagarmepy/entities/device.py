# -*- coding: utf-8 -*-
from .lib import *

class Device(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.platform = String(max=256)

		
		super().__init__(**kw)
