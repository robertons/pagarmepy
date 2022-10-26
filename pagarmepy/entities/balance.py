
# -*- coding: utf-8 -*-
from .lib import *

class Balance(PagarMeEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.currency = String(max=30)
        cls.available_amount = Int()
        cls.waiting_funds_amount = Int()
        cls.transferred_amount = Int()
        cls.recipient = Obj(context=cls, key='recipient', name='Recipient')

        super().__init__(**kw)
