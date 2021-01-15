import os, csv

colors = []

with open('farben.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count is not 0:
            colors.append(row[1])
            line_count += 1
        else:
            line_count += 1

with open('colors.scss', "w") as scss:
    scss.write(".color{")
    for color in colors:
        scss.write("&.color--"+color+"{background-color:#"+color+";}")
    scss.write("}")