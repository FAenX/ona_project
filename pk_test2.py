import onadata as od


title='pk_test2'
endpoint='https://api.ona.io/api/v1/data'
username='shailok'
password='WdNT-A_8=27%5ei#`S*LCrDn!3)-v{P`Y*7E(~ruTy")>-=Zs"E:}2-\'UYJa*w!c'
	
fields=['rent', 'contact_name', 'contact_number', 'locality', 'toilet_photo', 'location', 'keja_type', 'bedroom_photo', '_submitted_by', 	'kitchen_photo', 'town', u'_attachments', 'rentals_name', '_submission_time', '_geolocation', u'_id']

prid=od.get_project_id(endpoint,username,password,title)
#print prid
dat=od.get_form_data(endpoint,username,password,prid)
#print dat
gen=generate(dat)


def generate(_list):
	for i in xrange(0,len(_list)):
		yield _list[i]

def kejdata():

	
	while True:
		try:
			dic=gen.next()
			for g in dic.keys():
				if g not in fields:
					dic.pop(g)
		except StopIteration:
			break
	return dat			
kejdata()	
