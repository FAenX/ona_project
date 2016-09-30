import requests
import json
import sys

response=requests.get('https://api.ona.io/api/v1/data/151926', auth=('shailok', 'WdNT-A_8=27%5ei#`S*LCrDn!3)-v{P`Y*7E(~ruTy")>-=Zs"E:}2-\'UYJa*w!c'))
if response.status_code==200:
	print 'successful'
	data=json.loads(response.text)
r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r:
            f.write(chunk)
