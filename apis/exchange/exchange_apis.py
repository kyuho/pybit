# upbit api doc : https://docs.upbit.com/
# ask : 매도
# bid : 매수

import os
from dotenv import load_dotenv
from pyupbit import Upbit, WebSocketManager

from data.classes.Ticker import Ticker

load_dotenv()
access_key = os.getenv("access_key")
secret_key = os.getenv("secret_key")


def getAccountBalance():
    upbit = Upbit(access_key, secret_key)
    balance = upbit.get_balances()
    print(balance)


def getAccountBalanceOf(coin):
    upbit = Upbit(access_key, secret_key)
    balance = upbit.get_balance(coin)
    print(balance)


# 마켓별 주문 가능 정보를 확인한다.
def getChance():
    upbit = Upbit(access_key, secret_key)
    chance = upbit.get_chance("KRW-BTC")
    print(chance)


def cancel_order(order_id):
    upbit = Upbit(access_key, secret_key)
    uuid = "uuid"  # 취소하고자하는 주문의 uuid
    cancel_result = upbit.cancel_order(uuid)
    print(cancel_result)


def buy_at_price(coin, price, volume):
    # 원화 시장에 리플을 613원에 10개 매수 합니다
    # upbit.buy_limit_order("KRW-XRP", 613, 10)
    upbit = Upbit(access_key, secret_key)
    upbit.buy_limit_order(coin, price, volume)


# response
# {'uuid': '1907dcdc-2b96-4d85-9963-866f7aa220cd',
#  'side': 'bid',
#  'ord_type': 'limit',
#  'price': '613.0',
#  'state': 'wait',
#  'market': 'KRW-XRP',
#  'created_at': '2021-03-21T15:10:32+09:00',
#  'volume': '10.0',
#  'remaining_volume': '10.0',
#  'reserved_fee': '3.065',
#  'remaining_fee': '3.065',
#  'paid_fee': '0.0',
#  'locked': '6133.065',
#  'executed_volume': '0.0',
#  'trades_count': 0}

def buy_at_current_price(coin, amount_price):
    # 최우선 매도호가에 즉시 매수
    # 10000원은 수수료를 제외한 금액 (수수료가 0.05%라면 수수료를 포함한 10005원의 현금을 보유하고 있어야 합니다.)
    # upbit.buy_market_order("KRW-XRP", 10000)

    upbit = Upbit(access_key, secret_key)
    upbit.buy_market_order(coin, amount_price)


def sell_at_price(coin, price, volume):
    # 원화 시장에 리플을 600원에 20개 매도 합니다.
    # upbit.sell_limit_order("KRW-XRP", 600, 20)
    upbit = Upbit(access_key, secret_key)
    upbit.sell_limit_order(coin, price, volume)


# response
#     {'uuid': '0bcf0916-a7f5-49ed-80a9-a45e9e190cd3',
#      'side': 'ask',
#      'ord_type': 'limit',
#      'price': '600.0',
#      'state': 'wait',
#      'market': 'KRW-XRP',
#      'created_at': '2021-03-21T15:24:11+09:00',
#      'volume': '20.0',
#      'remaining_volume': '20.0',
#      'reserved_fee': '0.0',
#      'remaining_fee': '0.0',
#      'paid_fee': '0.0',
#      'locked': '20.0',
#      'executed_volume': '0.0',
#      'trades_count': 0}

def sell_at_current_price(coin, volume):
    # 리플 30개를 시장가 매도
    # 매도대금이 총 10000원이라면 수수료를 제외한 금액이 입금됩니다. (만약 수수료가 0.05%라면 9995원 받을 수 있습니다.)
    # upbit.sell_market_order("KRW-XRP", 30)

    upbit = Upbit(access_key, secret_key)
    upbit.sell_market_order(coin, volume)


