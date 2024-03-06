class OrderBookUnit:
    def __init__(self, ask_price, bid_price, ask_size, bid_size):
        self.ask_price: float = ask_price   # 매도 호가, 93555000.0
        self.bid_price: float = bid_price   # 매수 호가, 93422000.0
        self.ask_size: float = ask_size   # 매도 잔량, 0.26531684
        self.bid_size: float = bid_size   # 매수 잔량, 0.0495416