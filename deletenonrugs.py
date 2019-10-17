import csv

# Checks if SKU is in rug list
product_info = []
with open('slimmedprices.csv', 'r') as find:

  # define reader and writer objects
  reader = csv.reader(find, skipinitialspace=True)

  # iterate and write rows based on condition
  for i in reader:
    product_info.append({'SKU': i[0],'Cost': i[1], 'MAP': i[2], 'MSRP': i[3]})

# Set Headers
fnames = ["Status","Product Type","SKU","Design","Product Description","Collection","Romance Copy","Parent ID","UPC","Color(s)","Material(s)","Generic Material(s)","Style","Shape","Size Name","Size Group","Length","Width","Item Weight","Ship Weight","Ship Length","Ship Width","Ship Height","Fringe Length","Surya Ship Method","3rd Party Ship Method","Country of Origin","Construction","Designer","Top Seller","Outdoor Safe","Has Fringe","---RUGS---","Backing","Pile Height","Pile Type","Knot Type","---LIGHTING---","Lighting Type","Cord Color","Base Color","Number of Lights","Bulbs Included","Number of Shades","Number of Tiers","Shade Included","Shade Shape","Shade Color","Bulb Wattage","Has Dimmer","Built-In Outlet","Adjustable","Has Swing Arm","Light Direction","Switch Location","Switch Type","Shade Height","---TEXTILES---","Fill","Tassels","Piped Edges","Fringe","Flange","Reversible","Removable Cover","Closure","Set Includes","---HARD LINES---","Hang Orientation","Hang Hardware","Framed","Frame Color","Frame Material","Beveled Glass","Tempered Glass","Mirror Shape","Print Process","Printed On","Is Watertight?","---IMAGES---","Flatshot","Roomscene","Styleshot","Front","Texture","Fold","Pile","Swatch","Corner","---URL IMAGES---","Flatshot URL","Roomscene URL","Styleshot URL","Front URL","Texture URL","Fold URL","Pile URL","Swatch URL","Corner URL","Cost", "MAP", "MSRP"]
# Get Cost
def get_cost(sku):
  for i in product_info:
    if(i.get('SKU') == sku):
      return i.get('Cost')
    else:
      continue
  return None
# Get MAP
def get_map(sku):
  for i in product_info:
    if(i.get('SKU') == sku):
      return i.get('MAP')
    else:
      continue
  return None
# Get MSRP
def get_msrp(sku):
  for i in product_info:
    if(i.get('SKU') == sku):
      return i.get('MSRP')
    else:
      continue
  return None

with open('onlypricedrugs.csv', 'r') as csvfile, open('testoutput.csv', 'w') as fout:
  reader = csv.DictReader(csvfile)
  writer = csv.DictWriter(fout, fieldnames=fnames, delimiter=',', quoting=csv.QUOTE_ALL)
  writer.writeheader()
  for row in reader:
    row['Cost'] = get_cost(row['SKU'])
    row['MAP'] = get_map(row['SKU'])
    row['MSRP'] = get_msrp(row['SKU'])
    writer.writerow(row)
  
