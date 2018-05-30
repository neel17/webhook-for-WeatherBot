import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


# A decorator that tells Flask what URL should trigger our function
# By default, the flask route responds to the GET requests.
# This prefrence can be altered by providing methods argument to route() decorator.

@app.route('/webhook', methods=['POST'])
def webhook():
	# Parse the incoming JSON request data and returns it.
	# By default this function will return None if the mumetype is not application/json but this can be overridden by the force parameter.
	# force - if set to True the mimetype is ignored
	# silent - if set to True this methid will fall silently and return None
	
	req = request.get_json(silent=True, force=True)
	print(Json.dumps(req, indent=4)
	
	# Extract paprameter value --> query the Open Weather API --> construct response --> send to Dialogflow
	res = makeResponse(req)
	res = json.dumps(res, indent = 4)
	# Setup the response from webhook in right format
	r = make_response(res) 
	r.headers['Content-type'] = 'application/json'
	return r
	
# Helper function makeResponse

def makeResponse(req):
	result = req.get('queryResult')
	parameters = result.get('parameters')
	city = parameters.get('geo-city')
	date = parameters.get('date')
	r = requests.get('https://samples.openweathermap.org/data/2.5/forecast?q='+city+'&appid=b6907d289e10d714a6e88b30761fae22'
	json_object = r.json()
	weather = json_object['list']
	for i in range(0,len(weather)):
		if date in weather[i]['dt_txt']:
			 condition = weather[i]['weather'][0]['description']
			 break
			
	# The response from the service should have the following fields:
	# Name : speech ; displayText ; source
	# Type : string ; string ; string
	# Description : Response to the request
	# Text displayed on the user device screen ;  Data Source
	
	speech = "The forecast for "+city+" for "+date+" is "+condition
	return{
	"speech":speech"displayText":speech,
	"source":"apiai-weather-webhook"
	}
	
if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=Flase, port=port, host='0.0.0.0')
	
	
