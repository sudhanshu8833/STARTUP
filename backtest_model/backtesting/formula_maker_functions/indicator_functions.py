
from finta import TA


import numpy as np

'''
* Simple Moving Average 'SMA'
* Simple Moving Median 'SMM'
* Smoothed Simple Moving Average 'SSMA'
* Exponential Moving Average 'EMA'
* Double Exponential Moving Average 'DEMA'
* Triple Exponential Moving Average 'TEMA'
* Triangular Moving Average 'TRIMA'
* Triple Exponential Moving Average Oscillator 'TRIX'
* Volume Adjusted Moving Average 'VAMA'
* Kaufman Efficiency Indicator 'ER'
* Kaufman's Adaptive Moving Average 'KAMA'
* Zero Lag Exponential Moving Average 'ZLEMA'
* Weighted Moving Average 'WMA'
* Hull Moving Average 'HMA'
* Elastic Volume Moving Average 'EVWMA'
* Volume Weighted Average Price 'VWAP'
* Smoothed Moving Average 'SMMA'
* Fractal Adaptive Moving Average 'FRAMA'
* Moving Average Convergence Divergence 'MACD'
* Percentage Price Oscillator 'PPO'
* Volume-Weighted MACD 'VW_MACD'
* Elastic-Volume weighted MACD 'EV_MACD'
* Market Momentum 'MOM'
* Rate-of-Change 'ROC'
* Relative Strenght Index 'RSI'
* Inverse Fisher Transform RSI 'IFT_RSI'
* True Range 'TR'
* Average True Range 'ATR'
* Stop-and-Reverse 'SAR'
* Bollinger Bands 'BBANDS'
* Bollinger Bands Width 'BBWIDTH'
* Momentum Breakout Bands 'MOBO'
* Percent B 'PERCENT_B'
* Keltner Channels 'KC'
* Donchian Channel 'DO'
* Directional Movement Indicator 'DMI'
* Average Directional Index 'ADX'
* Pivot Points 'PIVOT'
* Fibonacci Pivot Points 'PIVOT_FIB'
* Stochastic Oscillator %K 'STOCH'
* Stochastic oscillator %D 'STOCHD'
* Stochastic RSI 'STOCHRSI'
* Williams %R 'WILLIAMS'
* Ultimate Oscillator 'UO'
* Awesome Oscillator 'AO'
* Mass Index 'MI'
* Vortex Indicator 'VORTEX'
* Know Sure Thing 'KST'
* True Strength Index 'TSI'
* Typical Price 'TP'
* Accumulation-Distribution Line 'ADL'
* Chaikin Oscillator 'CHAIKIN'
* Money Flow Index 'MFI'
* On Balance Volume 'OBV'
* Weighter OBV 'WOBV'
* Volume Zone Oscillator 'VZO'
* Price Zone Oscillator 'PZO'
* Elder's Force Index 'EFI'
* Cummulative Force Index 'CFI'
* Bull power and Bear Power 'EBBP'
* Ease of Movement 'EMV'
* Commodity Channel Index 'CCI'
* Coppock Curve 'COPP'
* Buy and Sell Pressure 'BASP'
* Normalized BASP 'BASPN'
* Chande Momentum Oscillator 'CMO'
* Chandelier Exit 'CHANDELIER'
* Qstick 'QSTICK'
* Twiggs Money Index 'TMF'
* Wave Trend Oscillator 'WTO'
* Fisher Transform 'FISH'
* Ichimoku Cloud 'ICHIMOKU'
* Adaptive Price Zone 'APZ'
* Squeeze Momentum Indicator 'SQZMI'
* Volume Price Trend 'VPT'
* Finite Volume Element 'FVE'
* Volume Flow Indicator 'VFI'
* Moving Standard deviation 'MSD'
* Schaff Trend Cycle 'STC'
* Mark Whistler's WAVE PM 'WAVEPM'
'''


def numpy_comversion(series):
    return np.reshape(series.to_numpy(),(len(series),1))

#1
def algo_get_RSI(df, inputs=[14,"close"], offset=0): 
    RSI=TA.RSI(df, period=inputs[0], column=inputs[1])

    if offset>0:
        RSI=RSI.add(offset)

    elif offset<0:
        RSI=RSI.subtract(offset)    

    return numpy_comversion(RSI)

