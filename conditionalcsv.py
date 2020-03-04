import csv

def is_state(row, state):
  return row[13] == state

def is_not_volunteer(row):
  print(row[18])
  return(row[18] != 'Volunteer')

with open('waybetterfiredept.csv', 'r') as fin, open('onlyFLFire.csv', 'w', newline='') as fout:
    state = 'FL'
    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_ALL)

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for row in reader:
      # print(row[13])
      if(is_state(row, state) and is_not_volunteer(row)):
        writer.writerow(row)
      else:
        print('skipped one!')

