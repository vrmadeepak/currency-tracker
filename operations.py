import requests

def get_remaining_requests(apikey):
    url = "https://api.currencyapi.com/v3/status?apikey="+apikey
    r = requests.get(url)
    data = r.json()
    return data["quotas"]["month"]["remaining"]

def get_prices(apikey, currencies):
    url = "https://api.currencyapi.com/v3/latest?apikey="+apikey+"&currencies="+"%2C".join(currencies)
    r = requests.get(url)
    data = r.json()
    return data