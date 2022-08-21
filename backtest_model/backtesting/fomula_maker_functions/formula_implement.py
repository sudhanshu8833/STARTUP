from .comparison_functions import *
from .data_functions import *
from .indicator_functions import *
from .math_functions import *
from .pattern_funtions import *
import vectorbt as vbt
import json
value="crossover(algo_get_RSI(algo_get_data('INFY.NS','1mo','5m'),[20,'close'],1)*.3,crossover(algo_get_RSI(algo_get_data('INFY.NS','1mo','5m'),[20,'close'],1)*.2,5)"


def execute(value):
    if value=="False":
        return value
    _locals = locals()
    
    exec(
        "result="+value,globals(),_locals
    )
    return result


with open("backtest_model/formula_maker_functions/strategy.json") as json_file:
    data=json.load(json_file)


def run(self):

    buy_entries = execute(data['buy_cond'])
    buy_exits = execute(data['buy_exits'])
    sell_entries = execute(data['sell_cond'])
    sell_exits = execute(data['sell_exits'])

    pf = vbt.Portfolio.from_signals(
        self.data_frame['Close'],
        entries=buy_entries,
        exits=buy_exits,
        short_entries=sell_entries,
        short_exits=sell_exits,
        fees=self.parameters['fees'],
        slippage=self.parameters['slippage'],
        reject_prob=self.parameters['reject_prob'],
        lock_cash=self.parameters['lock_cash'],
        max_logs=self.parameters['max_logs'],
        upon_long_conflict=self.parameters['long_conflict'],
        upon_short_conflict=self.parameters['short_conflict'],
        upon_dir_conflict=self.parameters['direction_conflict'],
        upon_opposite_entry=self.parameters['opposite_conflict'],
        sl_stop=self.parameters['sl_stop'],
        sl_trail=self.parameters['sl_trail'],
        tp_stop=self.parameters['tp_stop']
    )

    print(pf.stats())