#2

def algo_get_ADL(df,inputs=[], offset=0): 
    ADL=TA.ADL(df)

    if offset>0:
        ADL=ADL.add(offset)

    if offset<0:
        ADL=ADL.subtract(offset)    

    return numpy_comversion(ADL)


# TA.ADX

def algo_get_ADX(df, inputs=[14], offset=0): 
    ADX=TA.ADX(df, period=inputs[0])

    if offset>0:
        ADX=ADX.add(offset)

    if offset<0:
        ADX=ADX.subtract(offset)    

    return numpy_comversion(ADX)

# TA.AO

def algo_get_AO(df, inputs=[34, 5], offset=0): 
    AO=TA.AO(df, slow_period=inputs[0], fast_period=inputs[1])

    if offset>0:
        AO=AO.add(offset)

    if offset<0:
        AO=AO.subtract(offset)    

    return numpy_comversion(AO)

# TA.APZ

def algo_get_APZ(df, inputs=[21, 2], offset=0): 
    APZ=TA.APZ(df, period=inputs[0], dev_factor=inputs[1])

    if offset>0:
        APZ=APZ.add(offset)

    if offset<0:
        APZ=APZ.subtract(offset)    

    return numpy_comversion(APZ)

# TA.ATR

def algo_get_ATR(df, inputs=[14], offset=0): 
    ATR=TA.ATR(df, period=inputs[0])

    if offset>0:
        ATR=ATR.add(offset)

    if offset<0:
        ATR=ATR.subtract(offset)    

    return numpy_comversion(ATR)

# TA.BASP


def algo_get_BASP(df, inputs=[40], offset=0, output="BASP"): 
    BASP=TA.BASP(df, period=inputs[0])

    if offset>0:
        BASP=BASP[output].add(offset)

    if offset<0:
        BASP=BASP[output].subtract(offset)    

    return numpy_comversion(BASP)

# TA.BASPN
# OUPUT= Buy.     Sell.
def algo_get_BASPN(df, inputs=[40],output="Buy.", offset=0): 
    BASPN=TA.BASPN(df, period=inputs[0])

    if offset>0:
        BASPN[output]=BASPN[output].add(offset)

    if offset<0:
        BASPN[output]=BASPN[output].subtract(offset)    

    return numpy_comversion(BASPN[output])



# TA.BBANDS
def algo_get_BBANDS(df, inputs=[20, 2], offset=0, outputs="BBANDS"): 
    BBANDS=TA.BBANDS(df, period=inputs[0], std_multiplier=inputs[1])

    if offset>0:
        BBANDS=BBANDS[outputs].add(offset)

    if offset<0:
        BBANDS=BBANDS[outputs].subtract(offset)    

    return numpy_comversion(BBANDS)


# OUTPUT=BB_UPPER,BB_MIDDLE,BB_LOWER
def algo_get_MOBO(df, inputs=[10, .8,"close"], offset=0, outputs="BB_MIDDLE"): 
    MOBO=TA.MOBO(df,period=inputs[0],std_multiplier=inputs[1],column=inputs[2])

    if offset>0:
        MOBO=MOBO[outputs].add(offset)

    if offset<0:
        MOBO=MOBO[outputs].subtract(offset)    

    return numpy_comversion(MOBO)


# TA.BBWIDTH

def algo_get_BBWIDTH(df, inputs=[20,"close"], offset=0): 
    BBWIDTH=TA.BBWIDTH(df, period=inputs[0], column=inputs[1])

    if offset>0:
        BBWIDTH=BBWIDTH.add(offset)

    if offset<0:
        BBWIDTH=BBWIDTH.subtract(offset)    
    return numpy_comversion(BBWIDTH)


# TA.BOP

def algo_get_BOP(df,offset=0): 
    BOP=TA.BOP(df)

    if offset>0:
        BOP=BOP.add(offset)

    if offset<0:
        BOP=BOP.subtract(offset)    

    return numpy_comversion(BOP)

