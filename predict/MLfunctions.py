#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:59:50 2018

@author: dm16
"""
import numpy as np
import pandas as pd
class LogisticRegression:
    def __init__(self):
        self.X_train = pd.DataFrame()
        self.y_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.y_test = pd.DataFrame()
        self.param=[1.4]
         
    #logistic regression
    def LogisticRegression_f(X_train, y_train,X_test, y_test, Cval):
        import pandas as pd
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
    
        logreg= LogisticRegression(penalty='l2',solver='lbfgs', C=Cval)
        logreg.fit(X_train,y_train)
        y_pred=logreg.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        y_pred_prob= logreg.predict_proba(X_test)[:,1]
        y_test=np.asfarray(y_test,float)
        y_train=np.asfarray(y_train,float)
    
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
        sc=roc_auc_score(y_test,y_pred_prob)

        report=res_conf+res_inp+sc
        pd.DataFrame(report).to_csv("report_"+str(line), sep='\t')
        return logreg, report

        
class RandomForests:
    def __init__(self):
        self.X_train = pd.DataFrame()
        self.y_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.y_test = pd.DataFrame()
        self.param=[1.4]
            
    def RandomForestClassifier_f(X_train, y_train,X_test, y_test, max_features_pr, n_estimators_pr):
        import numpy as np
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix
    
        rfc = RandomForestClassifier(n_jobs=-1,max_features= max_features_pr ,n_estimators=n_estimators_pr, oob_score = True) 
        rfc.fit(X_train, y_train)
        y_pred=rfc.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        report=res_conf+res_inp
        return rfc, report
        
class GradientBoosting:
    def __init__(self):
        self.X_train = pd.DataFrame()
        self.y_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.y_test = pd.DataFrame()
        self.param=[1.4]
        
    def GradientBoostingClassifier_f(X_train, y_train,X_test, y_test, max_features_pr, n_estimators_pr):
        import numpy as np
        from sklearn.ensemble import GradientBoostingClassifier
        from sklearn.metrics import precision_recall_fscore_support
        from sklearn.utils.multiclass import unique_labels
        from sklearn.metrics import confusion_matrix

        gbm0 = GradientBoostingClassifier(random_state=10,max_features= max_features_pr,n_estimators=n_estimators_pr,verbose=True)
        fitted_gbm=gbm0.fit(X_train, y_train)
        y_pred = fitted_gbm.predict(X_test)
        conf=confusion_matrix(y_test,y_pred , sample_weight=None)
        labels = unique_labels(y_test, y_pred)
        inp= precision_recall_fscore_support(y_test, y_pred, labels=labels, average=None)
        res_conf=conf.ravel().tolist()
        res_inp=np.asarray(inp).ravel().tolist()
        report=res_conf+res_inp
        return fitted_gbm, report
    
    def plot_train_test(fitted_gbm,X_test,y_test):
        import matplotlib.pyplot as plt
        n_est=600
        test_score = np.zeros((n_est,), dtype=np.float64)
        for i, y_pred in enumerate(fitted_gbm.staged_predict(X_test)):
            test_score[i] = fitted_gbm.loss_(y_test, y_pred)

        plt.figure(figsize=(12, 6))
        plt.title('Deviance')
        plt.plot(np.arange(n_est) + 1, fitted_gbm.train_score_, 'b-', label='Training Set Deviance')
        plt.plot(np.arange(n_est) + 1, test_score, 'r-', label='Test Set Deviance')
        plt.legend(loc='upper right')
        plt.xlabel('Boosting Iterations')
        plt.ylabel('Deviance')
    
    
    def plot_important_features(fitted_gbm, num_feat, feat_nam):
        import numpy as np
        import matplotlib.pyplot as plt
        feature_importance = fitted_gbm.feature_importances_
        feature_importance = 100.0 * (feature_importance / feature_importance.max())
        sorted_idx = np.argsort(feature_importance)
        sorted_idx = sorted_idx[len(feature_importance)-num_feat:]
        pos = np.arange(sorted_idx.shape[0]) + .5
        plt.subplot(1, 2, 2)
        plt.barh(pos, feature_importance[sorted_idx], align='center')
        plt.yticks(pos, np.array(feat_nam)[sorted_idx])
        plt.xlabel('Relative Importance')
        plt.title('Variable Importance')
        plt.show()

    def plot_gbm_tree(path, fitted_gbm, tree_id, col_lab): 
        import collections
        import pydotplus
        from sklearn import tree

        tree_tmp = fitted_gbm.estimators_[tree_id, 0]
        dot_data = tree.export_graphviz(tree_tmp,out_file=None,filled=True,rounded=True)

        lab=list(map(lambda x: "X["+str(x)+"]", np.arange(X.shape[1])))
        dict_lab = {}
        for i in range(len(lab)):
            dict_lab[lab[i]] = col_lab[i]

        hold=dot_data
        for key, value in dict_lab.items():
            hold=str.replace(hold, key,value)

        graph = pydotplus.graph_from_dot_data(hold)
        colors = ('turquoise', 'orange')
        edges = collections.defaultdict(list)
 
        for edge in graph.get_edge_list():
            edges[edge.get_source()].append(int(edge.get_destination()))
 
        for edge in edges:
            edges[edge].sort()    
            for i in range(2):
                dest = graph.get_node(str(edges[edge][i]))[0]
                dest.set_fillcolor(colors[i])
        graph.write_png(path + '/tree_'+str(tree_id)+ '.jpg')
        
class DeepLearning:
    def __init__(self):
        self.X_train = pd.DataFrame()
        self.y_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.y_test = pd.DataFrame()
        self.param=[1.4]
        
    def DeepLearning_f(b,c,a):
        
        
        
        
def DeepLearning_f(X_train, y_train,X_test, y_test):
    import numpy as np
    import pandas as pd
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
    
    return model, report
