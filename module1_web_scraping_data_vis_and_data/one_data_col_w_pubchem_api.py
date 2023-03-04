# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:36:34 2023

@author: jonat_od7omk3
"""

import pubchempy as pcp
#from pprint import pprint
#import requests
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
#import numpy as np
import selfies as sf

n = 4

elements_repr = ['C']
#d = {'CID': range(1,10**n), 'smiles_repr':[], 'selfies_repr':[], 'h_acc':[], 'h_don':[], 'C':[]}
d = {'CID': range(2400,4300), 'smiles_repr':[], 'selfies_repr':[], 'h_acc':[], 'h_don':[], 'C':[]}

start_time = time.time()

#note: 10**1 --> 2-3 second run time (without making dataframe)
    #with making dataframe, 4 seconds. With making dataframe, but with chrome closed: 2.5 seconds
# 10**2 --> 34 second run time
#10**3 --> 303 second run time (with chrome closed, but with printing what CID am on)
#

for i in d['CID']:
    if (i % 100 == 0):
        print(i)
    compound = pcp.Compound.from_cid(i)
    d['smiles_repr'].append(compound.isomeric_smiles)
    d['selfies_repr'].append(sf.encoder(compound.isomeric_smiles))
    d['h_acc'].append(compound.h_bond_donor_count)
    d['h_don'].append(compound.h_bond_acceptor_count)    
    
    #print(compound.molecular_formula)
    
    for j in ( set(compound.elements) - set(elements_repr) ):
        d[j] = [0]*len(d['C'])
        elements_repr.append(j)        
        
    for k in elements_repr:
        d[k].append(compound.elements.count(k))        

print(time.time() - start_time)        
    #if 'C' in d.keys():
        #print(d['C'])

    #if 'P' in d.keys():
        #print(d['P'])
        
    #print('new compound \n\n')
#for i in d:
#    print(len(d[i]))
#    print (i, d[i])


df = pd.DataFrame(data = d)
df.to_csv('pub_chem_2400_to_4300_compounds.csv')