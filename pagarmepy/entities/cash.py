# -*- coding: utf-8 -*-
from .lib import *

class Voucher(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.description = String(max=256)
		cls.confirm = Boolean()
		cls.metadata = Dict()


		super().__init__(**kw)
