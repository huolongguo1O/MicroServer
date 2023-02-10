import time
import requests
import clientconfig
cnt = 0
def pause():
	time.sleep(1)
	if cnt == 0:
		requests.get('http://'+clientconfig.host+':8000/pause/'+clientconfig.name) 