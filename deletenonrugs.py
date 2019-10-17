# Delete all products that are not rugs
lines = list()

delete = 'Rugs'

with open('masterlist.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if field != delete:

                lines.remove(row)

with open('mycsv.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)