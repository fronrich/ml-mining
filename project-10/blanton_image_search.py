import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()

# the other imports
# import pandas as pd
# import numpy as np
# import urllib, json, requests, re
# import xlsxwriter

# args should be as followed
# input = 'blanton_list_fixed.xlsx'
# output = 'blanton_list_images.xlsx'

# filter to get only rows with images
def filter_images(df):
  for row, data in df.iterrows():
    if row == 1372:
        break
    #create url
    title = df.iloc[row]['Title']
    name = df.iloc[row]['Artist sort name']
    accession = df.iloc[row]['Accession #']
        
    url = f"https://collection.blantonmuseum.org/objects-1/info?query=mfs all \"{accession} {title} {name}\"&sort=9"
    #get JSON data and get rid of any trailing 
    response  = requests.get(url)
    text = response.text

    current_has_image = text.find("This object does not have an image") == -1
    
    df.at[row,'has_image'] = False
    if current_has_image:
        df.at[row, 'has_image'] = True

  return df[df['has_image'] == True].copy()

# compare the size of the original df to the cleaned df
def compare_sizes(df, df_images):
  # compare sizes of old and new dataframe
  df_rows = len(df.axes[0])
  df_images_rows = len(df_images.axes[0])
  diff = (df_images_rows / df_rows) * 100

  print(str(diff) + "% of rows have images")

# create random table for each f us
def create_rand(df_images):
  #Create databased of random images to judge
  rand_fron = df_images.sample(n=60)
  rand_ana = df_images.sample(n=60)

  rand_fron['student_id'] = 'Frp323'
  rand_ana['student_id'] = 'AnaW4804'

  rand_fron['Emotional_Reaction'] = 0
  rand_ana['Emotional_Reaction'] = 0

  rand_fron['Asthetically_Pleasing'] = 0
  rand_ana['Asthetically_Pleasing'] = 0

  rand_fron.head()

  #Saving Fron Random
  writer = pd.ExcelWriter('student_Frp323_blanton.xlsx', engine='xlsxwriter', options = {'string_to_numbers' : False})
  rand_fron.to_excel(writer)
  writer.save()

  #Saving Ana Random
  writer = pd.ExcelWriter('student_AnaW4804_blanton.xlsx', engine='xlsxwriter', options = {'string_to_numbers' : False})
  rand_ana.to_excel(writer)
  writer.save()

def main(input, output):
  df = pd.read_excel(input_file, dtype={i:object for i in range(0,10)})

  # filter and save
  df_images = filter_images(df)
  writer = pd.ExcelWriter(output_file, engine='xlsxwriter', options = {'string_to_numbers' : False})
  df_images.to_excel(writer)
  writer.save()

  # compare size of original and cleaned df
  compare_sizes(df, df_images)

  # create random datasets for each of us
  create_rand(df_images)

# invoke main
main(args.input_file, args.output_file)