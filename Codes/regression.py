# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 09:04:59 2017

@author: Mahdix
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as py
import extraction
import os
def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
#main program
Hsheet=extraction.retrieve_Hsheet('Hsheet.csv')
Country_names=[]
for ii in range(1,6):
    Country_names.append(Hsheet[ii][0].strip())

# The name of columns that the main one is going to correlate based on
wanted_cols=[]
wanted_cols_names=[]
wanted_axis=[]
for ii in range(1,60):
    wanted_cols.append(Hsheet[ii][1])
    wanted_cols_names.append(Hsheet[ii][2].strip())
    wanted_axis.append(Hsheet[ii][3])
reg='Regression'
create_dir(reg)
for jj in range(0,len(Country_names)):
    Country_name=Country_names[jj]
    create_dir(reg+"/"+Country_name)
    for kk in range(0,len(wanted_cols)):
        col1=extraction.retrieve_col(Country_name+'.csv',wanted_cols[kk])
        new_index=col1.index(next((x for x in col1 if x!='0'), '0'))
        colr=col1[::-1]
        last = len(colr)-colr.index(next((x for x in colr if x!='0'), '0'))
        col1=col1[new_index:last]
        col1=[float(i) for i in col1]
        x=np.arange(1960+new_index, 2017-(len(colr)-last), 1)
        x2=np.arange(1960+new_index,2020)
        y=np.array(col1)
        fig = py.figure()
        p1=sc.polyfit(x,y,1)
        p2=sc.polyfit(x,y,2)
        py.plot(x,y,'o')
        lns1=py.plot(x2,sc.polyval(p1,x2),'r-')
        lns2=py.plot(x2,sc.polyval(p2,x2),'b--')
        py.title('Regression analysis for ' +wanted_cols_names[kk])
        py.xlabel('time (Year)')
        py.ylabel(wanted_axis[kk])
        lns=lns1+lns2
        lgd =py.legend(lns, ['linear model','quadratic model'], loc='upper center', bbox_to_anchor=(0.5, -0.15))
        py.show()
        fig.savefig(reg+"/"+Country_name+"/"+wanted_cols_names[kk].replace(",","_").replace(" ","")+'.jpg',format='jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')