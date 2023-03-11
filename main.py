import requests
from settings import api_key
from currencies import currencies
from operations import *

url = "https://api.currencyapi.com/v3/"

# endpoints = {
#     "health": "status",
#     "currencies": "currencies",
# }

endpoints = ["status", "currencies", "latest", "historical"]

# https://api.currencyapi.com/v3/status?apikey=
# https://api.currencyapi.com/v3/currencies?apikey=&currencies=EUR%2CUSD%2CCAD
# https://api.currencyapi.com/v3/latest?apikey=&currencies=EUR%2CUSD%2CCAD
# https://api.currencyapi.com/v3/historical?apikey=&currencies=EUR%2CUSD%2CCAD&date=2023-03-10

health = "status?apikey=" + api_key 

['apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

print(get_remaining_requests(api_key))
print(get_prices(api_key, currencies))
# print(r, r.request, r.text, sep='\n')