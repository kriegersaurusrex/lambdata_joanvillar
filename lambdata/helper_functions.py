"""helper functions"""

"""Checks the dataframe for null values 
and returns the number of missing values"""

import pandas as pd 

def null_count(df):
  cnt = 0
  for x in df.columns:
    a = df[x].isnull().sum()
    cnt += a
  return cnt

"""Function splits date to Month, Day, Year columns"""

def split_dates(date_series):
  newdf = []
  for x in range(len(date_series)):
    data_date = str(date_series.values[x]).strip('[\'').strip('\']').split('/')
    newdf.append(data_date)
  add_data = pd.DataFrame(data=newdf,columns=['Month', 'Day', 'Year'])
  new_df = pd.concat([date_series,add_data], axis=1)
  return new_df