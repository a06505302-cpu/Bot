import requests

api = "http://gatescheck.duckdns.org:7000/check"

params = {
    "url": "https://dandelionsmontessori.org/give/15767517?giveDonationFormInIframe=1",
    "card": f"",
    "amount": 0.10
}

r = requests.get(api, params=params)

print(r.json()['result'])
