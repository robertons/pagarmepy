# -*- coding: utf-8 -*-
from .lib import *

class SubMerchant(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.Merchant_Category_Code = String(max=256)
		cls.Payment_Facilitator_Code = String(max=256)
		cls.Code = String(max=256)
		cls.name = String(max=256)
		cls.Document = String(max=256)
		cls.Type = String(max=256)
		cls.phones = String(max=256)
		cls.Coutry_code = String(max=256)
		cls.Area_code = String(max=256)
		cls.Number = String(max=256)
		cls.Address = String(max=256)
		cls.Country = String(max=256)
		cls.State = String(max=256)
		cls.City = String(max=256)
		cls.Neighborhood = String(max=256)
		cls.Street = String(max=256)
		cls.Number = String(max=256)
		cls.Complement = String(max=256)
		cls.Zip_Code = String(max=256)

		super().__init__(**kw)