# TA.CCI
def algo_get_CCI(df, inputs=[20,0.015], offset=0): 
    CCI=TA.CCI(df, period=inputs[0], constant=inputs[1])

    if offset>0:
        CCI=CCI.add(offset)

    if offset<0:
        CCI=CCI.subtract(offset)    

    return numpy_comversion(CCI)

# TA.CFI
def algo_get_CFI(df,inputs=["close"],offset=0): 
    CFI=TA.CFI(df,column=inputs[0])

    if offset>0:
        CFI=CFI.add(offset)

    if offset<0:
        CFI=CFI.subtract(offset)    

    return numpy_comversion(CFI)

# TA.CHAIKIN

def algo_get_CHAIKIN(df,inputs=[], offset=0): 
    CHAIKIN=TA.CHAIKIN(df)

    if offset>0:
        CHAIKIN=CHAIKIN.add(offset)

    if offset<0:
        CHAIKIN=CHAIKIN.subtract(offset)    

    return numpy_comversion(CHAIKIN)

# TA.CHANDELIER

# OUTPUT=Short.       Long.
def algo_get_CHANDELIER(df, inputs=[22, 22, 3],output="Long.", offset=0): 
    CHANDELIER=TA.CHANDELIER(df, short_period=inputs[0], long_period=inputs[1], k=inputs[2])

    if offset>0:
        CHANDELIER[output]=CHANDELIER[output].add(offset)

    if offset<0:
        CHANDELIER[output]=CHANDELIER[output].subtract(offset)    

    return numpy_comversion(CHANDELIER[output])

# TA.CMO


def algo_get_CMO(df, inputs=[9, 100], offset=0): 
    CMO=TA.CMO(df, period=inputs[0], factor=inputs[1])

    if offset>0:
        CMO=CMO.add(offset)

    if offset<0:
        CMO=CMO.subtract(offset)    

    return numpy_comversion(CMO)

# TA.COPP

def algo_get_COPP(df,inputs=[], offset=0): 
    COPP=TA.COPP(df)

    if offset>0:
        COPP=COPP.add(offset)

    if offset<0:
        COPP=COPP.subtract(offset)    

    return numpy_comversion(COPP)

# TA.DEMA

def algo_get_DEMA(df, inputs=[9,"close"], offset=0): 
    DEMA=TA.DEMA(df, period=inputs[0],column=inputs[1])

    if offset>0:
        DEMA=DEMA.add(offset)

    if offset<0:
        DEMA=DEMA.subtract(offset)    

    return numpy_comversion(DEMA)

# TA.DO
# OUTPUT=LOWER      MIDDLE       UPPER
def algo_get_DO(df, inputs=[20, 5], offset=0,output="MIDDLE"): 
    DO=TA.DO(df,upper_period=inputs[0],lower_period=inputs[1])

    if offset>0:
        DO[output]=DO[output].add(offset)

    if offset<0:
        DO[output]=DO[output].subtract(offset)    

    return numpy_comversion(DO[output])

# OUTPUT=  DI+        DI-
def algo_get_DMI(df, inputs=[20, 5], offset=0,output="DI+"): 
    DMI=TA.DMI(df, upper_period=inputs[0], lower_period=inputs[1])

    if offset>0:
        DMI[output]=DMI[output].add(offset)

    if offset<0:
        DMI[output]=DMI[output].subtract(offset)    

    return numpy_comversion(DMI[output])

# TA.DYMI
def algo_get_DYMI(df,inputs=["close"], offset=0): 
    DYMI=TA.DYMI(df,column=inputs[0])

    if offset>0:
        DYMI=DYMI.add(offset)

    if offset<0:
        DYMI=DYMI.subtract(offset)    

    return numpy_comversion(DYMI)


# OUTPUT=  Bull.     Bear.
# TA.EBBP
def algo_get_EBBP(df,inputs=[],output="Bull.", offset=0): 
    EBBP=TA.EBBP(df)

    if offset>0:
        EBBP[output]=EBBP[output].add(offset)

    if offset<0:
        EBBP[output]=EBBP[output].subtract(offset)    

    return numpy_comversion(EBBP[output])

# TA.EFI


def algo_get_EFI(df, inputs=[13,"close"], offset=0): 
    EFI=TA.EFI(df, period=inputs[0],column=inputs[1])

    if offset>0:
        EFI=EFI.add(offset)

    if offset<0:
        EFI=EFI.subtract(offset)    

    return numpy_comversion(EFI)

