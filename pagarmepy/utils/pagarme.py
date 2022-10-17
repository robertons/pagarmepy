
from pagarmepy.utils import constants
import base64
from requests_toolbelt import MultipartEncoder
import requests
import logging
import json
import os
import io
from datetime import datetime

DEBUG = False
SANDBOX = False
ACCOUNTID = ''
PUBLICKEY = ''
PRIVATEKEY = ''

def DebugRequest():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def PagarMe(idAccount, publicKey, privateKey, sandbox=False, debug=False):
    if debug:
        DebugRequest()
    global DEBUG
    global SANDBOX
    global ACCOUNTID
    global PUBLICKEY
    global PRIVATEKEY
    DEBUG = debug
    SANDBOX = sandbox
    ACCOUNTID = idAccount
    PUBLICKEY = publicKey
    PRIVATEKEY = privateKey
    if sandbox and not 'test' in PUBLICKEY:
        raise Exception('Isn`t valid Public Key for Sandbox')

    if sandbox and not 'test' in PRIVATEKEY:
        raise Exception('Isn`t valid Private Key for Sandbox')

def __headers(data=None, addHeader=None):
    hash = base64.b64encode(f'{PRIVATEKEY}:'.encode("utf-8")).decode("utf-8")
    __headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8' if addHeader is None or not 'Content-Type' in addHeader else addHeader['Content-Type'],
        'Authorization': f'Basic {hash}'
    }
    if addHeader:
        del addHeader['Content-Type']
        __headers = {**__headers, **addHeader}

    return __headers


def __Route(url):
    return f'{constants.ROUTE_PRODUCAO}{url}'


def Get(url, data={}, addHeader=None):
    return __ValidateResponse(requests.get(__Route(url), params=data, headers=__headers(data, addHeader)))


def Post(url, data, addHeader=None):
    return __ValidateResponse(requests.post(__Route(url), json=data, headers=__headers(data, addHeader)))


def Put(url, data, addHeader=None):
    return __ValidateResponse(requests.put(__Route(url), json=data, headers=__headers(data, addHeader)))


def Patch(url, data, addHeader=None):
    post_data = dict(data)
    if 'resourceToken' in post_data:
        del post_data['resourceToken']
    return __ValidateResponse(requests.patch(__Route(url), json=post_data, headers=__headers(data, addHeader)))


def Delete(url, addHeader=None):
    return __ValidateResponse(requests.delete(__Route(url), headers=__headers(None, addHeader)))


def UploadMultiPart(url, files, data=None, addHeader=None):
    f = []
    for file in files:
        if isinstance(file, str):
            f.append(('files', (file, open(file, 'rb'))))
        elif isinstance(file, tuple) and isinstance(file[0], str) and (isinstance(file[1], bytes) or isinstance(file[1], io.BufferedReader)):
            f.append(('files', (file[0], file[1])))
    m = MultipartEncoder(fields=f)
    return __ValidateResponse(requests.post(__Route(url), data=m, headers=__headers(data, {'Content-Type': m.content_type})))


class PagarMeException(Exception):
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail

def __ValidateResponse(response):

    if response.status_code == 200:
        try:
            if DEBUG:
                print(f"Response:\n\n {json.dumps(response.json(), indent=4)} \n\n")
            return response.json()
        except:
            if DEBUG:
                print(f"Response:\n\n {response.text} \n\n")
            return response.text
    elif response.status_code > 200:
        status_code = response.status_code
        try:
            response_json = response.json()
            response_json['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response_json['status'] = status_code
        except Exception as e:
            response_json = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": status_code,
                "message": "Unexpected Error",
                "errors": [
                    {
                        "message": str(e),
                        "errorCode": "0"
                    }
                ]
            }
        raise PagarMeException("Pagar.me Request Error", response_json)