# 입력한 암호화폐의 미체결 주문을 조회
def get_unmatched_orders(coin):
    upbit = Upbit(access_key, secret_key)
    upbit.get_order(coin)

    # upbit.get_order("KRW-LTC")
    # response
    # 250000원에 매도(ask) 주문한 LTC이 1개(volume)있다는 의미입니다.
    # [{'uuid': '50e184b3-9b4f-4bb0-9c03-30318e3ff10a',
    #   'side': 'ask',
    #   'ord_type': 'limit',
    #   'price': '250000.0',
    #   'state': 'wait',
    #   'market': 'KRW-LTC',
    #   'created_at': '2021-03-25T14:10:53+09:00',
    #   'volume': '1.0',
    #   'remaining_volume': '1.0',
    #   'reserved_fee': '0.0',
    #   'remaining_fee': '0.0',
    #   'paid_fee': '0.0',
    #   'locked': '1.0',
    #   'executed_volume': '0.0',
    #   'trades_count': 0}]


# 완료된 주문들을 조회
def get_matched_orders(coin):
    upbit = Upbit(access_key, secret_key)
    upbit.get_order(coin, state="done")

    # upbit.get_order("KRW-LTC", state="done")
    # [{'uuid': '0694def7-5ada-405f-b0f3-053801d5b190',
    #   'side': 'ask',
    #   'ord_type': 'market',
    #   'price': None,
    #   'state': 'done',
    #   'market': 'KRW-LTC',
    #   'created_at': '2021-03-21T14:43:40+09:00',
    #   'volume': '0.07336815',
    #   'remaining_volume': '0.0',
    #   'reserved_fee': '0.0',
    #   'remaining_fee': '0.0',
    #   'paid_fee': '8.39331636',
    #   'locked': '0.0',
    #   'executed_volume': '0.07336815',
    #   'trades_count': 1},
    #  {'uuid': '48d6d451-3db5-4357-9d5a-bfb8f417c943',
    #   'side': 'ask',
    #   'ord_type': 'limit',
    #   'price': '230000.0',
    #   'state': 'done',
    #   'market': 'KRW-LTC',
    #   'created_at': '2021-03-17T01:06:55+09:00',
    #   'volume': '0.5',
    #   'remaining_volume': '0.0',
    #   'reserved_fee': '0.0',
    #   'remaining_fee': '0.0',
    #   'paid_fee': '58.775',
    #   'locked': '0.0',
    #   'executed_volume': '0.5',
    #   'trades_count': 2}]


def get_order_info(order_uuid):
    upbit = Upbit(access_key, secret_key)
    order = upbit.get_order(order_uuid)
    print(order)

    # 지정가 매도를 실행했으며 주문은 취소(cancel) 됐음
    # order = upbit.get_order('50e184b3-9b4f-4bb0-9c03-30318e3ff10a')
    # response
    # {'uuid': '50e184b3-9b4f-4bb0-9c03-30318e3ff10a', 'side': 'ask', 'ord_type': 'limit', 'price': '250000.0',
    #  'state': 'cancel', 'market': 'KRW-LTC', 'created_at': '2021-03-25T14:10:53+09:00', 'volume': '1.0',
    #  'remaining_volume': '1.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '0.0', 'locked': '1.0',
    #  'executed_volume': '0.0', 'trades_count': 0, 'trades': []}


# 매수 / 매도 주문을 취소.
def cancel_order(order_uuid):
    upbit = Upbit(access_key, secret_key)
    upbit.cancel_order(order_uuid)

    # print(upbit.cancel_order('50e184b3-9b4f-4bb0-9c03-30318e3ff10a'))
    # {'uuid': '50e184b3-9b4f-4bb0-9c03-30318e3ff10a', 'side': 'ask', 'ord_type': 'limit', 'price': '250000.0',
    #  'state': 'wait', 'market': 'KRW-LTC', 'created_at': '2021-03-25T14:10:53+09:00', 'volume': '1.0',
    #  'remaining_volume': '1.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '0.0', 'locked': '1.0',
    #  'executed_volume': '0.0', 'trades_count': 0}







if __name__ == '__main__':
    print("hello")

    # getAccountBalanceOf("KRW")
    # getChance()

    # orderbook : 시세호가정보
    # WebSocket을 이용해서 현재가, 호가, 체결에 대한 정보를 수신합니다.
    # wm = WebSocketManager("ticker", ["KRW-BTC"])
    # ticker_data = Ticker(data)
    # wm = WebSocketManager("orderbook", ["KRW-BTC"])
    # order_book = OrderBook(data)
    wm = WebSocketManager("trade", ["KRW-BTC"])
    for i in range(10):
        data = wm.get()
        print(data)

    wm.terminate()
