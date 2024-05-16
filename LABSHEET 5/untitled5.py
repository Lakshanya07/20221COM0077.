# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mbzaIvZsR0zpKOoHd3j_jmHTmcRdkYNh
"""

import pandas as pd
meteorites=pd.read_csv('/content/Meteorite_Landings.csv')
meteorites

meteorites.name

meteorites.columns

meteorites.index

import requests

response = requests.get(
    'https://data.nasa.gov/resource/gh4g-9sfh.json',
    params={'$limit': 50_000}
)

if response.ok:
  payload = response.json()
else:
  print(f'Request was not successful and returned code : {response.status_code}')
  payload = None

import pandas as pd

df=pd.DataFrame(payload)
df.head(3)

meteorites.columns

meteorites.dtypes

meteorites.head()

meteorites.tail()

meteorites.info()

meteorites.name

meteorites[['name','mass (g)']]

meteorites[100:104]

meteorites.iloc[100:104,[0,3,4,6]]

meteorites.loc[100:104,'mass (g)':'year']

(meteorites['mass (g)'] > 50) & (meteorites.fall =='Found')

meteorites[(meteorites['mass (g)'] > le6)&(meteorites.fall=='fell')]

meteorits.query("'mass (g)' >  le6 and fall == 'fell'")





