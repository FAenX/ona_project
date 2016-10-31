import requests,json
from stuff.stuff import generate

#get ona.io project id
def get_project_id(endpoint,username,password,title):
	response=requests.get(endpoint, auth=(username, password))
	try:
		if response.status_code==200:
			print 'successful'
			data=json.loads(response.text)
			#print data
			dat=generate(data)
			project = dat.next()
			if not project.get('title')==title:
				project=dat.next()
				if project.get('title')==title:
					#print 'project id ',project.get('id')
					project_id= project.get('id')
					return project_id
		else:
			pass
	except:
		pass

	
	
		

#get form data by id
def get_form_data(endpoint,username,password,form_id):
	response=requests.get(endpoint +'/'+str(form_id), auth=(username, password))
	try:
		if response.status_code==200:
			print 'successful'
			project_data=json.loads(response.text)
			#print data
			#dat=generate(data)
			return project_data
		else:
			pass
	except:
		pass	
	









