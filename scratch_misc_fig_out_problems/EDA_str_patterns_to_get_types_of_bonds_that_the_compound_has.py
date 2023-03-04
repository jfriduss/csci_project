# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:19:20 2023

@author: jonat_od7omk3
"""

#this was a bad approach, that I tried before realizing that RDKit has functionalities that mostly address this problem
#and that the molecular graph, not a string representation, should be used

import pandas as pd


df = pd.read_csv('.\pub_chem_1000_compounds.csv')
d = df.to_dict(orient='list')

##get number of 

d['n_rings'] = []
d['n_branches'] = []


for i in d['CID']:
    smiles_repr = d['smiles_repr'][i-1]
    num_b = 0
    num_r = 0
    
    for j in range(len(smiles_repr)):
        if j == '(': num_b += 1
        
        try:
            r = int(j)
            if r > num_r: num_r = r

        except:            
            pass
    
    d['n_rings'].append(num_r)
    d['n_branches'].append(num_b)

## get the different string patterns that occur with nitrogens and oxygens,
## e.g. ')OC' , '=O)' are example patterns for oxygen, in order to classify the
## different types of bonding each compound has

# str_patterns = {'O':[] , 'N':[]}

# for i in d['CID']:
#     smiles_repr = d['smiles_repr'][i-1]
    
#     for j in range(1, len(smiles_repr) -1):
        
#         chars = smiles_repr[j-1:j+2]
        
#         if chars[1] == 'O':
#             if not (chars in str_patterns['O']):
#                 str_patterns['O'].append(chars)
        
#         if chars[1] == 'N':
#              if not (chars in str_patterns['N']):
#                 str_patterns['N'].append(chars)           

# print(str_patterns['O'])
# print(str_patterns['N'])

##Some of the string patterns above are difficult for me to work with right now
##(for example ones with formal charges and '[OH' ). I would
##like to consider temporarily not working with these ones, but I want to know
##what percentage of these fit into this category. So I am going to visualize
##how many occurances of these ones show up.

str_patterns = {'O':[] , 'N':[]}

for i in d['CID']:
    smiles_repr = d['smiles_repr'][i-1]
    
    for j in range(2, len(smiles_repr) - 2):
        
        chars = smiles_repr[j-2:j+3]
        
        if chars[1] == 'O':
            if not (chars in str_patterns['O']):
                str_patterns['O'].append(chars)
        
        if chars[1] == 'N':
             if not (chars in str_patterns['N']):
                str_patterns['N'].append(chars)           

print(str_patterns['O'])
print(str_patterns['N'])
