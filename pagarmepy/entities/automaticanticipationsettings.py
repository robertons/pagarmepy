# -*- coding: utf-8 -*-
from .lib import *

class AutomaticAnticipationSettings(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.enabled = Boolean()
		cls.type = String(max=30)
		cls.volume_percentage = Int()
		cls.days = Int()
		cls.delay = Int()

		super().__init__(**kw)
