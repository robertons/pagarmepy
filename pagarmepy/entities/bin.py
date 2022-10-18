# -*- coding: utf-8 -*-
from .lib import *
from pagarmepy.utils.pagarme import *

class BIN(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.brand = String(max=26)
		cls.gaps = ObjList(context=cls, key='gaps', name='int')
		cls.lenghts = ObjList(context=cls, key='lenghts', name='int')
		cls.mask =  String(max=26)
		cls.cvv = Int()
		cls.brandImage = String(max=155)
		cls.possibleBrands =ObjList(context=cls, key='possibleBrands', name='str')

		super().__init__(**kw)

	def Get(self, **kw):
		if not 'bin' in kw:
			raise Exception(f"Param (bin) is required on method Get")
		response = ValidateResponse(requests.get(f"https://api.pagar.me/bin/v1/{kw['bin']}"))
		self.load(**response)
		return self
