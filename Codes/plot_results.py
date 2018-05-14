# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:25:35 2017

@author: Mahdi Aziz - SN: 8024161
"""

import extraction
import seaborn as sb
import matplotlib.pyplot as plt

def plot_res(wanted_cols,xlabel,ylabel,title,picname):
    cols=["Canada","China","Germany","Japan","United States"]
    result=extraction.retrieve_cols('WDIEXCEL.csv',cols[0],wanted_cols)
    print(result)
    result2=extraction.retrieve_cols('WDIEXCEL.csv',cols[1],wanted_cols)
    result3=extraction.retrieve_cols('WDIEXCEL.csv',cols[2],wanted_cols)
    result4=extraction.retrieve_cols('WDIEXCEL.csv',cols[3],wanted_cols)
    result5=extraction.retrieve_cols('WDIEXCEL.csv',cols[4],wanted_cols)
    sb.set_palette("colorblind")
    sb.set_style("darkgrid")
    sb.set_context("notebook",rc={"lines.linewidth":4.3})
    fig = plt.figure(figsize=(20,10),dpi=300);
    x=range(1960,2017)
    plt.plot(x,result,'r--',x,result2,'b--',x,result3,'g--',x,result4,'y--',x,result5,'--o')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(cols)
    plt.title(title)
    fig.savefig(picname,format='jpg')
    
def plot_res_all():
    #plot_res("Inflation, GDP deflator (annual %)",'Years','Inflation rate','The inflation rate of 5 developed countries from 1960 to 2016','inflation.jpg')
    #plot_res("Inflation, consumer prices (annual %)",'Years','Inflation rate','The inflation rate of 5 developed countries from 1960 to 2016','inflation2.jpg')
    plot_res('Unemployment, total (% of total labor force) (national estimate)','Years','Unemployment rate','The unemployment rate of 5 developed countries from 1960 to 2016','unemployment.jpg')
plot_res_all()