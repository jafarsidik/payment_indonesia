import frappe, json, base64, datetime, hashlib, hmac, json, urllib.request, urllib.error
from frappe import _ 
from frappe.integrations.utils import make_get_request, make_post_request, create_request_log
from frappe.utils import cint, flt, today, response
from frappe.model.document import Document

        
        # self.api_key = api_key
        # self.api_secret = api_secret
        # self.access_token = ''

        # self.host = host
        # self.oauth_path = '/api/oauth/token'
        # self.get_balance_path = '/banking/v2/corporates/{corporate_id}/accounts/{account_number}'
        # self.get_statement_path = '/banking/v2/corporates/{corporate_id}/accounts/' \
        #     '{account_number}/statements?EndDate={end_date}&StartDate={start_date}'
        # self.transfer_path = '/banking/corporates/transfers'
    
def _generate_signature(self, relative_url, timestamp, http_method='GET', request_body=b''):
    ''' Generate signature to be sent.
    '''
    signature = hmac.new(self.apisecret.encode(), digestmod=hashlib.sha256)
    string_to_sign = http_method + ':' + relative_url + ':' + self.access_token + \
        ':' + hashlib.sha256(request_body.replace(b' ', b'')).hexdigest() + ':' + timestamp
    signature.update(string_to_sign.encode())
    return signature.hexdigest()

@frappe.whitelist(allow_guest=True)
def make_post(**kwargs):
    args = frappe._dict(kwargs)
    doc = frappe.get_doc('Setting')
    
    #if (doc.mode_bpjs == "Production"):
    #    host = doc.prod_host
    #    outh_order_id = doc.prod_outh_order_id
    #    outh_secret_id = doc.prod_outh_secret_key
    #    apikey = doc.prod_apikey
    #    apisecret = doc.prod_apikey_secret_key
    #else:
    #    host = doc.sandbox_host
    #    outh_order_id = doc.sandbox_outh_order_id
    #    outh_secret_id = doc.sandbox_outh_secret_key
    #    apikey = doc.sandbox_apikey
    #    apisecret = doc.sandbox_apikey_secret_key
    headers ={
        'Host': 'sandbox.bca.co.id',
        'Authorization': 'Bearer a0daAPsGwPDHGMv6MpWzoIPgZvN9YvrSi7xdVI7Jb98638ilM7ila7',
        'Content-Type': 'application/json',
        'Origin': 'yourdomain.com',
        'X-BCA-Key': '41138489-1057-4e7e-ab93-9bc97b511cf6', 
        'X-BCA-Timestamp': '2016-02-03T10:00:00.000+07:00',
        'X-BCA-Signature': 'ce20470484c27c0441d7c9dedc7d3e187e5e908df1780c6c389941b779033519'
    }
    data={
        'username': 'test'
    }
    make_post_request('https://example.com', headers=headers,data=data)

@frappe.whitelist(allow_guest=True)
def test(**kwargs):
    #timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
    #timestamp = timestamp[:23] + timestamp[26:]
    #signature = self._generate_signature(relative_url, timestamp)
    #bca._generate_signature()
    return Bca.auth()