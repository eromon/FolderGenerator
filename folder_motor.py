# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:30:54 2017

@author: Eromon D Great
"""

import os as os
import pandas as pd



xl = pd.ExcelFile('dl-auto.xlsx')
names = xl.sheet_names
names = names[1:]
#print(names)
rootPath = "C:\\Users\\Eromon D Great\\.spyder-py3\\motor\\"
views = ["front_view", "rear_view","side_view"]
years =[]
for i,brand in enumerate(names):
    df = pd.read_excel("dl-auto.xlsx", sheetname=brand)
    years = df["model_year"]
    #df.loc["model_year"]
    years = years.astype(str)
    #print(years,brand)
    os.makedirs(os.path.join(rootPath,brand),exist_ok=True)
    brand = brand.strip()
    for i,year in enumerate(years):
        os.makedirs(os.path.join(rootPath,brand,year),exist_ok=True)
        for s,model in enumerate(df.model_name[years== year].astype(str)):
            os.makedirs(os.path.join(rootPath,brand,year,model),exist_ok=True)
            for view in views:
                os.makedirs(os.path.join(rootPath,brand,year,model,view),exist_ok=True)