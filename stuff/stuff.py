#pieces of code
import requests


# Colours
W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m";

#generate list items
def generate(li):
	for i in xrange(0,len(li)):
		yield li[i]
		

#unfinished......get images url
def download(url, path,**kwargs):
	if kwargs:
		r = requests.get(url, stream=True, auth=(kwargs['username'],kwargs['password']))
	else:
		r = requests.get(url, stream=True )
	if r.status_code == 200:
		with open(path, 'wb') as f:
			for chunk in r:
    				f.write(chunk)
	
		

#sort remove irrelevant dictionary key:values 
def sort_data(data,keys,**kwargs):
	if kwargs:
		dat=[]
		key=kwargs['key']	
		for d in data:
			dat.extend(d[key])
		

	else:
	
		dat=data	
	gen=generate(dat)		
	while True:
		try:	
			dic=gen.next()
			all_keys=dic.keys()
		
		except StopIteration:
			break			
		
		for key in all_keys:
			if key not in keys:
				dic.pop(key)	
	return dat	



	
















#google reverse geocoding requests and response
def get_location_data(lat,_long,API_KEY):
	response=requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%d,%d&key=%s'%(lat, _long, API_KEY))
	
	
#or using googlemaps
def get_location(lat,_long,API_KEY):
	gmaps=googlemaps.Client(key=API_KEY)
	reverse_geocode_results=gmaps.reverse_geocode((lat,_long))
	




