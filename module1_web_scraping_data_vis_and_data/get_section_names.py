# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 00:09:24 2023

@author: jonat_od7omk3
"""
import time
from selenium import webdriver
import pandas as pd


start_time = time.time()


driver = webdriver.Chrome(executable_path='C:\\Users\jonat_od7omk3\chromedriver_win32\chromedriver')

d = {'CID': range(1,1000), 'sections':[]}

for j in d['CID']:
    lst = []
    
    driver.get('https://pubchem.ncbi.nlm.nih.gov/compound/' + str(j))
    section_names = driver.find_elements("xpath", '//div[@class="relative p-xl-right f-gray"]') #the "div" vs. "td" vs. ... is important!

    while(len(section_names) == 0):
        section_names = driver.find_elements("xpath", '//div[@class="relative p-xl-right f-gray"]') 

    
    for i in range(len(section_names)):
        lst.append(section_names[i].text)
    
    d['sections'].append(lst)
    
driver.quit()
print(time.time() - start_time)

df = pd.DataFrame(data = d)
df.to_csv('pub_chem_1000_sections.csv')

