# -*- coding: utf-8 -*-

"""Main module."""
import pandas as pd
import csv
from genedb import cleanerfunc

# def removespecchar(test):
#     import re
#     if type(test) == str:
#         test2=re.sub('\t','',test)
#         test=re.sub('\"','',test2)
#     return(test)
"""String Cleaning Function."""


"""Function to create bed file.
   Changes excel file into seperate bed files"""
def createbed(dfgenes, disease, sheetindex):
    df=pd.read_excel("data/MyeloidGeneKB01.xlsx", sheetname=sheetindex, index_col="GeneSymbol", parse_cols = [0,1,2,3,4])
    df.columns= disease +"_"+ df.columns
    dfgenes2 = dfgenes.join(df,  how="outer")
    dfgenes2.reset_index(inplace=True)
    dfgenes2=dfgenes2.fillna("")
    dfgenes2=dfgenes2.applymap(cleanerfunc.removespecchar)
    collist=list(dfgenes2.columns)
    newcollist=collist[6:9] + collist[0:6] + collist[9:]
    dfgenes2.to_csv("data\\" + disease+".bed", sep='\t', columns=newcollist, index=False)

dfgenes=pd.read_excel("data/MyeloidGeneKB01.xlsx", sheetname=0,index_col="GeneSymbol", dtypes=object)
myeloidDiseaseList = ["Unknown", "AML", "MDS", "MPN", ]
myeloidSheetList = [1,2,3,4]
for disease, sheetindex in zip (myeloidDiseaseList, myeloidSheetList):
    createbed(dfgenes,disease,sheetindex)

