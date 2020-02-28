import csv

ex_list = ['Chittenango Village Police Department', 'Cazenovia Village Police Department', 'Ramapo Town Police Department', 'Canastota Village Police Department', 'Baldwinsville Village Police Department', 'Tupper Lake Village Police Department', 'Saranac Lake Village Police Department','Rouses Point Village Police Department', 'Troy City Police Department', 'Malone Village Police Department', 'Lake Placid Village Police Department', 'Whitehall Village Police Department', 'Ticonderoga Police Department', 'Hudson Falls Village Police Department', 'Greenwich Village Police Department', 'Granville Village Police Department', 'Fort Edward Village Police Department', 'Corinth Village Police Department', 'Cambridge Village Police Department', 'WestSeneca Town Police Department', 'South Glens Falls Village Police Department', 'Glens Falls City Police Department', 'White Plains City Police Department', 'Southampton Town Police Department', 'Port Jervis City Police Department', 'Liberty Village Police Department', 'Monticello Village Police Department', 'Wappingers Falls Village Police Department', 'Village of Walden Police Department', 'Rhinebeck Village Police Department', 'Red Hook Village Police Department', 'Rome City Police Department', 'Greenburgh Town Police Department', 'New Paltz Town/Village Police Department', 'Maybrook Village Police Department', 'Freeport Village Police Department', 'Town of Poughkeepsie Police Department', 'Lloyd Town Police Department', 'Cornwall', 'Beacon City Police Department', 'Ellenville Village Police Department', 'Catskill Village Police Department', 'Haverstraw Town Police Department', 'Brighton Town Police Department', 'Scotia Village Police Department', 'Jamestown City Police Department', 'Yorktown Town Police Department', 'Orangetown Town Police Department', 'North Tonawanda City Police Department', 'Menands Village Police Department', 'Watervliet City Police Department', 'Waterford Town Police Department', 'Long Bch City Police Department', 'Carmel Town Police Department', 'Green Island Village Police Department', 'Stillwater Town Police Department', 'Mechanicville City Police Department', 'Johnstown City Police Department', 'Elmira City Police Department', 'Coxsackie Village Police Department', 'Cobleskill Village Police Department', 'Chatham Village Police Department', 'Guilderland Police Department', 'Auburn City Police Department', 'Ballston Spa Village Police Department', 'Athens Village Police Department', 'Poughkeepsie City Police Department', 'Altamont Police Department', 'Manlius Town Police Department', 'Gates Town Police Department', 'Webster Town/Village Police Department', 'Orchard Park Town Police Department', 'Rotterdam Town Police Department', 'Bethlehem Town Police Department', 'Ithaca City Police Department', 'Watertown City Police Department', 'Camillus Town/Village Police Department', 'Mount Pleasant Town Police Department']

def is_sendable(row):
  return (row[0].strip() not in ex_list and row[0] not in ex_list)

with open('NYPDRealREAL.csv', 'r') as fin, open('sendableNYPD.csv', 'w', newline='') as fout:
    state = 'CA'
    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_ALL)

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for row in reader:
      # print(row[13])
      if(is_sendable(row)):
        writer.writerow(row)
      else:
        print('skipped one!')

