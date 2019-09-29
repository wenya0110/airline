# -*-coding:utf-8-*-
from openpyxl import *
import pandas as pd
import xlrd
data = pd.read_csv("t5.csv")
data.head()

data.describe()



import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
scatter_matrix(data.iloc[:,:],figsize=(14,12))
plt.show()



# 划分因变量和自变量
X = data.loc[:,data.columns!='unexpected']
y = data.loc[:,data.columns=='unexpected']
# 划分训练集和测试集
from sklearn.model_selection import train_test_split
X_tr,X_ts,y_tr,y_ts = train_test_split(X,y,test_size=0.33,random_state=2)
X_tr.shape,X_ts.shape

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_tr,y_tr.values.ravel())



y_pred = gnb.predict(X_ts)

from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score

f1_score(y_ts,y_pred)


scores = cross_val_score(gnb,X,y.values.ravel(),cv=5,scoring='f1')
print('5 fold cross validation f1-score: %.4f'%scores.mean())


y_tr_pred_prob = gnb.predict_proba(X_tr)
y_tr_pred_prob = [y for x,y in y_tr_pred_prob]


import numpy as np
from sklearn.metrics import roc_curve,roc_auc_score

fpr, tpr, thresh = roc_curve(y_tr, y_tr_pred_prob)

df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
idx = np.argmax(tpr-fpr)
Thresh = thresh[idx]
myAUC = roc_auc_score(y_tr, y_tr_pred_prob)



plt.figure(figsize=(8,6))
plt.plot(fpr,tpr)

plt.scatter(fpr[idx],tpr[idx],c='r')
plt.text(fpr[idx],tpr[idx],'(FPR %.4f,\n TPR %.4f,\n Thresh %.4f,\n AUC %.4f)'%(fpr[idx],tpr[idx],Thresh,myAUC),va='top')

plt.title('ROC curve')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.grid(True)


y_ts_pred_prob = gnb.predict_proba(X_ts)
y_ts_pred = (y_ts_pred_prob[:,1]>Thresh) *1
print y_ts_pred

print 'ROC predictede: '
print f1_score(y_ts,y_ts_pred)
data=xlrd.open_workbook('d.xls')
sh=data.sheets()[0]
#aa=sh.cell(row=4,column=4,value='aa')
