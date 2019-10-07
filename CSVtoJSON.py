import csv
import json
import glob
import os

def read_CSV():
    for filename in glob.glob('./csv/*.csv'):

        csvfile = os.path.splitext(filename)[0]
        jsonfile = csvfile + '.json'

        with open(csvfile+'.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(jsonfile, 'w') as f:
            json.dump(rows, f)


read_CSV()
