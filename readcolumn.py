import pandas as pd
from glob import glob
import shutil

df = pd.read_csv('./Data/CORRECTISIZES.csv')
saved_column = df.SKU #you can also use df['column_name']

def contains_sku(file_name):
  just_sku = file_name[file_name.index('Images/')+7:file_name.index('-fold.jpg')].upper()
  #return just_sku
  testing = just_sku.strip()
  print(testing)
  return (testing in saved_column.values)

for file_name in glob('./Images/*.jpg'):
  if(contains_sku(file_name)):
    shutil.move(file_name, './Output/')
  else:
    continue
