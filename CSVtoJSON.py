import csv
import json
import glob
import os

def convert_to_json():
    for filename in glob.glob('./csv/*.csv'):

        csvfile = os.path.splitext(filename)[0]
        jsonfile = csvfile + '.json'

        with open(csvfile+'.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(jsonfile, 'w') as f:
            json.dump(rows, f)


convert_to_json()
