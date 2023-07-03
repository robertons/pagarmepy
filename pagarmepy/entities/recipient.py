# -*- coding: utf-8 -*-
from .lib import *
from pagarmepy.entities.balance import Balance
from pagarmepy.entities.bankaccount import BankAccount
from pagarmepy.entities.withdraw import Withdraw
from pagarmepy.entities.transfersetting import TransferSetting

class Recipient(PagarMeEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/recipients'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.name = String(max=100)
		cls.email = String(max=100)
		cls.document =String(max=17)
		cls.description = String(max=156)
		cls.type = String(max=30)
		cls.status = String(max=30)
		cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.default_bank_account = Obj(context=cls, key='default_bank_account', name='BankAccount')
		cls.transfer_settings = Obj(context=cls, key='transfer_settings', name='TransferSetting')
		cls.gateway_recipients = ObjList(context=cls, key='gateway_recipients', name='GatewayRecipient')
		cls.metadata = Dict()

		super().__init__(**kw)

	def ChangeDefaultBankAccount(self, bank:BankAccount):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/default-bank-account", {'bank_account': bank.toJSON()}, addHeader)
		self.load(**response)
		return self

	def GetBalance(self):
		addHeader, route = self.FormatRoute(True, **{})
		response = Get(f"{route}/balance", None, addHeader)
		return Balance(**response)

	def DoWithdraw(self, amount:int):
		addHeader, route = self.FormatRoute(True, **{})
		response = Post(f"{route}/withdrawals", {'amount': amount}, addHeader)
		return Withdraw(**response)

	def GetWithdraw(self, withdraw_id:str):
		addHeader, route = self.FormatRoute(True, **{})
		response = Get(f"{route}/withdrawals/{withdraw_id}", None, addHeader)
		return Withdraw(**response)

	def ListWithdrawals(self, filters=None, **kw):
		addHeader, route = self.FormatRoute(True, **kw)
		qs =''
		if filters:
			qs = '?' + '&'.join([f'{k}={v}' for k,v in filters.items()])
		route = f"{route}/withdrawals{qs}"
		response = Get(route, addHeader)
		return ListType(Withdraw).add([Withdraw(**item) for item in response['data']]) if 'data' in response else ListType(Withdraw)

	def ChangeTransferSettings(self, transfer_enabled:bool, transfer_interval:str, transfer_day:str):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/transfer-settings",  {'transfer_enabled': transfer_enabled, 'transfer_interval': transfer_interval, 'transfer_day': transfer_day}, addHeader)
		self.load(**response)
		return self

	def ChangeAnticipationSettings(self, enabled:bool, type:str, volume_percentage:str, days:list, delay:str):
		addHeader, route = self.FormatRoute(True, **{})
		response = Patch(f"{route}/automatic-anticipation-settings",  {'enabled': enabled, 'type': type, 'volume_percentage': volume_percentage, 'days': days, 'delay': delay }, addHeader)
		self.load(**response)
		return self
