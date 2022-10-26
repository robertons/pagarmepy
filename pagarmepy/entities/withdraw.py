
# -*- coding: utf-8 -*-
from .lib import *

class Withdraw(PagarMeEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=30)
        cls.amount = Int()
        cls.status = String(max=30)
        cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.bank_account = Obj(context=cls, key='bank_account', name='BankAccount')
        cls.metadata = Dict()

        super().__init__(**kw)
