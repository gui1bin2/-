# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:47:57 2018

@author: lenovo
"""

import pandas as pd
import numpy as np
import time
dc = pd.read_excel('D:/WinCode/自如数据/HS赛事预测/结果6.23.xlsx')
df = pd.read_excel('D:/WinCode/自如数据/HS赛事预测/世锦赛卡组间胜率.xlsx',sheetname='胜率处理')
lu = pd.read_excel('D:/WinCode/自如数据/HS赛事预测/小组赛lineup.xlsx')
df1 = pd.read_excel('D:/WinCode/自如数据/HS赛事预测/比赛模拟.xlsx')


df2 = df1.iloc[0:1:,][df1['A']==0]
label = df1.iloc[0:1:,]
label = label[label=='nan']
starttime = time.time()
for i in range(10000):   
    label['A']=np.array(lu[(lu['分组']=='D组')&(lu['组内序列']==2)].reset_index(drop=True)[['ID']].iloc[0,0])
    label['B']=np.array(lu[(lu['分组']=='D组')&(lu['组内序列']==3)].reset_index(drop=True)[['ID']].iloc[0,0])
    A = lu[(lu['分组']=='D组')&(lu['组内序列']==2)].reset_index(drop=True)[['卡组']]
    B = lu[(lu['分组']=='D组')&(lu['组内序列']==3)].reset_index(drop=True)[['卡组']]
    round1 = np.random.randint(1,101)
    round2 = np.random.randint(1,101)
    round3 = np.random.randint(1,101)
    round4 = np.random.randint(1,101)
    round5 = np.random.randint(1,101)
    #BP
    rollA = np.random.randint(0,A.shape[0])
    rollB = np.random.randint(0,B.shape[0])  
    label['A被ban'] = A.iloc[rollA,0]
    label['B被ban'] = B.iloc[rollB,0]
    A = A.drop(rollA).reset_index(drop=True)
    B = B.drop(rollB).reset_index(drop=True)
    #round1
    rollA = np.random.randint(0,A.shape[0])
    rollB = np.random.randint(0,B.shape[0])    
    label['AP1'] = A.iloc[rollA,0]
    label['BP1'] = B.iloc[rollB,0]
    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
    #round1 1
    if (round1<=win)==True:
        label['round1'] = '1:0'
        A = A.drop(rollA).reset_index(drop=True)
        rollA = np.random.randint(0,A.shape[0])
        rollB = np.random.randint(0,B.shape[0]) 
        label['AP2'] = A.iloc[rollA,0]
        label['BP2'] = B.iloc[rollB,0]
        win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
        #round2 11
        if (round2<=win)==True:
            label['round2'] = '2:0'
            A = A.drop(rollA).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 111 over
            if (round3<=win)==True:
                label['round3'] = '3:0'
            #round3 110
            elif (round3<=win)==False:
                label['round3'] = '2:1'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1101 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 1100
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 11001 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 11000 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
        #round2 10
        elif (round2<=win)==False:
            label['round2'] = '1:1'
            B = B.drop(rollB).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 101
            if (round3<=win)==True:
                label['round3'] = '2:1'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1011 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 1010
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 10101 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 10100 over
                    if (round5<=win)==False:
                        label['round5'] = '2:3'
            #round3 100
            elif (round3<=win)==False:
                label['round3'] = '1:2'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1001
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 10011 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 10010 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 1000 over
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
    elif (round1<=win)==False:
        label['round1'] = '0:1'
        B = B.drop(rollB).reset_index(drop=True)
        rollA = np.random.randint(0,A.shape[0])
        rollB = np.random.randint(0,B.shape[0]) 
        label['AP2'] = A.iloc[rollA,0]
        label['BP2'] = B.iloc[rollB,0]
        win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
        #round2 01
        if (round2<=win)==True:
            label['round2'] = '1:1'
            A = A.drop(rollA).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 011
            if (round3<=win)==True:
                label['round3'] = '2:1'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0111 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 0110
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 01101 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 01100 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
            #round3 010
            elif (round3<=win)==False:
                label['round3'] = '1:2'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0101
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 01011 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 01010 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 0100
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
        #round2 00
        elif (round2<=win)==False:
            label['round2'] = '0:2'
            B = B.drop(rollB).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 001
            if (round3<=win)==True:
                label['round3'] = '1:2'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0011
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 00111 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 00110 over 
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 0010 over
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
            #round3 000 over
            elif (round3<=win)==False:
                label['round3'] = '0:3'
    df2 =pd.concat([df2,label])
    label = label[label=='nan']    
df2.ix[df2.round3=='3:0','结果'] = df2['A'].drop_duplicates()+'胜'
df2.ix[df2.round3=='0:3','结果'] = df2['B'].drop_duplicates()+'胜'
df2.ix[df2.round4=='3:1','结果'] = df2['A'].drop_duplicates()+'胜'
df2.ix[df2.round4=='1:3','结果'] = df2['B'].drop_duplicates()+'胜'
df2.ix[df2.round5=='3:2','结果'] = df2['A'].drop_duplicates()+'胜'
df2.ix[df2.round5=='2:3','结果'] = df2['B'].drop_duplicates()+'胜'
df2.ix[df2.round3=='3:0','结果代码'] = '1'
df2.ix[df2.round4=='3:1','结果代码'] = '1'
df2.ix[df2.round5=='3:2','结果代码'] = '1'
df2.ix[df2.round3=='0:3','结果代码'] = '0'
df2.ix[df2.round4=='1:3','结果代码'] = '0'
df2.ix[df2.round5=='2:3','结果代码'] = '0'
g0 = df2.groupby(by=['结果'],as_index=False)['结果代码'].agg({
    '场次': np.size})      
g1 = df2.groupby(by=['A被ban','结果','结果代码'],as_index=False)['结果代码'].agg({
    '场次': np.size})  
g1 = pd.merge(g1[g1['结果代码']=='1'][['A被ban','结果','场次']],g1[g1['结果代码']=='0'][['A被ban','结果','场次']],
              left_on=['A被ban'],right_on=['A被ban'])
g1['A胜率'] = g1['场次_x']/(g1['场次_x']+g1['场次_y'])
g1 = g1[g1['A胜率']==g1['A胜率'].min()].reset_index(drop=True)[['A被ban']]
g2 = df2.groupby(by=['B被ban','结果','结果代码'],as_index=False)['结果代码'].agg({
    '场次': np.size})  
g2 = pd.merge(g2[g2['结果代码']=='1'][['B被ban','结果','场次']],g2[g2['结果代码']=='0'][['B被ban','结果','场次']],
              left_on=['B被ban'],right_on=['B被ban'])
g2['A胜率'] = g2['场次_x']/(g2['场次_x']+g2['场次_y'])
g2 = g2[g2['A胜率']==g2['A胜率'].max()].reset_index(drop=True)[['B被ban']]

df3 = df1.iloc[0:1:,][df1['A']==0]
for i in range(10000):   
    label['A']=np.array(lu[(lu['分组']=='D组')&(lu['组内序列']==2)].reset_index(drop=True)[['ID']].iloc[0,0])
    label['B']=np.array(lu[(lu['分组']=='D组')&(lu['组内序列']==3)].reset_index(drop=True)[['ID']].iloc[0,0])
    A = lu[(lu['分组']=='D组')&(lu['组内序列']==2)].reset_index(drop=True)[['卡组']]
    B = lu[(lu['分组']=='D组')&(lu['组内序列']==3)].reset_index(drop=True)[['卡组']]
    round1 = np.random.randint(1,101)
    round2 = np.random.randint(1,101)
    round3 = np.random.randint(1,101)
    round4 = np.random.randint(1,101)
    round5 = np.random.randint(1,101)
    #BP 
    label['A被ban'] = g1['A被ban']
    label['B被ban'] = g2['B被ban']
    A = pd.merge(A,g1,left_on=['卡组'],right_on=['A被ban'],how='outer')
    A = pd.DataFrame(A[A['A被ban'].isnull()==1]['卡组']).reset_index(drop=True)
    B = pd.merge(B,g2,left_on=['卡组'],right_on=['B被ban'],how='outer')
    B = pd.DataFrame(B[B['B被ban'].isnull()==1]['卡组']).reset_index(drop=True)
    #round1
    rollA = np.random.randint(0,A.shape[0])
    rollB = np.random.randint(0,B.shape[0])    
    label['AP1'] = A.iloc[rollA,0]
    label['BP1'] = B.iloc[rollB,0]
    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
    #round1 1
    if (round1<=win)==True:
        label['round1'] = '1:0'
        A = A.drop(rollA).reset_index(drop=True)
        rollA = np.random.randint(0,A.shape[0])
        rollB = np.random.randint(0,B.shape[0]) 
        label['AP2'] = A.iloc[rollA,0]
        label['BP2'] = B.iloc[rollB,0]
        win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
        #round2 11
        if (round2<=win)==True:
            label['round2'] = '2:0'
            A = A.drop(rollA).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 111 over
            if (round3<=win)==True:
                label['round3'] = '3:0'
            #round3 110
            elif (round3<=win)==False:
                label['round3'] = '2:1'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1101 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 1100
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 11001 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 11000 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
        #round2 10
        elif (round2<=win)==False:
            label['round2'] = '1:1'
            B = B.drop(rollB).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 101
            if (round3<=win)==True:
                label['round3'] = '2:1'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1011 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 1010
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 10101 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 10100 over
                    if (round5<=win)==False:
                        label['round5'] = '2:3'
            #round3 100
            elif (round3<=win)==False:
                label['round3'] = '1:2'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 1001
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 10011 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 10010 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 1000 over
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
    elif (round1<=win)==False:
        label['round1'] = '0:1'
        B = B.drop(rollB).reset_index(drop=True)
        rollA = np.random.randint(0,A.shape[0])
        rollB = np.random.randint(0,B.shape[0]) 
        label['AP2'] = A.iloc[rollA,0]
        label['BP2'] = B.iloc[rollB,0]
        win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
        #round2 01
        if (round2<=win)==True:
            label['round2'] = '1:1'
            A = A.drop(rollA).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 011
            if (round3<=win)==True:
                label['round3'] = '2:1'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0111 over
                if (round4<=win)==True:
                    label['round4'] = '3:1'
                #round4 0110
                elif (round4<=win)==False:
                    label['round4'] = '2:2'
                    B = B.drop(rollB).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 01101 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 01100 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
            #round3 010
            elif (round3<=win)==False:
                label['round3'] = '1:2'
                B = B.drop(rollB).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0101
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 01011 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 01010 over
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 0100
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
        #round2 00
        elif (round2<=win)==False:
            label['round2'] = '0:2'
            B = B.drop(rollB).reset_index(drop=True)
            rollA = np.random.randint(0,A.shape[0])
            rollB = np.random.randint(0,B.shape[0]) 
            label['AP3'] = A.iloc[rollA,0]
            label['BP3'] = B.iloc[rollB,0]
            win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
            #round3 001
            if (round3<=win)==True:
                label['round3'] = '1:2'
                A = A.drop(rollA).reset_index(drop=True)
                rollA = np.random.randint(0,A.shape[0])
                rollB = np.random.randint(0,B.shape[0]) 
                label['AP4'] = A.iloc[rollA,0]
                label['BP4'] = B.iloc[rollB,0]
                win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                #round4 0011
                if (round4<=win)==True:
                    label['round4'] = '2:2'
                    A = A.drop(rollA).reset_index(drop=True)
                    rollA = np.random.randint(0,A.shape[0])
                    rollB = np.random.randint(0,B.shape[0]) 
                    label['AP5'] = A.iloc[rollA,0]
                    label['BP5'] = B.iloc[rollB,0]
                    win = np.array(df[(df['A']==A.iloc[rollA,0])&(df['B']==B.iloc[rollB,0])][['胜率']])
                    #round5 00111 over
                    if (round5<=win)==True:
                        label['round5'] = '3:2'
                    #round5 00110 over 
                    elif (round5<=win)==False:
                        label['round5'] = '2:3'
                #round4 0010 over
                elif (round4<=win)==False:
                    label['round4'] = '1:3'
            #round3 000 over
            elif (round3<=win)==False:
                label['round3'] = '0:3'
    label.ix[label.round3=='3:0','背锅职业'] = label['BP3']     
    label.ix[label.round3=='0:3','背锅职业'] = label['AP3'] 
    label.ix[label.round4=='3:1','背锅职业'] = label['BP4']    
    label.ix[label.round4=='1:3','背锅职业'] = label['AP4'] 
    label.ix[label.round5=='3:2','背锅职业'] = label['BP5']
    label.ix[label.round5=='2:3','背锅职业'] = label['AP5']
    df3 =pd.concat([df3,label])
    label = label[label=='nan']
df3.ix[df3.round3=='3:0','结果'] = df3['A'].drop_duplicates()+'胜'
df3.ix[df3.round3=='0:3','结果'] = df3['B'].drop_duplicates()+'胜'
df3.ix[df3.round4=='3:1','结果'] = df3['A'].drop_duplicates()+'胜'
df3.ix[df3.round4=='1:3','结果'] = df3['B'].drop_duplicates()+'胜'
df3.ix[df3.round5=='3:2','结果'] = df3['A'].drop_duplicates()+'胜'
df3.ix[df3.round5=='2:3','结果'] = df3['B'].drop_duplicates()+'胜'
h = df3.groupby(by=['A被ban','B被ban','结果'],as_index=False)['结果'].agg({
    '场次': np.size})
h = pd.merge(g0,h,left_on=['结果'],right_on=['结果'])   
h.columns = ['结果','完全随机','A被ban(B的最优)','B被ban(A的最优)','最优ban场次']
bg = df3.groupby(by=['结果','背锅职业'],as_index=False)['结果'].agg({
    '背锅场次': np.size})
bg1= bg.groupby(by=['结果'],as_index=False)['背锅场次'].agg({
    '最大背锅场次': np.max})
bg = pd.merge(bg,bg1,left_on=['结果','背锅场次'],right_on=['结果','最大背锅场次'])[['结果','背锅职业','背锅场次']]
h = pd.merge(h,bg,left_on=['结果'],right_on=['结果'])


dc = pd.concat([dc,h])[['结果','完全随机','A被ban(B的最优)','B被ban(A的最优)','最优ban场次','背锅职业','背锅场次']]
print('耗时',str(round((time.time()-starttime)/60,1))+'分')

dc.to_excel('D:/WinCode/自如数据/HS赛事预测/ABCD组.xlsx',index=0)
