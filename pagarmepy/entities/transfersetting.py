# -*- coding: utf-8 -*-
from .lib import *

class TransferSetting(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.transfer_enabled = Boolean()
		cls.transfer_interval = String(max=30)
		cls.transfer_day = Int()

		super().__init__(**kw)
