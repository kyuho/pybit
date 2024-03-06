##
# 초당 5회, 분당 100회 연결 요청할 수 있습니다.
# 종목, 캔들, 체결, 티커, 호가 API는 분당 600회, 초당 10회 사용 가능합니다.
import pyupbit




# coin의 현재 값 (krw)를 리턴 한다.
# 한번에 최대 100개까지 쿼리 가능
def get_current_price(coin_name):
    price = pyupbit.get_current_price(coin_name)
    print("{price}".format(name=coin_name, price=price))


# 업비트가 지원하는 모든 암호화폐 목록을 얻어옵니다.
# market_type : "KRW", "BTC", "USDT"
def get_tickers(market_type):
    tickers = pyupbit.get_tickers(market_type)
    print(tickers)


# 분봉
# 1, 3, 5, 10, 15, 30, 60, 240분봉에 대해서 최대 200개 조회 가능
def get_minute_price(coin_name, mins):
    scale = "minute1"
    if mins == 1:
        scale = "minute1"
    elif mins == 3:
        scale = "minute3"
    elif mins == 5:
        scale = "minute5"
    elif mins == 10:
        scale = "minute10"
    elif mins == 30:
        scale = "minute30"
    elif mins == 60:
        scale = "minute60"

    res = pyupbit.get_ohlcv(coin_name, scale)

    print(res)
    return res


def get_daily_price(coin_name):
    # 기본 요청시 200일 (최대)
    df = pyupbit.get_ohlcv(coin_name, "day")
    print(df)

    # # 200개 미만의 경우 count 인자에 설정 가능
    # df = pyupbit.get_ohlcv("KRW-BTC", "day", count=10)
    # print(df)

def get_weekly_price(coin_name):
    # 기본 요청시 200개
    df = pyupbit.get_ohlcv(coin_name, "week")
    print(df)

def get_monthly_price(coin_name):
    df = pyupbit.get_ohlcv(coin_name, "month")
    print(df)

# 매수/매도 호가 정보를 조회합니다.
def get_order_book(coin_name):
    df = pyupbit.get_orderbook(ticker=coin_name)
    print(df)

# ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLYX', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-HIFI', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT', 'KRW-MOC', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT', 'KRW-PDA', 'KRW-DOT', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META', 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HPO', 'KRW-DOGE', 'KRW-STRIKE', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO', 'KRW-NEAR', 'KRW-AVAX', 'KRW-T', 'KRW-CELO', 'KRW-GMT', 'KRW-APT', 'KRW-SHIB', 'KRW-MASK', 'KRW-ARB', 'KRW-EGLD', 'KRW-SUI', 'KRW-GRT', 'KRW-BLUR', 'KRW-IMX', 'KRW-SEI', 'KRW-MINA', 'KRW-CTC', 'KRW-ASTR', 'KRW-ID', 'KRW-PYTH']

if __name__ == '__main__':
    print("hello")
    # get_current_price(["KRW-BTC", "KRW-XRP"])
    # get_tickers("KRW")
    # get_current_price("KRW-BTC")
    get_minute_price("KRW-DOGE", 5)
    # get_order_book("KRW-BTC")
    # get_order_book(["KRW-BTC", "KRW-XRP"])