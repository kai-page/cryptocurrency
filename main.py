import ccxt
import requests

class BitBank_Line:
    def __init__(self):

        bitbank_api_key = 'ビットバンクAPIキー'
        bitbank_secret_key = 'ビットバンクシークレットキー'
        self.bitbank = ccxt.bitbank({'api_key': bitbank_api_key, 'secret_key': bitbank_secret_key})

        self.line_url = 'https://notify-api.line.me/api/notify'
        line_token = 'Lineトークン'
        self.line_headers = {'Authorization': 'Bearer ' + line_token}

    def get_price(self, symbol):
        result = self.bitbank.fetch_ticker(symbol=symbol)
        self.send_line(result)

    def send_line(self, result):
        btc_price = int(result['last'])
        btc_price_convert = '{:,}'.format(btc_price)
        payload = {'message': f'\n BTC価格 : {btc_price_convert}円'}
        requests.post(self.line_url, headers=self.line_headers, params=payload)


if __name__ == '__main__':
    btc = BitBank_Line()
    btc.get_price('BTC/JPY')
