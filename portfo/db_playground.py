import csv
def write_to_csv(dict):
	with open('database.csv',mode='a',newline='') as database:
		csv_writer = csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow(dict)
	pass