# -*- coding: utf-8 -*-
from .lib import *

class GatewayRecipient(PagarMeEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.gateway = String(max=30)
        cls.status = String(max=30)
        cls.pgid = String(max=100)
        cls.createdAt = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.updatedAt = DateTime(format="%Y-%m-%dT%H:%M:%S")

        super().__init__(**kw)
