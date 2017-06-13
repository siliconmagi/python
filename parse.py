# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:41:50 2017

@author: ITAssistant
"""
import pandas as pd

sD = pd.read_excel('./solidData.xlsx')
vD = pd.read_excel('./vendorDataTrim.xlsx')

print(sD)
print(vD)

# print(vD.Year.str.replace('2007','HI', case=False))

# create column start year
vD['syear'] = vD.Year.str.replace(r'-.*$', '', case=False)
print(vD.syear)

# create column end year
vD['eyear'] = vD.Year.str.replace(r'.*-', '', case=False)
print(vD.eyear)

# concat
vD['concat'] = vD['Make'] + " " + vD['Model4']
vD['fMatch'] = vD.syear + "-" + vD.eyear + " " + vD.Make + " " + vD.Model4
print(vD.fMatch)
print(sD['product attribute:make'])
print(sD['product attribute:model'])
sD['fMatch'] = sD['product attribute:make'] + sD['product attribute:model']