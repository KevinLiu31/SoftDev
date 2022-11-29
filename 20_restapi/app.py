from flask import Flask, render_template
import requests
import urllib
import json
app = Flask(__name__)
@app.route('/', methods=["GET"])
def main():
	file = open("key_nasa.txt", "r")
	key = file.read().strip()
	print(key)
	#dict1= requests.get("https://api.nasa.gov/planetary/apod?api_key="+key).json()
	dic = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key="+key)
	dict1 = json.loads(dic.read())
	return render_template("main.html", pic = dict1["url"], title = dict1["title"], exp = dict1["explanation"])
if __name__ == '__main__':
	app.debug = True
	app.run()