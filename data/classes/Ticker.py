# 현재가.
class Ticker:
    def __init__(self, data):
        self.type: str = data.get('type')   # 타입, ticker(현재가)
        self.code: str = data.get('code')   # 마켓 코드 (ex. KRW-BTC)
        self.opening_price: float = data.get('opening_price')   #시가, 91284000.0
        self.high_price: float = data.get('high_price') # 고가, 94917000.0
        self.low_price: float = data.get('low_price')   # 저가, 88233000.0
        self.trade_price: float = data.get('trade_price')   # 현재가, 93644000.0
        self.prev_closing_price: float = data.get('prev_closing_price') # 전일 종가, 91275000.0
        self.acc_trade_price: float = data.get('acc_trade_price')   # 누적 거래대금(UTC 0시 기준), 935305192310.6866
        self.change: str = data.get('change')   # 전일 대비, RISE : 상승, EVEN : 보합, FALL : 하락
        self.change_price: float = data.get('change_price') # 부호 없는 전일 대비 값, 2369000.0
        self.signed_change_price: float = data.get('signed_change_price')   # 전일 대비 값, 2369000.0
        self.change_rate: float = data.get('change_rate')   # 부호 없는 전일 대비 등락율, 0.025954533
        self.signed_change_rate: float = data.get('signed_change_rate') # 전일 대비 등락율, 0.025954533
        self.ask_bid: str = data.get('ask_bid') # 매수/매도 구분, ASK : 매도, BID : 매수
        self.trade_volume: float = data.get('trade_volume') # 가장 최근 거래량, 0.01065
        self.acc_trade_volume: float = data.get('acc_trade_volume') #누적 거래량(UTC 0시 기준), 10176.86255028
        self.trade_date: str = data.get('trade_date')   # 최근 거래 일자(UTC), yyyyMMdd, 20240306
        self.trade_time: str = data.get('trade_time')   # 최근 거래 시각(UTC), HHmmss, 141211
        self.trade_timestamp: int = data.get('trade_timestamp') # 체결 타임스탬프 (milliseconds), 1709734331811
        self.acc_ask_volume: float = data.get('acc_ask_volume') # 누적 매도량, 4811.05477809
        self.acc_bid_volume: float = data.get('acc_bid_volume') # 누적 매수량, 5365.80777219
        self.highest_52_week_price: float = data.get('highest_52_week_price')   #52주 최고가, 97000000.0
        self.highest_52_week_date: str = data.get('highest_52_week_date')   # 52주 최고가 달성일, yyyy-MM-dd, 2024-03-05
        self.lowest_52_week_price: float = data.get('lowest_52_week_price') #52주 최저가, 26707000.0
        self.lowest_52_week_date: str = data.get('lowest_52_week_date') # 52주 최저가 달성일, yyyy-MM-dd, 2023-03-10
        self.market_state: str = data.get('market_state')   #거래상태,PREVIEW : 입금지원, ACTIVE : 거래지원가능, DELISTED : 거래지원종료
        self.is_trading_suspended: bool = data.get('is_trading_suspended')  # 거래 정지 여부, False
        self.delisting_date = data.get('delisting_date')    #거래지원 종료일
        self.market_warning: str = data.get('market_warning')   #유의 종목 여부, NONE : 해당없음, CAUTION : 투자유의
        self.timestamp:int = data.get('timestamp')  #타임스탬프 (millisecond), 1709734331843
        self.acc_trade_price_24h: float = data.get('acc_trade_price_24h')   #24시간 누적 거래대금, 1902029357551.3816
        self.acc_trade_volume_24h: float = data.get('acc_trade_volume_24h') #24시간 누적 거래량, 20679.40011082
        self.stream_type: str = data.get('stream_type')  #SNAPSHOT : 스냅샷, REALTIME : 실시간