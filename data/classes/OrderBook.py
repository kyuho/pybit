from data.classes.OrderBookUnit import OrderBookUnit


class OrderBook:
    def __init__(self, data):
        self.type: str = data.get('type')  # 타입.  e.g."orderbook"
        self.code: str = data.get('code')  # 마켓 코드. e.g."KRW-BTC"
        self.timestamp: int = data.get('timestamp')  # 호가 생성 시각, 1709733815103
        self.total_ask_size: float = data.get('total_ask_size') # 호가 매도 총 잔량, 2.25490176
        self.total_bid_size: float = data.get('total_bid_size') # 호가 매수 총 잔량, 5.6728971
        self.orderbook_units: [OrderBookUnit] = [OrderBookUnit(unit['ask_price'], unit['bid_price'], unit['ask_size'], unit['bid_size'])
                                for unit in data.get('orderbook_units')]
        self.stream_type: float = data.get('stream_type')   # REALTIME
        self.level: float = data.get('level')
   # print(order_book.type)
        # print(order_book.code)
        # print(order_book.timestamp)
        # print(order_book.total_ask_size)
        # print(order_book.total_bid_size)
        # print([unit.__dict__ for unit in order_book.orderbook_units])
        # print(order_book.stream_type)
        # print(order_book.level)