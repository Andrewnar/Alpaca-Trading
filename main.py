# Key : PKUBQJY8RDT60IH5XUKE
from enum import Enum
import threading
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca_trade_api.common import URL
from alpaca_trade_api.stream import Stream
from util import *

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

account = trading_client.get_account()
for property_name, value in account:
    print(f"\"{property_name}\": {value}")

# Setting parameters for our buy order
market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )
                
def startMonitor():
    async def trade_callback(t):
        print('trade', t)


    async def quote_callback(q):
        print('quote', q)


    # Initiate Class Instance
    stream = Stream(API_KEY,
                    SECRET_KEY,
                    base_url=BASE_URL,
                    data_feed='iex',)  # <- replace to 'sip' if you have PRO subscription

    # subscribing to event
    stream.subscribe_trades(trade_callback, 'AAPL')
    stream.subscribe_quotes(quote_callback, 'IBM')

    stream.run()

startMonitor()