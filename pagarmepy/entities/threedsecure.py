# -*- coding: utf-8 -*-
from .lib import *

class ThreedSecure(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.mpi = String(max=11)
		cls.eci = String(max=2)
		cls.cavv = String(max=256)
		cls.transaction_id = String(max=256)
		cls.ds_transaction_id = String(max=256)
		cls.version = String(max=6)
		cls.redirect_url = String(max=512)

		super().__init__(**kw)
