# 참고
# https://pyupbit.readthedocs.io/en/latest/exchange.html#api
# https://github.com/sharebook-kr/pyupbit
# https://github.com/youtube-jocoding/pyupbit-autotrade
# upbit api doc : https://docs.upbit.com/

from apis.quota.quota_apis import get_current_price

if __name__ == '__main__':
    get_current_price("KRW-BTC")
    # get_tickers("KRW")
    # apis.getMinutePrice("KRW-BTC", 3)


