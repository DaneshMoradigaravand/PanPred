#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:59:50 2018

@author: dm16
"""
import numpy as np
import pandas as pd
import os

class LR:
    def __init__(self, path):
        self.path=path
         
    #logistic regression
    def LogisticRegression_f(self,input_file, ratio,Cval):
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import scale
        
        feature_inp=pd.DataFrame()
        if not os.path.isfile(self.path+"/"+input_file):
            print("No input file")
            return
        else:
            print("Reading input file")
            feature_inp= pd.read_csv(self.path+"/"+input_file,index_col=0)
            print("input file is imported")
        
        print(list(range(1,feature_inp.shape[1])))
        feature_inp=feature_inp.dropna()
        
        X = feature_inp.iloc[:,list(range(1,feature_inp.shape[1]))]
        y = feature_inp.iloc[:,0]
        
        X = scale(X)
        y = y.as_matrix()
        
        X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=ratio, random_state=42)
 
        print("Performing Logistic Regression")
        
        logreg= LogisticRegression(penalty='l2',solver='lbfgs', C=Cval)
        logreg.fit(X_train,y_train)
        y_pred=logreg.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        y_test=np.asfarray(y_test,float)
        y_train=np.asfarray(y_train,float)

        report=res_conf+res_inp
        
        report=pd.DataFrame(report, index = ['TN','FP','FN','TP','PRC_S','PRC_R','RCL_S','RCL_R','FSc_S','FSc_R','Sc_S','Sc_R'])
        report.to_csv(self.path+"/"+"report_LR", sep='\t')
        
        print(logreg)
        print(report)
        print("Done!")
        return

class RF:
    def __init__(self, path):
        self.path=path   
    
    #Rnadom Forests
    def RandomForests_f(self,input_file, ratio,max_features_pr, n_estimators_pr):
        import pandas as pd
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import scale
       
        feature_inp=pd.DataFrame()
        if not os.path.isfile(self.path+"/"+input_file):
            print("No input file")
            return
        else:
            print("Reading input file")
            feature_inp= pd.read_csv(self.path+"/"+input_file,index_col=0)
            print("input file is imported")
        
        print(list(range(1,feature_inp.shape[1])))
        feature_inp=feature_inp.dropna()
        
        X = feature_inp.iloc[:,list(range(1,feature_inp.shape[1]))]
        y = feature_inp.iloc[:,0]
        
        X = scale(X)
        y = y.as_matrix()
        
        X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=ratio, random_state=42)
 
        print("Performing random Forests")
        
        rfreg= RandomForestClassifier(n_jobs=-1,max_features= max_features_pr ,n_estimators=int(n_estimators_pr), oob_score = True) 
        rfreg.fit(X_train,y_train)
        y_pred=rfreg.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        y_test=np.asfarray(y_test,float)
        y_train=np.asfarray(y_train,float)

        report=res_conf+res_inp
        
        report=pd.DataFrame(report, index = ['TN','FP','FN','TP','PRC_S','PRC_R','RCL_S','RCL_R','FSc_S','FSc_R','Sc_S','Sc_R'])
        report.to_csv(self.path+"/"+"report_RF", sep='\t')
        
        print(report)
        print("Done!")
        return
    
class GB:
    def __init__(self, path):
        self.path=path 
    
        #Rnadom Forests
    def GradientBoostingClassifier_f(self,input_file, ratio,max_features_pr, n_estimators_pr):
        import pandas as pd
        from sklearn.ensemble import GradientBoostingClassifier
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import scale
       
        feature_inp=pd.DataFrame()
        if not os.path.isfile(self.path+"/"+input_file):
            print("No input file")
            return
        else:
            print("Reading input file")
            feature_inp= pd.read_csv(self.path+"/"+input_file,index_col=0)
            print("input file is imported")
        
        feature_inp=feature_inp.dropna()
        
        X = feature_inp.iloc[:,list(range(1,feature_inp.shape[1]))]
        y = feature_inp.iloc[:,0]
        
        X = scale(X)
        y = y.as_matrix()
        
        X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=ratio, random_state=42)
 
        print("Performing gradient boositng")
        
        gbreg = GradientBoostingClassifier(random_state=10,max_features= max_features_pr,n_estimators=int(n_estimators_pr),verbose=True)
        gbreg.fit(X_train,y_train)
        y_pred=gbreg.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        y_test=np.asfarray(y_test,float)
        y_train=np.asfarray(y_train,float)

        report=res_conf+res_inp
        report=pd.DataFrame(report, index = ['TN','FP','FN','TP','PRC_S','PRC_R','RCL_S','RCL_R','FSc_S','FSc_R','Sc_S','Sc_R'])
        report.to_csv(self.path+"/"+"report_GB", sep='\t')

        print(report)
        print("Done!")
        return
    
class DL:
    def __init__(self, path):
        self.path=path
    
    def DeepLearning_f(self,input_file, ratio):
        import pandas as pd
        from sklearn.ensemble import GradientBoostingClassifier
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import scale
        from keras.layers import Dense
        from keras.models import Sequential
        from sklearn.preprocessing import scale
        from keras.utils.np_utils import to_categorical
        from keras.callbacks import EarlyStopping
        from keras.layers import Dropout
        from sklearn.preprocessing import LabelEncoder 
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
       
        feature_inp=pd.DataFrame()
        if not os.path.isfile(self.path+"/"+input_file):
            print("No input file")
            return
        else:
            print("Reading input file")
            feature_inp= pd.read_csv(self.path+"/"+input_file,index_col=0)
            print("input file is imported")
        
        feature_inp=feature_inp.dropna()
        
        X = feature_inp.iloc[:,list(range(1,feature_inp.shape[1]))]
        y = feature_inp.iloc[:,0]
        
        X = scale(X)
        y = y.as_matrix()
        
        X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=ratio, random_state=42)
        
        model=Sequential()
        model.add(Dense(600,activation='relu', input_shape=(X_train.shape[1],)))
        model.add(Dropout(0.1, input_shape=(X_train.shape[1],)))
        for i in range(1):
            model.add(Dense(400,activation='relu'))
            model.add(Dropout(0.05))
        model.add(Dense(2, activation = 'softmax'))
        model.compile(optimizer='adam', loss= 'binary_crossentropy', metrics=['accuracy'])

        early_stopping_monitor= EarlyStopping(patience=50)
        model.fit(X_train, to_categorical(y_train), validation_split = 0.2, callbacks= [early_stopping_monitor],epochs=10, batch_size=128)
        probability_true=model.predict(X_test)[:,1]
        score = model.evaluate(X_test, to_categorical(y_test))
        model.summary()

        y_pred=model.predict_classes(X_test)
        model.predict(X_test)
        y_test=np.asfarray(y_test,float)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)

        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        report=res_conf+res_inp
        
        report=pd.DataFrame(report, index = ['TN','FP','FN','TP','PRC_S','PRC_R','RCL_S','RCL_R','FSc_S','FSc_R','Sc_S','Sc_R'])
        report.to_csv(self.path+"/"+"report_DL", sep='\t')

        print(report)
        return
    