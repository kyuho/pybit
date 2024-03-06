# 체결
class Trade:
    def __init__(self, data):
        self.type: str = data.get('type')    # 타입 : trade
        self.code: str = data.get('code')   # 마켓 코드 (ex. KRW-BTC)
        self.timestamp: int = data.get('timestamp') #타임스탬프 (millisecond), 1709735575318
        self.trade_date: str = data.get('trade_date')   #체결 일자(UTC 기준), yyyy-MM-dd, 2024-03-06
        self.trade_time: str = data.get('trade_time')   #체결 시각(UTC 기준), HH:mm:ss, 14:32:55
        self.trade_timestamp: int = data.get('trade_timestamp') #체결 타임스탬프 (millisecond), 1709735575293
        self.trade_price: float = data.get('trade_price') #체결 가격, 94000000.0
        self.trade_volume: float = data.get('trade_volume')#체결량, 0.00446412, 가끔..6.97e-05 로 나올때도 있음. 예외처리 필요.
        self.ask_bid: str = data.get('ask_bid')# 매수/매도 구분 , ASK : 매도, BID : 매수
        self.prev_closing_price: float = data.get('prev_closing_price')#전일 종가, 91275000.0
        self.change: str = data.get('change')#전일 대비, RISE : 상승, EVEN : 보합, FALL : 하락
        self.change_price: float = data.get('change_price')#부호 없는 전일 대비 값, 2725000.0
        self.sequential_id: int = data.get('sequential_id')#체결 번호 (Unique), 17097355752930000
        self.stream_type: str = data.get('stream_type')#스트림 타입, SNAPSHOT : 스냅샷, REALTIME : 실시간