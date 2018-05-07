#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:51:38 2018

@author: dm16
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import sys
import os
import warnings
warnings.filterwarnings('ignore')


class prep_mod:
    def __init__(self, path):
        self.path=path
        
    def train_test_split(self,metadata):
        ratio=0.7
        tmp_csv=pd.read_csv(self.path+"/"+metadata, index_col=0)
        for id_d in range(1,tmp_csv.shape[1]):
            tmp_csv.iloc[:,id_d].isnull()
            id_phen=np.where(tmp_csv.iloc[:,id_d].notnull())[0]
            len_id_phen=len(id_phen)
            ind=tmp_csv.index[id_phen]
            train=np.random.choice(ind, size=int(len_id_phen*ratio), replace=False)
            test=np.random.choice(ind, size=int(len_id_phen*(1-ratio)), replace=False)
            pd.DataFrame(train).to_csv(self.path+"/train_"+str(id_d)+".csv")
            pd.DataFrame(test).to_csv(self.path+"/test_"+str(id_d)+".csv")

    #delete duplicated columns      X_train = scale(X_train)
    def dedup_preprocess(self, Rtab,Gene_PA,del_part=True):     
        print("Reading gene_presence_absence.Rtab file")
        tmp_tab=pd.read_table(self.path+"/gene_presence_absence.Rtab", index_col=0)
        if del_part==True:
            print("Delete non-unique Genes activated")
            print("Reading gene_presence_absence.csv file")
            tmp_csv=pd.read_csv(self.path+"/gene_presence_absence.csv", usecols = ["Gene","Non-unique Gene name"])
            id_un=np.where(tmp_csv["Non-unique Gene name"].isnull())[0]
            print("Number of genes before removing genes: %d" % tmp_tab.shape[0])
            tmp_tab=tmp_tab.iloc[id_un,:]
            print("Number of genes after removing genes: %d" % tmp_tab.shape[0])

        print("\nRemoving gene clusters with identical frequency")
        print("Number of genes before clsutering: %d" % tmp_tab.shape[0])
        tmp_dedup=tmp_tab.drop_duplicates()
        print("Number of genes after clsutering: %d" % tmp_dedup.shape[0])
        Gene_inp=tmp_dedup.transpose()


    def label_encoder(path, structure):
        from sklearn.preprocessing import LabelEncoder
        output_st=pd.read_csv(path+structure,index_col=0)
        le=LabelEncoder()
        for col in output_st.columns.values:
            le.fit(output_st[col].values)
            output_st[col]=le.transform(output_st[col])
        return output_st

#Year-Structure-Gene
    def input_preparation(metadata,id_drug, input_gene, structure, type_inp):
        import pandas as pd
        output=pd.DataFrame()
        metadata_gn=pd.DataFrame()

        if type_inp==111:
            #1/1/1
            metadata_gn=metadata.iloc[:,[id_drug+1,1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure,how='inner').join(input_gene,how='inner')
        elif type_inp==011:
            #0/1/1
            metadata_gn=metadata.iloc[:,[id_drug+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure,how='inner').join(input_gene,how='inner')
        elif type_inp==101:
            #1/0/1
            metadata_gn=metadata.iloc[:,[id_drug+1,1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(input_gene,how='inner')
        elif type_inp==010:
            #0/1/0
            metadata_gn=metadata.iloc[:,[id_drug+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure,how='inner')
        elif type_inp==001:
            #0/0/1
            metadata_gn=metadata.iloc[:,[id_drug+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(input_gene,how='inner')
        elif type_inp==010:
            #1/1/0
            metadata_gn=metadata.iloc[:,[id_drug+1,1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure,how='inner')
        return output
    

    