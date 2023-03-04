# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:21:11 2023

@author: jonat_od7omk3
"""

from rdkit import Chem
import pandas as pd



orig_df = pd.read_csv('.\pub_chem_1000_compounds.csv')
orig_d = orig_df.to_dict(orient='list')

substructs = [Chem.MolFromSmarts('CO'), Chem.MolFromSmarts('C=O'), Chem.MolFromSmarts('CN'), Chem.MolFromSmarts('C=N'),
              Chem.MolFromSmarts('C#N')]

d_bonding_list = [[],[],[],[],[]]

for i in orig_d['CID']:
    m = Chem.MolFromSmiles(orig_d['smiles_repr'][i-1])
    
    for j in range(5):
        n_occurances_of_b_type_in_c = len( m.GetSubstructMatches(substructs[j]) )
        d_bonding_list[j].append(n_occurances_of_b_type_in_c)

d_bonding = {}
d_bonding['CO'] = d_bonding_list[0]
d_bonding['C=O'] = d_bonding_list[1]
d_bonding['CN'] = d_bonding_list[2]
d_bonding['C=N'] = d_bonding_list[3]
d_bonding['C#N'] = d_bonding_list[4]

bonding_df = pd.DataFrame(data = d_bonding)

bonding_df.to_csv('pub_chem_1000_compounds_nitr_and_oxygen_bonding.csv')