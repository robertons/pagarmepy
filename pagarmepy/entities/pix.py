# -*- coding: utf-8 -*-
from .lib import *

class Pix(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.expires_in = Int()
		cls.expires_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.additional_information = ObjList(context=cls, key='additional_information', name='dict')

		super().__init__(**kw)
