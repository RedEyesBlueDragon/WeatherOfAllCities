
import urllib
import json


with open ('cities.json') as json_file:
	data = json.load(json_file)
	de= u"\N{DEGREE SIGN}"
	for i in range(1,1000):
		
		
		try:

			name = str(data[i]["name"])
			
			#request = urllib.urlopen('http://api.aerisapi.com/observations/seattle,wa?client_id=mkI4RPF4CmLoXCLcx1POy&client_secret=03nEfOzhSxbQSrkDKaJiozbVXQZ4ibu0AEJSV35L')
			request = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q= ' + name +'&appid=bea6ec41cd1e78632481d9de7332259b')
			response = request.read()
					
			json2 = json.loads(response)
			#print(json2['cod'])
			if int(json2['cod']) == 200:  #Number of cities to be printed
				
				number = len(name)
				
				name = name.ljust(40, ' ');

				print(" %s " % name),
				number = 20 - number
				
				
				print(" : %s  %d %sC " % ( json2['weather'][0]['main'], json2['main']['temp'] - 273, de))
		except:
			continue
	request.close()
