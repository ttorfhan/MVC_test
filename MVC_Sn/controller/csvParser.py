import csv

csv_path ="model/database.csv"

def parseCsv():
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        data = []
        next(reader) #ข้าม header
        for row in reader:
            data.append(row)
        return data