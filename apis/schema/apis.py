from instructor import Mode
from instructor import OpenAISchema
from pydantic import Field

class get_current_price(OpenAISchema):
    """암호화폐의 현재 값 (krw)를 리턴 한다.
한번에 최대 100개까지 쿼리 가능
* example - KRW-BTC의 가격을 가져온다
get_current_price(KRW-BTC)
response :
94257000.0

"""
    coin_name : str = Field(..., description="암호화폐 이름. e.g. KRW-BTC")

class get_tickers(OpenAISchema):
    """구매 가능한 모든 암호화폐의 목록을 얻어온다.
* example
get_tickers("krw")
response :
['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLYX', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-HIFI', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT', 'KRW-MOC', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT', 'KRW-PDA', 'KRW-DOT', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META', 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HPO', 'KRW-DOGE', 'KRW-STRIKE', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO', 'KRW-NEAR', 'KRW-AVAX', 'KRW-T', 'KRW-CELO', 'KRW-GMT', 'KRW-APT', 'KRW-SHIB', 'KRW-MASK', 'KRW-ARB', 'KRW-EGLD', 'KRW-SUI', 'KRW-GRT', 'KRW-BLUR', 'KRW-IMX', 'KRW-SEI', 'KRW-MINA', 'KRW-CTC', 'KRW-ASTR', 'KRW-ID', 'KRW-PYTH']
"""
    market_type : str = Field(..., description="should be 'KRW'")

class get_minute_price(OpenAISchema):
    """
인자로 전달되는 코인의 가격 분봉을 리턴.
1, 3, 5, 10, 15, 30, 60, 240분봉에 대해서 최대 200개 조회 가능
* example - "KRW-BTC"의 5분봉을 가져온다
get_minute_price("KRW-BTC", 5)
response :
                      open   high    low  close        volume         value
2024-03-03 07:10:00  891.6  891.6  888.9  890.0  4.926618e+05  4.384187e+08
2024-03-03 07:15:00  890.0  892.1  889.6  891.7  6.241602e+05  5.561929e+08
2024-03-03 07:20:00  891.7  893.0  891.3  892.0  6.870158e+05  6.130258e+08"""
    coin_name: str = Field(..., description="암호화폐 이름")
    mins: str = Field(..., description="1, 3, 5, 10, 15, 30, 60 are available")


def test():
    print("test")
    val = get_current_price.openai_schema
    print(val)

if __name__ == '__main__':
    # print("hello")
    # print(get_current_weather("서울"))
    test()