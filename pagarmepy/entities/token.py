# -*- coding: utf-8 -*-
from .lib import *
from pagarmepy.utils.pagarme import *

class Token(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.type = String(max=26)
		cls.card = Obj(context=cls, key='card', name='Card')
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.update_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.deleted_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.expires_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.status = String(max=26)
		cls.metadata = Dict()

		super().__init__(**kw)

	def Create(self, **kw):
		if not 'appId' in kw:
			raise Exception(f"Param (appId) is required on method Create")
		data = Post(f"/tokens?appId={kw['appId']}", self.toJSON(), None)
		self.load(**data)
		return self