# TA.EMA
def algo_get_EMA(df, inputs=[9,"close"], offset=0): 
    EMA=TA.EMA(df, period=inputs[0],column=inputs[1])

    if offset>0:
        EMA=EMA.add(offset)

    if offset<0:
        EMA=EMA.subtract(offset)    

    return numpy_comversion(EMA)

# TA.EMV

def algo_get_EMV(df, inputs=[14], offset=0): 
    EMV=TA.EMV(df, period=inputs[0])

    if offset>0:
        EMV=EMV.add(offset)

    if offset<0:
        EMV=EMV.subtract(offset)    

    return numpy_comversion(EMV)

# OUTPUT=KC_UPPER    KC_LOWER
def algo_get_KC(df, inputs=[20,10,2], offset=0, output="KC_UPPER"): 
    KC=TA.KC(df,period=inputs[0],atr_period=inputs[1],kc_mult=inputs[2])

    if offset>0:
        KC[output]=KC[output].add(offset)

    if offset<0:
        KC[output]=KC[output].subtract(offset)    

    return numpy_comversion(KC[output])


# TA.EV_MACD
# output=MACD,SIGNAL
def algo_get_MACD(df, inputs=[12, 26, 9, "close"], offset=0, output="MACD"): 
    MACD=TA.MACD(df, period_fast=inputs[0], period_slow=inputs[1], signal=inputs[2], column=inputs[3])

    if offset>0:
        MACD[output]=MACD[output].add(offset)

    if offset<0:
        MACD[output]=MACD[output].subtract(offset)    

    return numpy_comversion(MACD[output])

# OUTPUT_TYPE=FALSE
def algo_get_SQZMI(df, inputs=[20], offset=0): 
    SQZMI=TA.SQZMI(df,period=inputs[0])

    if offset>0:
        SQZMI=SQZMI.add(offset)

    if offset<0:
        SQZMI=SQZMI.subtract(offset)    

    return numpy_comversion(SQZMI)

# OUTPUT=   TENKAN       KIJUN  senkou_span_a      SENKOU      CHIKOU
def algo_get_ICHIMOKU(df, inputs=[12, 26, 9, "close"], offset=0, output="CHIKOU"):
    ICHIMOKU=TA.ICHIMOKU(df,tenkan_period=inputs[0],kijun_period=inputs[1],senkou_period=inputs[2],chikou_period=inputs[3])

    if offset>0:
        ICHIMOKU[output]=ICHIMOKU[output].add(offset)

    if offset<0:
        ICHIMOKU[output]=ICHIMOKU[output].subtract(offset)    

    return numpy_comversion(ICHIMOKU[output])


# OUTPUT= WT1.       WT2.
def algo_get_WTO(df, inputs=[10,21], offset=0, output="WT1."): 
    WTO=TA.WTO(df,channel_lenght=inputs[0],average_lenght=inputs[1])

    if offset>0:
        WTO[output]=WTO[output].add(offset)

    if offset<0:
        WTO[output]=WTO[output].subtract(offset)    

    return numpy_comversion(WTO[output])

# OUTPUT=  KST    signal
def algo_get_KST(df, inputs=[10,15,20,30], offset=0, output="KST"): 
    KST=TA.KST(df,r1=inputs[0],r2=inputs[1],r3=inputs[2],r4=inputs[3])

    if offset>0:
        KST[output]=KST[output].add(offset)

    if offset<0:
        KST[output]=KST[output].subtract(offset)    

    return numpy_comversion(KST[output])


# OUTPUT=   TSI     signal
def algo_get_TSI(df, inputs=[25,13,13,"close"], offset=0, output="TSI"): 
    TSI=TA.TSI(df,long=inputs[0],short=inputs[1],signal=inputs[2],column=inputs[3])

    if offset>0:
        TSI[output]=TSI[output].add(offset)

    if offset<0:
        TSI[output]=TSI[output].subtract(offset)    

    return numpy_comversion(TSI[output])


