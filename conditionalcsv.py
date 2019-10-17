with open('onlyrugs.csv', 'r') as fin, open('onlypricedrugs.csv', 'w', newline='') as fout:

    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_ALL)

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for i in reader:
      if(contains_sku(i[2])):
        writer.writerow(i)
      else:
        print('skipped: ' + i[2])