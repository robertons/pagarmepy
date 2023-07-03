# -*- coding: utf-8 -*-
from .lib import *

class Splitsubscription(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.enabled = Boolean()
		cls.rules = ObjList(context=cls, key='split', name='Split')

		super().__init__(**kw)
