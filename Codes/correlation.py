# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 20:13:10 2017

@author: Mahdi Aziz
"""
import numpy as np
import extraction
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
def lens(listoflists):
  return [len(x) for x in listoflists]
def cor(a,b):
    return np.corrcoef(a,b)[0, 1]
def plot_foursides(x,y1,y2,title,ax,ax22,Country_name,Col_except_name,Col_wanted_name,filename):
    fig, ax1 = plt.subplots()
    for axis in [ax1.xaxis, ax1.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(integer=True))
    lns1=ax1.plot(x, y1, 'b-')
    ax1.grid()
    ax1.set_xlabel('time (Year)')
    ax1.set_ylabel(ax22, color='b')
    ax1.tick_params('y', colors='b')
    ax1.set_title(title, fontsize='large')
    ax2 = ax1.twinx()
    lns2=ax2.plot(x, y2, 'r-')
    ax2.set_ylabel(ax, color='r')
    ax2.tick_params('y', colors='r')
    lns = lns1+lns2
    lgd =ax1.legend(lns, [Col_wanted_name,Col_except_name], loc='upper center', bbox_to_anchor=(0.5, -0.15))
    plt.show()
    fig.savefig(Country_name+"/"+Col_except_name+"/"+filename.replace(",","_").replace(" ","")+'.jpg',format='jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')
## other measures vs GDP
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
#The name without axis and axis and fullname of the columns that the Correlation is based upon
except_cols=[]
except_names=[]
except_axis=[]
for ii in range(1,11):
    except_cols.append(Hsheet[ii][4])
    except_names.append(Hsheet[ii][5].strip())
    except_axis.append(Hsheet[ii][6])


#Country_name=['Canada','China','Germany','Japan','United States']
for jj in range(0,len(Country_names)):
    Country_name=Country_names[jj]
    create_dir(Country_names[jj])
    for ii in range(0,len(except_names)):
        create_dir(Country_name+"/"+except_names[ii])
        col2=extraction.retrieve_col(Country_name+'.csv',except_cols[ii])
        col2c=[float(i) for i in col2]
        for kk in range(0,len(wanted_cols)):
            col2=col2c
            col1=extraction.retrieve_col(Country_name+'.csv',wanted_cols[kk])
            new_index=col1.index(next((x for x in col1 if x!='0'), '0'))
            colr=col1[::-1]
            last = len(colr)-colr.index(next((x for x in colr if x!='0'), '0'))
            col1=col1[new_index:last]
            col2=col2[new_index:last]
            col1=[float(i) for i in col1]
            corr=cor(col1,col2)
            if abs(corr)>0.66 and corr!=1.0:
                title=except_names[ii]+' correlates to \n' + wanted_cols_names[kk]+"\n with "+str(corr) +" correlation";
                x1 = np.arange(1960+new_index, 2017-(len(col2c)-last), 1)
                filename=except_names[ii] + "_"+wanted_cols_names[kk]
                plot_foursides(x1,col1,col2,title,except_axis[ii],wanted_axis[kk],Country_name,except_names[ii],wanted_cols_names[kk],filename)
        
        
## other measures vs GDP
#==============================================================================
# except_cols=['ï»¿Indicator Name','GDP (current US$)']
# col2=extraction.retrieve_col('Canada.csv',except_cols[1])
# col2=[float(i) for i in col2]
# wanted_cols=extraction.wanted_cols_func('Canada.csv',except_cols)
# for wanted_col in wanted_cols:
#     col1=extraction.retrieve_col('Canada.csv',wanted_col)
#     col1=[float(i) for i in col1]
#     corr=cor(col1,col2)
#     if abs(corr)>0.66:
#         print(except_cols[1]+' correlates to ' + wanted_col+" with "+str(corr) +" correlation")
#==============================================================================
        