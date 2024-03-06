import pyupbit
import pandas as pd

# 거래량이 급증하는 코인 찾기
def find_high_volume_coins():
    tickers = pyupbit.get_tickers()
    high_volume_coins = []
    for ticker in tickers:
        df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
        if df is not None:
            prev_volume = df.iloc[0]['volume']
            current_volume = df.iloc[1]['volume']
            if current_volume > 2 * prev_volume:  # 현재 거래량이 전날의 거래량보다 2배 이상 증가했을 때
                high_volume_coins.append(ticker)
    return high_volume_coins

# 단기 거래 전략 시뮬레이션
def short_term_trading_strategy(ticker):
    current_price = pyupbit.get_current_price(ticker)
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=5)  # 최근 5분 데이터
    current_volume = df['volume'].iloc[-1]
    if current_volume > 2 * df['volume'].iloc[:-1].mean():  # 현재 거래량이 최근 4분간 거래량 평균의 2배 이상일 때
        # 매수
        buy_price = current_price
        # 매도
        sell_price = buy_price + 1000  # 간단하게 가정, 매수 가격보다 1000원 오르면 매도
        return buy_price, sell_price
    else:
        return None, None

# 메인
if __name__ == "__main__":
    high_volume_coins = find_high_volume_coins()
    for coin in high_volume_coins:
        buy_price, sell_price = short_term_trading_strategy(coin)
        if buy_price and sell_price:
            print(f"코인: {coin}, 매수가격: {buy_price}, 매도가격: {sell_price}")