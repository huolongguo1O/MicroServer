import os
from flask import Flask
import sqlite3
import requests
# import client_config
app = Flask(__name__)
conn = sqlite3.connect('dataclient.db')
cur = conn.cursor()
@app.route('/awawawa/add/<str:username>/<int:userid>/<str:name>/<int:port>/<path:url>')
def add(username,userid, name, port,url):
	cur.execute('INSERT INTO Dockers VALUES(?,?,?,?,?,?,?,?)',(username,userid,port,name,0,0,0,url))
	conn.commit()

	os.system('docker run -d -p '+port+':80 -m 64MB --cpu-period=50000 --cpu-quota=5000 --name '+name+' MicroServer/python:v1')
	return 'Hello, World!'
@app.route('/awa/pause/<str:name>')
def pause(name):
	os.system('docker pause '+name)
	return 'Done!'
@app.route('/awawawa/unpause/<int:port>')
def unpause(port):
	name=cur.execute('SELECT name FROM Dockers WHERE port =?',(port,)).fetchone()

	os.system('docker unpause '+name)
	return 'Done!'

@app.route('/<int:port>/<path:pat>')
# 讲收到的内容转发到127.0.0.1:port
def turner(port,pat):
	requests.get('127.0.0.1/awawawa/unpause/'+port)
	ret=requests.get('127.0.0.1:'+port+'/'+pat)
	return ret.text


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)



if __name__ == '__main__':
	app.run(host='0.0.0.0')