# OUTPUT=pivot          s1          s2          s3          s4          r1          r2          r3          r4
def algo_get_PIVOT(df, inputs=[], offset=0, output="pivot"): 
    PIVOT=TA.PIVOT(df)

    if offset>0:
        PIVOT[output]=PIVOT[output].add(offset)

    if offset<0:
        PIVOT[output]=PIVOT[output].subtract(offset)    

    return numpy_comversion(PIVOT[output])

# OUTPUT=pivot          s1          s2          s3          s4          r1          r2          r3          r4
def algo_get_PIVOT_FIB(df, inputs=[], offset=0, output="pivot"): 
    PIVOT_FIB=TA.PIVOT_FIB(df)

    if offset>0:
        PIVOT_FIB[output]=PIVOT_FIB[output].add(offset)

    if offset<0:
        PIVOT_FIB[output]=PIVOT_FIB[output].subtract(offset)    

    return numpy_comversion(PIVOT_FIB[output])


# OUTPUT =MACD,SIGNAL
def algo_get_EV_MACD(df, inputs=[12, 26, 9, "close"], offset=0, output="MACD"): 
    EV_MACD=TA.EV_MACD(df, period_fast=inputs[0], period_slow=inputs[1], signal=inputs[2], column=inputs[3])

    if offset>0:
        EV_MACD[output]=EV_MACD[output].add(offset)

    if offset<0:
        EV_MACD[output]=EV_MACD[output].subtract(offset)    

    return numpy_comversion(EV_MACD[output])

# output=PPO,SIGNAL,HISTO
def algo_get_PPO(df, inputs=[12, 26, 9, "close"], offset=0, output="PPO"): 
    PPO=TA.PPO(df, period_fast=inputs[0], period_slow=inputs[1], signal=inputs[2], column=inputs[3])

    if offset>0:
        PPO[output]=PPO[output].add(offset)

    if offset<0:
        PPO[output]=PPO[output].subtract(offset)    

    return numpy_comversion(PPO[output])

# output=MACD,SIGNAL
def algo_get_VW_MACD(df, inputs=[12, 26, 9, "close"], offset=0, output="MACD"): 
    VW_MACD=TA.VW_MACD(df, period_fast=inputs[0], period_slow=inputs[1], signal=inputs[2], column=inputs[3])

    if offset>0:
        VW_MACD[output]=VW_MACD[output].add(offset)

    if offset<0:
        VW_MACD[output]=VW_MACD[output].subtract(offset)    

    return numpy_comversion(VW_MACD[output])
# TA.EVSTC

def algo_get_EVSTC(df, inputs=[12, 30, 10, 3], offset=0): 
    EVSTC=TA.EVSTC(df, period_fast=inputs[0], period_slow=inputs[1], k_period=inputs[2], d_period=inputs[3])

    if offset>0:
        EVSTC.add(offset)

    if offset<0:
        EVSTC.subtract(offset)    

    return numpy_comversion(EVSTC)

# TA.EVWMA

def algo_get_EVWMA(df, inputs=[20], offset=0): 
    EVWMA=TA.EVWMA(df, period=inputs[0])

    if offset>0:
        EVWMA=EVWMA.add(offset)

    if offset<0:
        EVWMA=EVWMA.subtract(offset)    

    return numpy_comversion(EVWMA)

# TA.FISH

def algo_get_FISH(df, inputs=[10], offset=0): 
    FISH=TA.FISH(df, period=inputs[0])

    if offset>0:
        FISH=FISH.add(offset)

    if offset<0:
        FISH=FISH.subtract(offset)    

    return numpy_comversion(FISH)

#TA.FRAMA

def algo_get_FRAMA(df, inputs=[16, 10], offset=0): 
    FRAMA=TA.FRAMA(df, period=inputs[0], batch=inputs[1])

    if offset>0:
        FRAMA=FRAMA.add(offset)

    if offset<0:
        FRAMA=FRAMA.subtract(offset)    

    return numpy_comversion(FRAMA)

#TA.FVE
def algo_get_FVE(df, inputs=[22,0.3], offset=0): 
    FVE=TA.FVE(df, period=inputs[0], factor=inputs[1])

    if offset>0:
        FVE=FVE.add(offset)

    if offset<0:
        FVE=FVE.subtract(offset)    

    return numpy_comversion(FVE)

