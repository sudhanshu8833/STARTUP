from symbol import parameters
from hypothesis import reject
import vectorbt as vbt
from binance.client import Client
import yfinance as yf
from datetime import datetime as dt
from .helpful_scripts.indicator_ import *
from .helpful_scripts.comparison_ import *
from .helpful_scripts._formula import *
from .helpful_scripts.condition_comparision import *


class run_strategy_crypto():


    def __init__(self, strategy):
        self.parameters = strategy
        self.data_frame = self.candles()

    def candles(self):
        df = yf.download(str(self.parameters['symbol']), interval=str(
            self.parameters['time_frame']), period=str(self.parameters['period']))
        return df

    def condition_indicator(self, condition_params):

        _side_1 = output(self.data_frame, condition_params['side_1']['ind_name'],
                         condition_params['side_1']['inputs'], condition_params['side_1']['output']).to_numpy()

        _side_2 = output(self.data_frame, condition_params['side_2']['ind_name'],
                         condition_params['side_2']['inputs'], condition_params['side_2']['output']).to_numpy()

        return comparison_output(_side_1, condition_params['mid'], _side_2)

    def condition_condition_based(self, condition_params):

        _side_1 = comparision_output(condition_params['side_1']).to_numpy()

        _side_2 = comparision_output(condition_params['side_2']).to_numpy()

        return comparison_output(_side_1, condition_params['mid'], _side_2)

    def condition_time(self, condition_params):
        return comparison_output_time(self.data_frame, condition_params['side_2']['inputs'], condition_params['side_2']['mid'])

    def condition(self, condition_params):
        if condition_params['type'] == 'indicator':
            signal = self.condition_indicator(condition_params)
            return signal

        elif condition_params['type'] == 'time':
            signal = self.condition_time(condition_params)
            return signal

        elif condition_params['type'] == 'condition_based':
            signal = self.condition_condition_based(condition_params)
            return signal

    def entry_condition(self, condition):

        if condition == "False":
            return False
        condition_name = []
        for i in range(1, int(condition['length'])+1):
            condition_name.append('C'+str(i))

        signals = []
        for i in range(int(condition['length'])):
            _condition = condition[condition_name[i]]

            signals.append(self.condition(_condition))
        formula = making_formula(condition['formula'], "")
        return formula_maker(signals, formula)

    def custom_indicator():
        pass

    def indicator_factory(self, inputs, parameters, output):

        ind = vbt.IndicatorFactory(
            class_name="combination",
            short_name="comb",
            input_names=["close"],
            param_names=["rsi_window", "ma_window"],
            output_names=["value"]

        )

    def run(self):

        buy_entries = self.entry_condition(self.parameters['buy_cond'])
        buy_exits = self.entry_condition(self.parameters['buy_exits'])
        sell_entries = self.entry_condition(self.parameters['sell_cond'])
        sell_exits = self.entry_condition(self.parameters['sell_exits'])

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
