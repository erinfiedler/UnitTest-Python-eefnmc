#You should write unit tests for the five inputs from the stock visualizer challenge that enforce the following constraints.

import unittest
from stock_data_vizualizer import get_stock_symbol, get_time_series, get_date
import datetime

#class TestStockVisualizer(unittest.TestCase):

#?symbol: capitalized, 1-7 alpha character
def TestSymbolCapital(self):
#uncapitalized
    result = get_stock_symbol("IZ2BMG7IZUT81I82")
    self.assertEqual(result.upper(), symbol) #checks if results from function are uppercase

def TestSymbolLength(self):
#not 1-7
    length_result = len(get_stock_symbol("IZ2BMG7IZUT81I82"))
    self.assertLess(length_result, 8) #checks if length is >7

#?chart type: 1 numeric character, 1 or 2
def TestChartTypeChar(self):
    chart_type = get_chart_type()
    len_chart_type_input = len(chart_type)
    self.Less(len_chart_type_input, 2) #checks if length is >2

def TestChartTypeNum(self):
    chart_type = get_chart_type()
    self.assertEqual(chart_type, 1)
    self.assertEqual(chart_type, 2)

#?time series: 1 numeric character, 1 - 4
def TestTimeSerChar(self):
    time_series = get_time_series()
    len_timeseries_input = len(time_series)
    self.assertLess(len_timeseries_input, 2) #checks if length is >2
def TestTimeSerNum(self):
    time_series = get_time_series()
    self.assertEqual(time_series, 1)
    self.assertEqual(time_series, 2)
    self.assertEqual(time_series, 3)
    self.assertEqual(time_series, 4)

#?start date: date type YYYY-MM-DD
#invalid format
def TestStartDateFormat(self):
    start_d = get_date()
    start_date = datetime.strptime(start_d, "%Y-%m-%d")
    self.assertEqual(start_d, start_date)


#?end date: date type YYYY-MM-DD
#invalid format
def TestEndDateFormat(self):
    end_d = get_date()
    end_date = datetime.strptime(end_d, "%Y-%m-%d")
    self.assertEqual(end_d, end_date)


if __name__ == '__main__':
    unittest.main()
