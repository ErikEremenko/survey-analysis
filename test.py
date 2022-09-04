import csv

filename = "(8) Politische Bildung.csv"

fields = []
rows = []


with open (filename, "r") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows.append(row)

    print("Gesamte Anzahl an Reihen: %d"%(reader.line_num))
    
print("Die Spaltennamen sind:" + ", ".join(field for field in fields))