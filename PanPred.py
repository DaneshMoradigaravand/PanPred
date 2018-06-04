#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
#sys.path.append("./")
from optparse import OptionParser
from argparse import ArgumentParser
#from prep import print_o
#from PanPred import *

from preprocess.prep import prep_mod
from predict.MLfunctions import LR
from predict.MLfunctions import RF
from predict.MLfunctions import GB
from predict.MLfunctions import DL

USAGE_STR = """Program: PanPred (Machine Learning tools to predict antibiotic resistance from NGS data)
Version: 0.1
Contact: Danesh Moradigaravand <d.morady@gmail.com>

Usage: PanPred <command> [options]

Command:
\t\t    preprocess\t    preprocess and creates the NGS input data for Machine Learning tools
\t\t    predict_LR _RF _GB _DL\t    Calls a Machine Learning model, i.e. Logistic regression, RandomForests, GradientBoosted and Deep Learning, to predict resistance from input
"""

USAGE_PREPROCESS = """Preprocess and creates the NGS input data for Machine Learning tools
Usage:
PanPred preprocess [options]

Options:
        -p STR   path to csv and Rtab files (Roary output files), default value: current path
        -c STR   create: create input file,  encode: label encoder for population structure, dedup: prepare Roary output
        -d STR   drug id number in the metadata file
        -i STR   input model ['GY', 'GYS', 'G','GS', 'S', 'SY']
        
        -m STR   name of the metadata file 
        -g STR   name of the accessory gene file
        -s STR   name of the population strcuture file
        
        -r STR   name of Rtab file from Roary output (.Rtab)
        -a STR   name of gene presence absence file from Roary output (.csv)
"""

"""Map sequencing reads to the reference for multiple sets of reads """ 
def preprocess_f():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    
    parser.add_option("-c", "--createinput", type="string", dest="input", default=None)
    parser.add_option("-i", "--type", type='choice', choices=('GY', 'GYS', 'G','GS', 'S', 'SY'), dest="type", default=None)
    parser.add_option("-d", "--drug", type='string', dest="drug", default=None)

    parser.add_option("-m", "--metadata", type="string", dest="metadata", default=None)
    parser.add_option("-g", "--gene", type="string", dest="gene", default=None)
    parser.add_option("-s", "--structure", type="string", dest="structure", default=None)
    
    parser.add_option("-r", "--Rtab", type="string", dest="Rtab", default=None)
    parser.add_option("-a", "--Accgen", type="string", dest="Accgen", default=None)
    
    (options, args) = parser.parse_args()
    
    if options.input == "create" and options.type != None and options.drug != None and options.metadata != None and  options.gene != None and  options.structure != None :
        prep_mod(options.path).input_preparation(options.metadata,options.drug,options.gene, options.structure, options.type)       
    elif options.input == "encode" and  options.structure != None and options.type == None and options.drug == None and options.gene == None and options.metadata == None:
        prep_mod(options.path).label_encoder(options.structure)
    elif options.input == "dedup" and  options.Rtab != None and options.structure == None and options.type == None and options.drug == None and options.Accgene != None and options.gene == None and options.metadata == None:
        prep_mod(options.path).dedup_preprocess(options.Rtab,options.Accgen)
    else:
        print(USAGE_PREPROCESS)
        return

#dedup_preprocess(self, Rtab,Gene_PA,del_part=True):

USAGE_PREDICT_LR = """Calls a Machine Learning modelLogistic regression
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -g FLT    L2 penalty
        -r FLT    train/test ratio
""" 

def predict_LR():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    parser.add_option("-i", "--input", type="string", dest="input", default=None)


    parser.add_option("-g", "--penalty", type="float", dest="Cval", default=0.0)
    parser.add_option("-r", "--ratio", type="float", dest="split", default=0.7)
    (options, args) = parser.parse_args()
    print(options.Cval)
    if options.Cval == None  or not isinstance(options.Cval, float) or options.split == None or options.input == None :
        print(USAGE_PREDICT_LR)
        return
    else:
        LR(options.path).LogisticRegression_f(options.input,options.split,options.Cval)

USAGE_PREDICT_RF = """Calls a Machine Learning model RandomForests
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio
""" 

def predict_RF():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    parser.add_option("-i", "--input", type="string", dest="input", default=None)
    parser.add_option("-r", "--ratio", type="float", dest="split", default=0.7)
    
    parser.add_option("-f", "--maxfeatures", type="string", dest="maxf", default=None)
    parser.add_option("-n", "--nestimators", type="float", dest="numest", default=10)
   
    (options, args) = parser.parse_args()
    print(options.maxf)
     
    if options.split == None  or options.maxf == None or options.numest == None or options.input == None :
        print(USAGE_PREDICT_RF)
        return
    else:
        RF(options.path).RandomForests_f(options.input, options.split,options.maxf,options.numest)

#RandomForests_f(self,input_file, ratio,max_features_pr, n_estimators_pr):

USAGE_PREDICT_GB = """Calls a Machine Learning model GradientBossting 
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio
""" 

def predict_GB():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    parser.add_option("-i", "--input", type="string", dest="input", default=None)
    parser.add_option("-r", "--ratio", type="float", dest="split", default=0.7)
    
    parser.add_option("-f", "--maxfeatures", type="string", dest="maxf", default=None)
    parser.add_option("-n", "--nestimators", type="float", dest="numest", default=10)
   
    (options, args) = parser.parse_args()
    print(options.maxf)
    
    if options.split == None  or options.maxf == None or options.numest == None or options.input == None :
        print(USAGE_PREDICT_GB)
        return
    else:
        GB(options.path).GradientBoostingClassifier_f(options.input, options.split,options.maxf,options.numest)

    

USAGE_PREDICT_DL = """Calls a Machine Learning model Deep Learning
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio
""" 

def predict_DL():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    parser.add_option("-i", "--input", type="string", dest="input", default=None)
    parser.add_option("-r", "--ratio", type="float", dest="split", default=0.7)
    
    (options, args) = parser.parse_args()
    
    if options.split == None  or options.input == None :
        print(USAGE_PREDICT_DL)
        return
    else:
        DL(options.path).DeepLearning_f(options.input, options.split)

   
    
def main():
    if len(sys.argv) < 2:
        print(USAGE_STR)
        return
    if sys.argv[1] == "preprocess": 
        preprocess_f()
    elif sys.argv[1] == "predict_LR":
        predict_LR()
    elif sys.argv[1] == "predict_RF":
        predict_RF()
    elif sys.argv[1] == "predict_GB":
        predict_GB()
    elif sys.argv[1] == "predict_DL":
        predict_DL()
    else:
        print(USAGE_STR)
        return
    


if __name__ == '__main__':
    main()
   