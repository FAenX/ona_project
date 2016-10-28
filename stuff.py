def generate(_list):
	for i in xrange(0,len(_list)):
		yield _list[i]
		

#unfinished......get images from ona.io form data
def get_image():
	r = requests.get(url, stream=True)
	if r.status_code == 200:
    		with open(path, 'wb') as f:
        		for chunk in r:
            			f.write(chunk)



#google reverse geocoding requests and response
def get_location_data(lat,_long,API_KEY):
	response=requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%d,%d&key=%s'%(lat, _long, API_KEY))
	
	
#or using googlemaps
def get_location(lat,_long,API_KEY):
	gmaps=googlemaps.Client(key=API_KEY)
	reverse_geocode_results=gmaps.reverse_geocode((lat,_long))
	




