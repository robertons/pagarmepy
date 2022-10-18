# -*- coding: utf-8 -*-
from .lib import *

class Authentication(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.threed_secure = Obj(context=cls, key='threed_secure', name='ThreedSecure')

		super().__init__(**kw)
