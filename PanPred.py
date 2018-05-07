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
from predict.MLfunctions import LogisticRegression


USAGE_STR = """Program: PanPred (Machine Learning tools to predict antibiotic resistance from NGS data)
Version: 0.1
Contact: Danesh Moradigaravand <d.morady@gmail.com>

Usage: PanPred <command> [options]

Command:
\t\t    preprocess\t    preprocess and creates the NGS input data for Machine Learning tools
\t\t    predict_LR _RF _GB _DL\t    Calls a Machine Learning model, i.e. Logistic regression, RandomForests, GradientBossting and Deep Learning, to predict resistance from input
\t\t    interpret\t    Interpret and plot the output of the prediction stage
"""

USAGE_PREPROCESS = """Preprocess and creates the NGS input data for Machine Learning tools
Usage:
PanPred preprocess [options]

Options:
        -p STR    path to csv and Rtab files (Roary output files)
        -c STR    perform clustring for features with identical frequencies
        -o STR    output file name
"""

"""Map sequencing reads to the reference for multiple sets of reads """ 
def preprocess_f():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--path", type="string", dest="path", default=os.getcwd())
    parser.add_option("-m", "--metadata", type="string", dest="metadata", default=None)
    parser.add_option("-g", "--gene", type="string", dest="gene", default=5)
    parser.add_option("-s", "--structure", type="string", dest="structure", default=5)
    (options, args) = parser.parse_args()
    
    if options.cluster == None  or options.memory == 5:
        print(USAGE_PREPROCESS)
        return
    else:
        #prep_mod.print_out(options.path,options.cluster,options.memory)
        prep_mod(options.path).train_test_split()



USAGE_PREDICT_LR = """Calls a Machine Learning modelLogistic regression
Usage:
PanPred predict [options]

Options:
        -m STR    model to choose 
""" 

def predict_LR():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-p", "--penalty", type="float", dest="Cval", default=0.0)
    (options, args) = parser.parse_args()
    print(options.Cval)
    if options.Cval == None  or not isinstance(options.Cval, float):
        print(USAGE_PREDICT_LR)
        return
    else:
        LogisticRegression.LogisticRegression_f(options.Cval)

USAGE_PREDICT_RF = """Calls a Machine Learning model RandomForests
Usage:
PanPred predict [options]

Options:
        -m STR    model to choose 
""" 

def predict_RF():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-m", "--model", type="choice", dest="model",choices=("LR","RF","GB","DL"), default="MN",help = "Method to use. Valid choices are %(choices)s. Default: %(default)s")
    parser.add_option("-i", "--input", type="choice", dest="input",choices=("YGS","-GS"), default="YGS")
    (options, args) = parser.parse_args()
    print(options.model)


USAGE_PREDICT_GB = """Calls a Machine Learning model GradientBossting 
Usage:
PanPred predict [options]

Options:
        -m STR    model to choose 
""" 

def predict_GB():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-m", "--model", type="choice", dest="model",choices=("LR","RF","GB","DL"), default="MN",help = "Method to use. Valid choices are %(choices)s. Default: %(default)s")
    parser.add_option("-i", "--input", type="choice", dest="input",choices=("YGS","-GS"), default="YGS")
    (options, args) = parser.parse_args()
    print(options.model)

USAGE_PREDICT_DL = """Calls a Machine Learning model Deep Learning
Usage:
PanPred predict [options]

Options:
        -m STR    model to choose 
""" 

def predict_DL():
    parser = OptionParser(usage=USAGE_PREPROCESS)
    parser.add_option("-m", "--model", type="choice", dest="model",choices=("LR","RF","GB","DL"), default="MN",help = "Method to use. Valid choices are %(choices)s. Default: %(default)s")
    parser.add_option("-i", "--input", type="choice", dest="input",choices=("YGS","-GS"), default="YGS")
    (options, args) = parser.parse_args()
    print(options.model)

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
   