# -*- coding: utf-8 -*-
from .lib import *

class Boleto(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.bank = Int()
		cls.instructions = String(max=256)
		cls.due_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.nosso_numero = String(max=30)
		cls.type = String(max=20)
		cls.metadata = Dict()
		cls.document_number = String(max=16)
		cls.statement_descriptor = String(max=13)
		cls.interest = Obj(context=cls, key='interest', name='Interest')
		cls.fine = Obj(context=cls, key='fine', name='Fine')

		super().__init__(**kw)
