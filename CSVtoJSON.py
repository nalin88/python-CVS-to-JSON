import csv, json

csvFile = 'file_csv.csv'
jsonFile = 'file_json.json'

# Read CSV File
def read_CSV(csvFile, jsonFile):

    print("Open CSV File")

    csv_rows = []
    with open(csvFile) as csv_file:
        reader = csv.DictReader(csv_file)
        field = reader.fieldnames

        for row in reader:
            csv_rows.extend([
                {
                    field[i]:row[field[i]]
                        for i in range(len(field))
                }
            ])

        convert_write_json(csv_rows, jsonFile)

# Convert csv data into json
def convert_write_json(data, jsonFile):

    print("Convert to JSON")

    with open(jsonFile, "w") as f:
		# Basic
        f.write(json.dumps(data))

        # Pretty
        # f.write(
        #     json.dumps(
        #         data,
        #         sort_keys = False,
        #         indent = 4,
        #         separators = (',', ': ')
        #     )
        # )

read_CSV(csvFile, jsonFile)
