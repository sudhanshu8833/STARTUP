import numpy as np
from datetime import datetime, time
import pandas as pd

def comparison_output(side_1,mid,side_2):
    
    if mid==">" or mid=="greater then":
        return np.where(side_1>side_2,True,False)

    elif mid=="<" or mid=="less then":
        return np.where(side_1<side_2,True,False)

    if mid==">=" or mid=="greater then equal to":
        return np.where(side_1>=side_2,True,False)

    if mid=="<=" or mid=="less then equal to":
        return np.where(side_1<=side_2,True,False)

    if mid=="=" or mid=="equal to":
        return np.where(side_1==side_2,True,False)

    if mid=="!=" or mid=="not equal to":
        return np.where(side_1!=side_2,True,False)

    if mid=="crossover":

        
        
        side_1=list(side_1)
        side_2=list(side_2)
        value=[]
        for i in range(1,len(side_1)):
            if side_1[i]>side_2[i] and side_1[i-1]<side_2[i-1]:
                value.append(True)
            else:
                value.append(False)

        value=np.reshape(value,(len(value),1))
        return value

    if mid=="crossunder":
        side_1=list(side_1)
        side_2=list(side_2)
        value=[]
        for i in range(1,len(side_1)):
            if side_1[i]<side_2[i] and side_1[i-1]>side_2[i-1]:
                value.append(True)
            else:
                value.append(False)
        value=np.reshape(value,(len(value),1))

        return value

def formula_maker(signals,formula):
    dicts={}
    for i in range(len(signals)):
        dicts['C'+str(i)]=signals[i]


    _locals = locals()
    formula=formula
    exec(
        "value=np.where(formula),True,False",globals(),_locals
    )

    return value


def comparison_output_time(df,inputs,mid):
    
    if mid==">" or mid=="greater then":

        lists=[]
        for i in range(len(df)):
            if df.index[i].time()>time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    elif mid=="<" or mid=="less then":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()<time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    if mid==">=" or mid=="greater then equal to":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()>=time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    if mid=="<=" or mid=="less then equal to":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()<=time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    if mid=="=" or mid=="equal to":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()==time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    if mid=="!=" or mid=="not equal to":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()!=time(inputs[0],inputs[1]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data

    if mid=="between":
        lists=[]
        for i in range(len(df)):
            if df.index[i].time()>=time(inputs[0],inputs[1]) and df.index[i].time()<=time(inputs[2],inputs[3]):
                lists.append(True)
            else:
                lists.append(False)
        data=pd.Series(lists).to_numpy()

        data=data.reshape(len(data),1)
        return data
