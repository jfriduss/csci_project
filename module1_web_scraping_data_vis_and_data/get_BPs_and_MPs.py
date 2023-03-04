# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:19:58 2023

@author: jonat_od7omk3
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re



##GET THE COMPOUNDS WITH BOILING POINTS AND/OR MELTING POINTS

# f_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/'
# #b_urls = ['/XML?heading=BOILING+POINT', '/XML?heading=MELTING+POINT']
# b_url  = '/XML?heading=BOILING+POINT'

# has_BP = []

# for i in range(1,1000):
#     #print(i)
#     url = f_url + str(i) + b_url
#     h = requests.get(url)
#     bs = BeautifulSoup(h.content, "xml")
    
#     try:
#         if(bs.Message.get_text() != 'No data found'):
#             has_BP.append(i)
#     except:
#         has_BP.append(i)
# print(has_BP)


# b_url  = '/XML?heading=MELTING+POINT'

# has_MP = []

# for i in range(1,1000):
#     #print(i)
#     url = f_url + str(i) + b_url
#     h = requests.get(url)
#     bs = BeautifulSoup(h.content, "xml")
    
#     try:
#         if(bs.Message.get_text() != 'No data found'):
#             has_MP.append(i)
#     except:
#         has_MP.append(i)
# print(has_MP)

##DONE GETTING THE CIDs OF THE COMPOUNDS WITH BPs/MPs, AND NOW ACTUALLY GETTING
##THE VALUES



## GETTING THE BOILING/MELTING POINTS (but as a messy string)
# start_time = time.time()

# f_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/'
# b_url_bp  = '/XML?heading=BOILING+POINT'
# b_url_mp  = '/XML?heading=MELTING+POINT'


# CIDS_w_BPs = [4, 6, 11, 13, 19, 33, 34, 49, 66, 79, 93, 96, 107, 125, 126, 135, 174, 176, 177, 178, 179, 180, 196, 222, 227, 234, 240, 241, 243, 244, 260, 261, 262, 263, 264, 273, 280, 281, 284, 289, 294, 297, 299, 300, 301, 305, 308, 311, 313, 323, 325, 326, 335, 338, 340, 342, 356, 370, 379, 385, 398, 402, 403, 412, 428, 444, 447, 454, 460, 525, 527, 533, 545, 563, 564, 568, 612, 650, 660, 673, 674, 679, 681, 700, 702, 712, 713, 727, 743, 753, 757, 768, 774, 783, 784, 785, 787, 791, 795, 798, 807, 811, 813, 867, 873, 876, 878, 880, 887, 888, 892, 904, 931, 935, 936, 938, 942, 944, 947, 948, 949, 957, 962, 967, 971, 977, 978, 980, 985, 991, 992, 995, 996, 998, 999]
# CIDS_w_MPs = [4, 6, 11, 13, 19, 33, 34, 45, 49, 51, 58, 66, 70, 71, 72, 79, 86, 89, 93, 96, 106, 107, 111, 119, 125, 126, 127, 135, 137, 138, 140, 144, 174, 176, 177, 178, 179, 180, 187, 190, 196, 199, 203, 204, 222, 227, 234, 237, 239, 240, 241, 243, 244, 247, 248, 258, 259, 260, 261, 262, 263, 264, 271, 273, 275, 280, 281, 284, 289, 294, 297, 299, 300, 301, 305, 308, 309, 311, 312, 313, 323, 325, 328, 335, 338, 340, 342, 356, 359, 366, 370, 379, 385, 397, 398, 402, 403, 408, 409, 428, 444, 447, 454, 458, 460, 464, 487, 525, 527, 528, 533, 535, 546, 547, 564, 568, 586, 588, 597, 612, 647, 649, 650, 660, 670, 673, 674, 675, 679, 681, 700, 702, 712, 713, 727, 743, 750, 751, 753, 756, 757, 760, 767, 768, 772, 774, 777, 780, 781, 783, 784, 785, 787, 790, 791, 795, 798, 802, 807, 811, 813, 836, 838, 849, 860, 863, 864, 867, 873, 875, 876, 878, 880, 887, 888, 892, 896, 904, 913, 923, 931, 934, 935, 936, 938, 942, 944, 947, 948, 949, 957, 962, 967, 970, 971, 974, 977, 978, 979, 980, 984, 985, 991, 992, 995, 996, 997, 998, 999]

