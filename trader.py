import backtrader as bt
import datetime
from strategies import TestStrategy

# https://www.backtrader.com/docu/quickstart/quickstart/

cerebro = bt.Cerebro()

cerebro.broker.setcash(10000.0)

data = bt.feeds.YahooFinanceCSVData(
    dataname="2015-2020_AAPL.csv",
    # Do not pass values before this date
    fromdate=datetime.datetime(2015, 10, 13),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 10, 13),
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake=100)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
