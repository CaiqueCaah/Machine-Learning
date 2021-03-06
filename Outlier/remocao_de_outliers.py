# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:13:21 2019

@author: caiqsilv
"""

import pandas as pd

def cut_outliers(df = pd.DataFrame, column = ''):
    df.reset_index()
    
    median_pos = round(df[column].count() / 2, 0)
    q1 = df[column].sort_values().iloc[[round(median_pos / 2, 0)]]
    q3 = df[column].sort_values().iloc[[round(median_pos * 1.5, 0)]]
    iiq = q3.iloc[0] - q1.iloc[0]
    out1 = q1 - 1.5 * iiq
    out2 = q3 + 1.5 * iiq
    
    to_drop = []
    for x in range(0, df[column].count()):
        if (((df[column].iloc[x] < out1).iloc[0]) | (df[column].iloc[x] > out2.iloc[0])):
            to_drop.append(x)
    
    print('Dropped {} outliers'.format(len(to_drop)))
    df.drop(df.index[to_drop], inplace = True)

base = pd.read_csv('train_transaction_clean.csv')

base = base.drop_duplicates()

import matplotlib.pyplot as plt
plt.boxplot(base['TransactionAmt'], showfliers = True)

cut_outliers(base, 'TransactionAmt')

plt.boxplot(base['card1'], showfliers = True)
plt.boxplot(base['card2'], showfliers = True)

plt.boxplot(base['addr1'], showfliers = True)
cut_outliers(base, 'addr1')

plt.boxplot(base['addr2'], showfliers = True)
cut_outliers(base, 'addr2')



