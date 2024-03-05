##
# 초당 5회, 분당 100회 연결 요청할 수 있습니다.
# 종목, 캔들, 체결, 티커, 호가 API는 분당 600회, 초당 10회 사용 가능합니다.
import pyupbit


# coin의 현재 값 (krw)를 리턴 한다.
def get_current_price(coin_name):
    price = pyupbit.get_current_price(coin_name)
    print("[Price] {name} : {price}".format(name=coin_name, price=price))


# coin 이름을 리턴 한다.
# market_type : "KRW", "BTC", "USDT"
def get_tickers(market_type):
    tickers = pyupbit.get_tickers(market_type)
    print(tickers)
    print(type(tickers))


# 분봉
# 1, 3, 5, 10, 15, 30, 60, 240분봉에 대해서 최대 200개 조회 가능
def getMinutePrice(coin_name, mins):
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