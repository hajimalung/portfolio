import csv
def write_to_csv(dict):
	with open('database.csv',mode='a',newline='') as database:
		csv_writer = csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow(dict)


def read_from_csv():
	with open('database.csv',mode='r',newline='') as database:
		csv_reader = csv.reader(database,delimiter=',',quotechar='"')
		return [row for row in csv_reader]