# TA.HMA
def algo_get_HMA(df, inputs=[16], offset=0): 
    HMA=TA.HMA(df, period=inputs[0])

    if offset>0:
        HMA=HMA.add(offset)

    if offset<0:
        HMA=HMA.subtract(offset)    

    return numpy_comversion(HMA)

def algo_get_SMA(df, inputs=[41,"close"], offset=0): 
    SMA=TA.SMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        SMA=SMA.add(offset)

    if offset<0:
        SMA=SMA.subtract(offset)    

    return numpy_comversion(SMA)

def algo_get_SMM(df, inputs=[9,"close"], offset=0): 
    SMM=TA.SMM(df,period=inputs[0],column=inputs[1])

    if offset>0:
        SMM=SMM.add(offset)

    if offset<0:
        SMM=SMM.subtract(offset)    

    return numpy_comversion(SMM)

def algo_get_SMMA(df, inputs=[42,"close"], offset=0): 
    SMMA=TA.SMMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        SMMA=SMMA.add(offset)

    if offset<0:
        SMMA=SMMA.subtract(offset)    

    return numpy_comversion(SMMA)

def algo_get_SSMA(df, inputs=[9,"close"], offset=0): 
    SSMA=TA.SSMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        SSMA=SSMA.add(offset)

    if offset<0:
        SSMA=SSMA.subtract(offset)    

    return numpy_comversion(SSMA)

def algo_get_TEMA(df, inputs=[9], offset=0): 
    TEMA=TA.TEMA(df,period=inputs[0])

    if offset>0:
        TEMA=TEMA.add(offset)

    if offset<0:
        TEMA=TEMA.subtract(offset)    

    return numpy_comversion(TEMA)

def algo_get_TRIMA(df, inputs=[18], offset=0): 
    TRIMA=TA.TRIMA(df,period=inputs[0])

    if offset>0:
        TRIMA=TRIMA.add(offset)

    if offset<0:
        TRIMA=TRIMA.subtract(offset)    

    return numpy_comversion(TRIMA)

def algo_get_TRIX(df, inputs=[18,"close"], offset=0): 
    TRIX=TA.TRIX(df,period=inputs[0],column=inputs[1])

    if offset>0:
        TRIX=TRIX.add(offset)

    if offset<0:
        TRIX=TRIX.subtract(offset)    

    return numpy_comversion(TRIX)

def algo_get_VAMA(df, inputs=[8,"close"], offset=0): 
    VAMA=TA.VAMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        VAMA=VAMA.add(offset)

    if offset<0:
        VAMA=VAMA.subtract(offset)    

    return numpy_comversion(VAMA)

def algo_get_ER(df, inputs=[10,"close"], offset=0): 
    ER=TA.ER(df,period=inputs[0],column=inputs[1])

    if offset>0:
        ER=ER.add(offset)

    if offset<0:
        ER=ER.subtract(offset)    

    return numpy_comversion(ER)

def algo_get_KAMA(df, inputs=[10,2,30,20,"close"], offset=0): 
    KAMA=TA.KAMA(df,er=inputs[0],ema_fast=inputs[1],ema_slow=inputs[2],period=inputs[3],column=inputs[4])

    if offset>0:
        KAMA=KAMA.add(offset)

    if offset<0:
        KAMA=KAMA.subtract(offset)    

    return numpy_comversion(KAMA)

def algo_get_ZLEMA(df, inputs=[26,"close"], offset=0): 
    ZLEMA=TA.ZLEMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        ZLEMA=ZLEMA.add(offset)

    if offset<0:
        ZLEMA=ZLEMA.subtract(offset)    

    return numpy_comversion(ZLEMA)

def algo_get_WMA(df, inputs=[9,"close"], offset=0): 
    WMA=TA.WMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        WMA=WMA.add(offset)

    if offset<0:
        WMA=WMA.subtract(offset)    

    return numpy_comversion(WMA)

def algo_get_WMA(df, inputs=[9,"close"], offset=0): 
    WMA=TA.WMA(df,period=inputs[0],column=inputs[1])

    if offset>0:
        WMA=WMA.add(offset)

    if offset<0:
        WMA=WMA.subtract(offset)    

    return numpy_comversion(WMA)

