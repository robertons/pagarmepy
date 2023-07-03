# -*- coding: utf-8 -*-
from .lib import *

class Transaction(PagarMeEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=25)
        cls.transaction_type = String(max=25)
        cls.gateway_id = String(max=100)
        cls.amount = Int()
        cls.payment_method = String(max=45)
        cls.status = String(max=25)
        cls.success = Boolean()
        cls.url = String(max=256)
        cls.pdf = String(max=256)
        cls.line =  String(max=256)
        cls.barcode =   String(max=256)
        cls.qr_code = String(max=256)
        cls.qr_code_url = String(max=256)
        cls.nosso_numero =  String(max=256)
        cls.bank = String(max=256)
        cls.document_number = String(max=256)
        cls.instructions = String(max=256)
        cls.due_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.installments = Int()
        cls.statement_descriptor = String(max=256)
        cls.acquirer_name = String(max=256)
        cls.acquirer_affiliation_code = String(max=100)
        cls.acquirer_tid = Int()
        cls.acquirer_nsu = Int()
        cls.acquirer_auth_code = Int()
        cls.acquirer_message = String(max=256)
        cls.acquirer_return_code = String(max=256)
        cls.operation_key = String(max=256)
        cls.operation_type = String(max=256)
        cls.card = Obj(context=cls, key='card', name='Card')
        cls.created_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.updated_at = DateTime(format="%Y-%m-%dT%H:%M:%S")
        cls.gateway_response = Dict()
        cls.antifraud_response = Obj(context=cls, key='antifraud_response', name='Antifraud')
        cls.metadata = Dict()

        super().__init__(**kw)