# d = {'CID': range(1,1000), 'BP':[], 'MP':[]}

# for i in d['CID']:
#     print(i)
#     if i in CIDS_w_BPs:
#         url = f_url + str(i) + b_url_bp
#         h = requests.get(url)
#         bs = BeautifulSoup(h.content, "xml")
#         try:
#             d['BP'].append(bs.StringWithMarkup.get_text())
#         except:
#             d['BP'].append(bs.Number.get_text())
            
#     else: d['BP'].append('unavailable')
        
#     if i in CIDS_w_MPs:
#         url = f_url + str(i) + b_url_mp
#         h = requests.get(url)
#         bs = BeautifulSoup(h.content, "xml")
#         try:
#             d['MP'].append(bs.StringWithMarkup.get_text())
#         except:
#             d['MP'].append(bs.Number.get_text())
            
#     else: d['MP'].append('unavailable')    

# print(time.time() - start_time)        
        

# df = pd.DataFrame(data = d)
# df.to_csv('pub_chem_1000_compounds_BP_MP_unparsed.csv')
## DONE GETTING THE BOILING/MELTING POINTS (but as a messy string)



df = pd.read_csv('.\pub_chem_1000_compounds_BP_MP_unparsed.csv')
d = df.to_dict(orient='list')

d['BP_parsed_C'] = []
d['has_units_BP'] = []
d['MP_parsed_C'] = []
d['has_units_MP'] = []


gVal = r"(?P<temp>[0-9]+)"
gUnits = r"[°](?P<units>[cCfF])"

for i in d['CID']:
    if d['BP'][i-1] != 'unavailable':
        get_BP = re.search(gVal, str(d['BP'][i-1]))
        getUnits = re.search(gUnits, str(d['BP'][i-1]))
        
        if getUnits: #the BP value was reported with units
            if (getUnits.group('units') == 'F') | (getUnits.group('units') == 'f') :
                BP_celsius = (5/9)*(int(get_BP.group('temp')) - 32) #convert to celsius
            else: BP_celsius = get_BP.group('temp')
            
            d['BP_parsed_C'].append(BP_celsius)
            d['has_units_BP'].append('y')
        
        else: #the BP value may not have been reported with units
            d['BP_parsed_C'].append(get_BP.group('temp'))    
            d['has_units_BP'].append('n')
            print(str(d['BP'][i-1]))
   
    else:
        #print(d['BP_parsed_C'])
        d['BP_parsed_C'].append('unavailable')
        d['has_units_BP'].append('N/A')
    
    #do the same for melting points
    
    if d['MP'][i-1] != 'unavailable':
        get_MP = re.search(gVal, str(d['MP'][i-1]))
        getUnits = re.search(gUnits, str(d['MP'][i-1]))
        
        if getUnits: #the MP value was reported with units
            if (getUnits.group('units') == 'F') | (getUnits.group('units') == 'f') :
                MP_celsius = (5/9)*(int(get_MP.group('temp')) - 32) #convert to celsius
            else: MP_celsius = get_MP.group('temp')
            
            d['MP_parsed_C'].append(MP_celsius)
            d['has_units_MP'].append('y')
        
        else: #the BP value may not have been reported with units
            d['MP_parsed_C'].append(get_MP.group('temp'))    
            d['has_units_MP'].append('n')
            print(str(d['MP'][i-1]))
    else:
        d['MP_parsed_C'].append('unavailable')
        d['has_units_MP'].append('N/A')

new_df = pd.DataFrame(data = d)
new_df.to_csv('pub_chem_1000_compounds_BP_MP_parsed.csv')
