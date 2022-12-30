# from comparison_functions import *
# from data_functions import *
# from indicator_functions import *
# from math_functions import *
# from pattern_funtions import *
# import vectorbt as vbt
# import json



# def execute(value):
#     if value=="False":
#         return value
#     _locals = locals()
    
#     # exec(
#     #     "global result; result="+value,globals(),_locals
#     # )
#     result=crossover(algo_get_RSI(algo_get_data('INFY.NS','1mo','5m'),[20,'close'],1),80)
#     print(result)
#     for i in range(len(result)):
#         for j in range(len(result[i])):
#             # Check if the value at the current index is True
#             if result[i][j]:
#                 # Print the index if the value is True
#                 print(i, j)

    
#     print(result[280][0])
#     return result






# def run(data):

#     buy_entries = execute(data['buy_cond'])
#     buy_exits = execute(data['buy_exits'])
#     sell_entries = execute(data['sell_cond'])
#     sell_exits = execute(data['sell_exits'])

#     df=algo_get_data(data['symbol'],data['period'],data['time_frame'])
#     # print(buy_entries)
#     # print(buy_exits)
#     # print(sell_entries)
#     # print(sell_exits)
#     pf = vbt.Portfolio.from_signals(
#         df['Close'],
#         entries=buy_entries,
#         exits=buy_exits,
#         short_entries=sell_entries,
#         short_exits=sell_exits,
#         # fees=data['fees'],
#         # slippage=data['slippage'],
#         # reject_prob=data['reject_prob'],
#         # lock_cash=data['lock_cash'],
#         # max_logs=data['max_logs'],
#         # upon_long_conflict=data['long_conflict'],
#         # upon_short_conflict=data['short_conflict'],
#         # upon_dir_conflict=data['direction_conflict'],
#         # upon_opposite_entry=data['opposite_conflict'],
#         # sl_stop=data['sl_stop'],
#         # sl_trail=data['sl_trail'],
#         # tp_stop=data['tp_stop']
#     )

#     print(pf.stats())

# # if __name__=="__main__":
# with open("strategy.json","r") as json_file:
#     data=json.load(json_file)
# run(data)