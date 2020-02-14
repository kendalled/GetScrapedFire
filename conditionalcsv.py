import csv

def is_texas(row):
  return row[13] == 'TX'

with open('waybetterfiredept.csv', 'r') as fin, open('onlyTXFire.csv', 'w', newline='') as fout:

    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_ALL)

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for row in reader:
      # print(row[13])
      if(is_texas(row)):
        writer.writerow(row)
      else:
        print('skipped one!')

