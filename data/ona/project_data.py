import onadata as od
from stuff.stuff import sort_data,download


title='pk_test2'
endpoint='https://api.ona.io/api/v1/data'
username='shailok'
password='WdNT-A_8=27%5ei#`S*LCrDn!3)-v{P`Y*7E(~ruTy")>-=Zs"E:}2-\'UYJa*w!c'






project_id=od.get_project_id(endpoint,username,password,title)
data=od.get_form_data(endpoint,username,password,project_id)

def keja_data():
	keys=['rent', 'contact_name', 'contact_number', 'locality', 'toilet_photo', 'location', 'keja_type', 'bedroom_photo', '_submitted_by', 	'kitchen_photo', 'town','rentals_name', '_submission_time', '_geolocation', '_id']
	keja_data=sort_data(data,keys)
	return keja_data

def keja_image_links():
	keys=['download_url','id']
	links=sort_data(data,keys,key='_attachments')
	return links






	




	
			
	
