# -*- coding: utf-8 -*-
from .lib import *

class BankAccount(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=30)
		cls.recipient = Obj(context=cls, key='recipient', name='Recipient')
		cls.holder_name = String(max=30)
		cls.holder_type = String(max=30)
		cls.holder_document = String(max=16)
		cls.bank = String(max=30)
		cls.branch_number = String(max=30)
		cls.branch_check_digit = String(max=30)
		cls.account_number = String(max=30)
		cls.account_check_digit =  String(max=30)
		cls.type = String(max=30)
		cls.status = String(max=30)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.metadata = Dict()

		super().__init__(**kw)
