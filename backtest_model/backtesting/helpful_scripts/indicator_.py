# from appscript import k
from finta import TA
from pyparsing import col
import pandas as pd
import numpy as np



def output(df,indicator,inputs,output):

    if indicator=="time":
        np.where()

    if indicator=="VALUE":
        # value=[inputs]

        value=pd.Series(inputs, index=range(len(df)))
        # value_list=pd.Series(value_list)
        return value

    if indicator=="RSI":
        value=TA.RSI(df,inputs[0],inputs[1])

        return value
######################################################
    elif indicator=="MACD":
        value=TA.MACD(df,period_fast=inputs[0],period_slow=inputs[1],signal=inputs[2],column=inputs[3])
        if output=="macd":
            return value['MACD']

        elif output=="signal":
            return value['SIGNAL']
######################################################
    elif indicator=="BBANDS":
        value=TA.BBANDS(df,period=inputs[0],column="close")
        if output=="bb_upper":
            return value['BB_UPPER']

        elif output=="bb_middle":
            return value['BB_MIDDLE']

        elif output=="bb_lower":
            return value['BB_LOWER']
######################################################
    elif indicator=="ADX":
        value=TA.ADX(df,inputs[0])
        return value
######################################################
    elif indicator=="SMA":
        value=TA.SMA(df,period=inputs[0],column=inputs[1])
        return value
######################################################
    elif indicator=="EMA":
        value=TA.EMA(df,period=inputs[0],column=inputs[1])
        return value
######################################################
    elif indicator=="ATR":
        value=TA.ATR(df,period=inputs[0])
        return value

    elif indicator=="OBV":
        value=TA.OBV(df,period=inputs[0])
        return value

    elif indicator=="STOCHRSI":
        value=TA.STOCHRSI(df,rsi_period=inputs[0],stoch_period=inputs[1])
        return value


    elif indicator=="SMM":
        value=TA.SMM(df,period=inputs[0],column=inputs[1])
        return value

    elif indicator=="ADL":
        value=TA.ADL(df)
        return value

    elif indicator=="ALMA":
        value=TA.ALMA(df,period=inputs[0],sigma=inputs[1],offset=inputs[2])
        return value

    elif indicator=="AO":
        value=TA.AO(df,slow_period=inputs[0],fast_period=inputs[1])
        return value


    elif indicator=="APZ":
        value=TA.APZ(df,period=inputs[0],dev_factor=inputs[1],MA=df[inputs[2]])
        return value

    elif indicator=="BASP":
        value=TA.BASP(df,period=inputs[0])
        if output=="buy":
            return value['Buy.']

        if output=="sell":
            return value['Sell.']

    elif indicator=="BASPN":
        value=TA.BASPN(df,period=inputs[0])
        if output=="buy":
            return value['Buy.']

        if output=="sell":
            return value['Sell.']

    elif indicator=="BBWIDTH":
        value=TA.BBWIDTH(df,period=inputs[0],MA=df[inputs[1]],column=inputs[2])
        return value

    elif indicator=="BOP":

        value=TA.BOP(df)
        return value

    elif indicator=="CCI":
        value=TA.CCI(df,period=inputs[0],constant=inputs[1])
        return value

    elif indicator=="CFI":
        value=TA.CFI(df,column=inputs[0])
        return value

    elif indicator=="DYMI":
        value=TA.DYMI(df,column=inputs[0])
        return value

    elif indicator=="CMO":
        value=TA.CMO(df,period=inputs[0],factor=inputs[1],column=inputs[2])
        return value

    elif indicator=="CHAIKIN":
        value=TA.CHAIKIN(df)
        return value

    elif indicator=="EFI":
        value=TA.EFI(df,period=inputs[0],column=inputs[1])
        return value

    elif indicator=="CHANDELIER":
        value=TA.CHANDELIER(df,short_period=inputs[0],long_period=inputs[1],k=inputs[2])
        if output=="long":
            return value['Long.']

        if output=="short":
            return value['Short.']

    elif indicator=="DMI":
        value=TA.DMI(df,period=inputs[0])
        if output=="di+":
            return value['DI+']

        if output=="di-":
            return value['DI-']

    elif indicator=="DO":
        value=TA.DO(df,upper_period=inputs[0],lower_period=inputs[1])
        if output=="lower":
            return value['LOWER']

        elif output=="middle":
            return value['MIDDLE']

        elif output=="upper":
            return value['UPPER']

    elif indicator=="EBBP":
        value=TA.EBBP(df)
        if output=="bull":
            return value['Bull.']

        if output=="bear":
            return value['Bear.']