# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import telepot
from binance.enums import *
from binance.client import Client
import sys
import time
from datetime import date
import traceback
import math
import json
import numpy as np
import pandas as pd
from analysis_fun import *
import sqlite3

conn = sqlite3.connect('../db.sqlite3')


# local modules

bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()

# %%

c = conn.cursor()

c.execute("SELECT * FROM shop_orders")
data1 = c.fetchall()

c.execute("SELECT * FROM shop_bot")
data2 = c.fetchall()


# %%
# import sqlite3
# conn = sqlite3.connect('../db.sqlite3')
# c= conn.cursor()
# c.execute("SELECT email FROM shop_user1")
# data=c.fetchall()
# print(data[0])


# c.execute(f"SELECT email FROM shop_bot1 WHERE email='{data[4][0]}'")
# data=c.fetchall()
# data


# %%
times = time.time()-60*60

while True:
    try:
        if time.time() > times+60*60:

            positions = order_to_position(data1)
            total_trades = total_tr(positions)
            max_drawdown = Max_draw(positions)
            symbols_used = symbols_used_fun(positions)
            winning = winnings(positions)
            profits = profit(positions)

            for i in range(len(data2)):

                c.execute(
                    f"UPDATE shop_bot SET profits = {profits[i]} WHERE bot_id = {i+1};")
                c.execute(
                    f"UPDATE shop_bot SET symbols_used = '{string(symbols_used[i])}' WHERE bot_id = {i+1};")
                c.execute(
                    f"UPDATE shop_bot SET winning = {winning[i]} WHERE bot_id = {i+1};")
                c.execute(
                    f"UPDATE shop_bot SET total_trades = {total_trades[i]} WHERE bot_id = {i+1};")
                c.execute(
                    f"UPDATE shop_bot SET max_drawdown = {max_drawdown[i]} WHERE bot_id = {i+1};")

                conn.commit()

            c.execute("SELECT email FROM shop_user1")
            data = c.fetchall()

            for i in range(len(data)):
                bots_owned = []
                c.execute(
                    f"SELECT email FROM shop_bot1 WHERE email='{data[i][0]}'")
                data4 = c.fetchall()

                if len(data4) > 0:
                    bots_owned.append(0)

                c.execute(
                    f"SELECT email FROM shop_bot2 WHERE email='{data[i][0]}'")
                data4 = c.fetchall()
                if len(data4) > 0:
                    bots_owned.append(1)

                c.execute(
                    f"SELECT email FROM shop_bot3 WHERE email='{data[i][0]}'")
                data4 = c.fetchall()
                if len(data4) > 0:
                    bots_owned.append(2)

                c.execute(
                    f"SELECT email FROM shop_bot4 WHERE email='{data[i][0]}'")
                data4 = c.fetchall()
                if len(data4) > 0:
                    bots_owned.append(3)

                print(bots_owned)
                if len(bots_owned) == 0:
                    continue
            #########################################################

                c.execute("SELECT profits FROM shop_bot")
                data4 = c.fetchall()
                profit = 0
                for number in bots_owned:
                    value = float(data4[number][0])+profit
                    profit = value
                c.execute(
                    f"UPDATE shop_user1 SET profits = {profit} WHERE email = '{str(data[i][0])}';")

            ###################################################

                c.execute("SELECT winning FROM shop_bot")
                data4 = c.fetchall()

                winning = 0
                for number in bots_owned:
                    value = float(data4[number][0])+profit
                    winning = value
                winning = winning/len(bots_owned)
                c.execute(
                    f"UPDATE shop_user1 SET winning = {profit} WHERE email = '{str(data[i][0])}';")

            ##################################################
                positions = order_to_position(data1)
                symbols_used = symbols_used_fun(positions)

                dicts = []
                for i in range(len(bots_owned)):
                    dicts.append(symbols_used[bots_owned[i]])

                dic = {}
                exempt = []

                for d in dicts:
                    for k, v in d.items():

                        if k not in exempt:
                            dic[k] = []
                        dic[k].append(v)
                        exempt.append(k)

                diction = {}
                for k, v in dic.items():
                    diction[k] = sum(dic[k])
                c.execute(
                    f"UPDATE shop_user1 SET symbols_used = '{string(diction)}' WHERE email = '{str(data[i][0])}';")
            print('completed')
            # times=time.time()

    except Exception as e:
        bot.sendMessage(1039725953, str(traceback.format_exc()))


# %%
