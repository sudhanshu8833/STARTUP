import pandas as pd
import numpy as np
import yfinance as yf

import json
from datetime import datetime, time

# SMA Crossover with a 2% takeprofit and 1% stoploss 
import pandas as pd
import numpy as np
# create Pandas Series with default index values
# default index ranges is from 0 to len(list) - 1
# x = pd.Series(['Geeks', 'for', 'Geeks'])

# df=yf.download("INFY.NS",period="1mo",interval="5m")
# print((df.index[0].time()))
# lists=[]
# for i in range(len(df)):
#     if df.index[i].time()>time(12,1):
#         lists.append(True)

#     else:
#         lists.append(False)
# data=pd.Series(lists).to_numpy()

# data=data.reshape(len(data),1)
# print(data)
# for i in range(len(df.index)):
#     datetime1.append(df.index[i].timestamp())

# datetime2=pd.Series(datetime1).to_numpy()
# datetime2=datetime2.reshape(len(datetime2),1)

# data=np.where(datetime2>1656992700.0,True,False)

# print(data)



# def is_time_between(begin_time=time(00,1), end_time=time(23,59), check_time=None):
#     # If check time is not given, default to current UTC time
#     print(check_time)
#     check_time = check_time or datetime.now().time()
#     if begin_time < end_time:
#         return check_time >= begin_time and check_time <= end_time
#     else: # crosses midnight
#         return check_time >= begin_time or check_time <= end_time

# # Original test case from OP
# print(is_time_between(begin_time=time(8,30), end_time=time(16,30)),check_time=(df.index[0].time()))

# # Test case when range crosses midnight
# print(is_time_between(time(22,0), time(4,00)))



# formula={
#     "C1":None,
#     "operator1":"and",
#     "C5":None,
#     "operator2":"or",
#     "C4":None,
#     "operator3":"and",
#     "C7":None,
#     "operator4":"or",
#     "C8":None,
# }

# for key,value in formula.items():
#     print(key)
# print(formula['C1']['C2'])

formula={"dicts['C1']": {"operator": "&", "dicts['C2']": "None"}}
def making_formula(formula,made_string=""):

    print(formula)
    for key,value in formula.items():

        if 'C' in key:
            if value==None:
                made_string=made_string+key

            else:
                made_string=made_string+'(' + key
                made_string=made_string+' '+value['operator']+' '
                made_string=made_string+list(formula[key].keys())[1]+')'
                formulas={
                    list(formula[key].keys())[1]:list(formula[key].values())[1]
                }
                # print(formulas)
                # making_formula(formulas,made_string=made_string)

        elif 'operator' in key:
            made_string=made_string +' '+value +' '

    return made_string
print(making_formula(formula,made_string=""))

# def making_formula(formula,made_string="",i=0):

#     key=formula.keys()[i]
#     value=formula.values()[i]
#     if 'C' in key:
#         if value==None:
#             made_string=made_string+key

#         else:
#             made_string=made_string+' '+value['operator']+' '
#             making_formula(list(formula[key].values())[1],made_string=made_string)

#     if 'operator' in key:
#         made_string=made_string +' '+value +' '

#     return made_string
# for key,value in formula.items():
#     if 'C' in key:
#         if value==None:
#             made_string=made_string+key