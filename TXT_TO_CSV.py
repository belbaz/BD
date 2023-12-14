import csv

def convert_txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = list(reader)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


convert_txt_to_csv('VOLS.txt', 'VOLS.csv')