def algo_get_VWAP(df, inputs=[], offset=0): 
    VWAP=TA.VWAP(df)

    if offset>0:
        VWAP=VWAP.add(offset)

    if offset<0:
        VWAP=VWAP.subtract(offset)    

    return numpy_comversion(VWAP)

def algo_get_MOM(df, inputs=[10,"close"], offset=0): 
    MOM=TA.MOM(df,period=inputs[0],column=inputs[1])

    if offset>0:
        MOM=MOM.add(offset)

    if offset<0:
        MOM=MOM.subtract(offset)    

    return numpy_comversion(MOM)

def algo_get_ROC(df, inputs=[12,"close"], offset=0): 
    ROC=TA.ROC(df,period=inputs[0],column=inputs[1])

    if offset>0:
        ROC=ROC.add(offset)

    if offset<0:
        ROC=ROC.subtract(offset)    

    return numpy_comversion(ROC)

def algo_get_IFT_RSI(df, inputs=[5,9,"close"], offset=0): 
    IFT_RSI=TA.IFT_RSI(df,rsi_period=inputs[0],wma_period=inputs[1],column=inputs[2])

    if offset>0:
        IFT_RSI=IFT_RSI.add(offset)

    if offset<0:
        IFT_RSI=IFT_RSI.subtract(offset)    

    return numpy_comversion(IFT_RSI)

def algo_get_TR(df, inputs=[], offset=0): 
    TR=TA.TR(df)

    if offset>0:
        TR=TR.add(offset)

    if offset<0:
        TR=TR.subtract(offset)    

    return numpy_comversion(TR)

def algo_get_SAR(df, inputs=[.02,.2], offset=0): 
    SAR=TA.SAR(df,af=inputs[0],amax=inputs[1])

    if offset>0:
        SAR=SAR.add(offset)

    if offset<0:
        SAR=SAR.subtract(offset)    

    return numpy_comversion(SAR)

def algo_get_PERCENT_B(df, inputs=[20,"close"], offset=0): 
    PERCENT_B=TA.PERCENT_B(df,period=inputs[0],column=inputs[1])

    if offset>0:
        PERCENT_B=PERCENT_B.add(offset)

    if offset<0:
        PERCENT_B=PERCENT_B.subtract(offset)    

    return numpy_comversion(PERCENT_B)

def algo_get_STOCH(df, inputs=[14], offset=0): 
    STOCH=TA.STOCH(df,period=inputs[0])

    if offset>0:
        STOCH=STOCH.add(offset)

    if offset<0:
        STOCH=STOCH.subtract(offset)    

    return numpy_comversion(STOCH)

def algo_get_STOCHD(df, inputs=[3,14], offset=0): 
    STOCHD=TA.STOCHD(df,period=inputs[0],stoch_period=inputs[1])

    if offset>0:
        STOCHD=STOCHD.add(offset)

    if offset<0:
        STOCHD=STOCHD.subtract(offset)    

    return numpy_comversion(STOCHD)

def algo_get_STOCHRSI(df, inputs=[14,14], offset=0): 
    STOCHRSI=TA.STOCHRSI(df,rsi_period=inputs[0],stoch_period=inputs[1])

    if offset>0:
        STOCHRSI=STOCHRSI.add(offset)

    if offset<0:
        STOCHRSI=STOCHRSI.subtract(offset)    

    return numpy_comversion(STOCHRSI)

def algo_get_WILLIAMS(df, inputs=[14], offset=0): 
    WILLIAMS=TA.WILLIAMS(df,period=inputs[0])

    if offset>0:
        WILLIAMS=WILLIAMS.add(offset)

    if offset<0:
        WILLIAMS=WILLIAMS.subtract(offset)    

    return numpy_comversion(WILLIAMS)

def algo_get_UO(df, inputs=["close"], offset=0): 
    UO=TA.UO(df,column=inputs[0])

    if offset>0:
        UO=UO.add(offset)

    if offset<0:
        UO=UO.subtract(offset)    

    return numpy_comversion(UO)

