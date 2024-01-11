import numpy as np
import requests
import pandas as pd


def multiple(a, b):
   url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
   df=pd.read_csv(url)

   return df.Country  #np.multiply(a, b).tolist()