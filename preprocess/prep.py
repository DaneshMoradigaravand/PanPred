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
import os.path


class prep_mod:
    def __init__(self, path):
        self.path=path

    def input_preparation(self,metadata,id_drug, input_gene, structure, type_inp):
        import pandas as pd
        output=pd.DataFrame()
        metadata_gn=pd.DataFrame()
        
        structure_inp=pd.DataFrame()
        gene_inp=pd.DataFrame()
        metadata_inp=pd.DataFrame()
        
        
        if not os.path.isfile(self.path+"/"+metadata):
            print("No metadata file")
            return
        else:
            print("Reading metadata file")
            metadata_inp= pd.read_csv(self.path+"/"+metadata,index_col=0)
            print("Metadata file is imported")
            
        if not os.path.isfile(self.path+"/"+input_gene):
            print("No accessory gene file")
            return
        else:
            print("Reading accessory gene file")
            gene_inp= pd.read_csv(self.path+"/"+input_gene,index_col=0)
            print("Accessory gene file is imported")
            
        if not os.path.isfile(self.path+"/"+structure):
            print("No structure file")
            return
        else: 
            print("Reading population structure file")
            structure_inp= pd.read_csv(self.path+"/"+structure,index_col=0)
            print("Structure file is imported")
            
        if type_inp=="GYS":
            #1/1/1
            print("salam")
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1,0]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure_inp,how='inner').join(gene_inp,how='inner')
        elif type_inp=="GS":
            #0/1/1
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure_inp,how='inner').join(gene_inp,how='inner')
        elif type_inp=="GY":
            #1/0/1
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1,0]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(gene_inp,how='inner')
            print(gene_inp.shape)
            print(metadata_inp.shape)
            
        elif type_inp=="S":
            #0/1/0
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure_inp,how='inner')
                 
        elif type_inp=="G":
            #0/0/1
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(gene_inp,how='inner')
        elif type_inp=="SY":
            #1/1/0
            metadata_gn=metadata_inp.iloc[:,[int(id_drug)+1,0]]
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="S", value=0)
            metadata_gn.iloc[:,0]=metadata_gn.iloc[:,0].replace(to_replace="R", value=1)
            output=metadata_gn.join(structure_inp,how='inner')
        
        output.to_csv(self.path+"/curated_input_"+ type_inp+".csv")
        print(output.shape)
        return
    
    def label_encoder(self, structure):
        from sklearn.preprocessing import LabelEncoder
        structure_inp=pd.DataFrame()
        if not os.path.isfile(self.path+"/"+structure):
            print("No structure file")
            return
        else: 
            print("Reading population structure file")
            structure_inp= pd.read_csv(self.path+"/"+structure,index_col=0)
            print("Structure file is imported")
        
        le=LabelEncoder()
        for col in structure_inp.columns.values:
            le.fit(structure_inp[col].values)
            structure_inp[col]=le.transform(structure_inp[col])
        structure_inp.to_csv(self.path+"/"+structure+"_labelencoded.csv")
        print("Structure file is created")
        return
    
    
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