def algo_get_MI(df, inputs=[9], offset=0): 
    MI=TA.MI(df,period=inputs[0])

    if offset>0:
        MI=MI.add(offset)

    if offset<0:
        MI=MI.subtract(offset)    

    return numpy_comversion(MI)

def algo_get_VORTEX(df, inputs=[14], offset=0): 
    VORTEX=TA.VORTEX(df,period=inputs[0])

    if offset>0:
        VORTEX=VORTEX.add(offset)

    if offset<0:
        VORTEX=VORTEX.subtract(offset)    

    return numpy_comversion(VORTEX)

def algo_get_TP(df, inputs=[], offset=0): 
    TP=TA.TP(df)

    if offset>0:
        TP=TP.add(offset)

    if offset<0:
        TP=TP.subtract(offset)    

    return numpy_comversion(TP)

def algo_get_MFI(df, inputs=[14], offset=0): 
    MFI=TA.MFI(df,period=inputs[0])

    if offset>0:
        MFI=MFI.add(offset)

    if offset<0:
        MFI=MFI.subtract(offset)    

    return numpy_comversion(MFI)

def algo_get_OBV(df, inputs=["close"], offset=0): 
    OBV=TA.OBV(df,column=inputs[0])

    if offset>0:
        OBV=OBV.add(offset)

    if offset<0:
        OBV=OBV.subtract(offset)    

    return numpy_comversion(OBV)

def algo_get_WOBV(df, inputs=["close"], offset=0): 
    WOBV=TA.WOBV(df,column=inputs[0])

    if offset>0:
        WOBV=WOBV.add(offset)

    if offset<0:
        WOBV=WOBV.subtract(offset)    

    return numpy_comversion(WOBV)

def algo_get_VZO(df, inputs=[14,"close"], offset=0): 
    VZO=TA.VZO(df,period=inputs[0],column=inputs[1])

    if offset>0:
        VZO=VZO.add(offset)

    if offset<0:
        VZO=VZO.subtract(offset)    

    return numpy_comversion(VZO)


def algo_get_PZO(df, inputs=[14,"close"], offset=0): 
    PZO=TA.PZO(df,period=inputs[0],column=inputs[1])

    if offset>0:
        PZO=PZO.add(offset)

    if offset<0:
        PZO=PZO.subtract(offset)    

    return numpy_comversion(PZO)

def algo_get_QSTICK(df, inputs=[14], offset=0): 
    QSTICK=TA.QSTICK(df,period=inputs[0])

    if offset>0:
        QSTICK=QSTICK.add(offset)

    if offset<0:
        QSTICK=QSTICK.subtract(offset)    

    return numpy_comversion(QSTICK)

def algo_get_TMF(df, inputs=[21], offset=0): 
    TMF=TA.TMF(df,period=inputs[0])

    if offset>0:
        TMF=TMF.add(offset)

    if offset<0:
        TMF=TMF.subtract(offset)    

    return numpy_comversion(TMF)

def algo_get_VPT(df, inputs=[], offset=0): 
    VPT=TA.VPT(df)

    if offset>0:
        VPT=VPT.add(offset)

    if offset<0:
        VPT=VPT.subtract(offset)    

    return numpy_comversion(VPT)

def algo_get_VFI(df, inputs=[130,3,.2,2.5], offset=0):
    VFI=TA.VFI(df,period=inputs[0],smoothing_factor=inputs[1],factor=inputs[2],vfactor=inputs[3])

    if offset>0:
        VFI=VFI.add(offset)

    if offset<0:
        VFI=VFI.subtract(offset)    

    return numpy_comversion(VFI)

def algo_get_MSD(df, inputs=[21,"close"], offset=0): 
    MSD=TA.MSD(df,period=inputs[0],column=inputs[1])

    if offset>0:
        MSD=MSD.add(offset)

    if offset<0:
        MSD=MSD.subtract(offset)    

    return numpy_comversion(MSD)

def algo_get_STC(df, inputs=[23,50,10,3,"close"], offset=0): 
    STC=TA.STC(df,period_fast=inputs[0],period_slow=inputs[1],k_period=inputs[2],d_period=inputs[3],column=inputs[4])

    if offset>0:
        STC=STC.add(offset)

    if offset<0:
        STC=STC.subtract(offset)    

    return numpy_comversion(STC)




