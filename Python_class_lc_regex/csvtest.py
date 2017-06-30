import csv
import os
import json

os.makedirs('Remove', exist_ok=True)

#Reading from a CSV file
exampleFile = open('csv.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)


#Writing into a CSV file
outputFile = open('output.csv', 'a', newline='')
outputFile1 = open('output.txt', 'a', newline='')
outputWriter = csv.writer(outputFile)
outputWriter1 = csv.writer(outputFile1, delimiter='\t', lineterminator='\n\n')
#outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])


for row in exampleData:
    outputWriter.writerow(row)
    outputWriter1.writerow(row)

#close after writing all
outputFile.close()
outputFile1.close()


for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
            continue    # skip non-csv files

       print('Removing header from ' + csvFilename + '...')

       # TODO: Read the CSV file in (skipping first row).
        # Read the CSV file in (skipping first row).
       csvRows = []
       csvFileObj = open(csvFilename)
       readerObj = csv.reader(csvFileObj)
       for row in readerObj:
           if readerObj.line_num == 1:
                continue    # skip first row
           csvRows.append(row)
       csvFileObj.close()
       # TODO: Write out the CSV file.
       csvFileObj = open(os.path.join('Remove', csvFilename), 'w',
                    newline='')
       csvWriter = csv.writer(csvFileObj)
       for row in csvRows:
           csvWriter.writerow(row)
       csvFileObj.close()

import json
print("json")
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print("python data")
print(jsonDataAsPythonValue)

#dump into json
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
print("json data")
stringOfJsonData2 = json.dumps(pythonValue)
print(stringOfJsonData2)


#get data from web site
#need pip install for it
import json, requests, sys
# Compute location from command line arguments.
##if len(sys.argv) < 2:
##    print('Usage: quickWeather.py location')
##    sys.exit()
##location = ' '.join(sys.argv[1:])

#hardcode location


# Download the JSON data from OpenWeatherMap.org's API.
#http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1
url ='http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
response = requests.get(url)
response.raise_for_status()

#response holds a large json text
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:'.format('my city'))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
