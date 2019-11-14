from flask import Blueprint, render_template
from app.models import Stocks
import twstock, time

sm_blueprint = Blueprint('stock_monitor', __name__, template_folder='./templates/')

@sm_blueprint.route('/', methods=['GET'])
def stock_monitor():
	result = []
	monitored_stocks = [
		{'stock_code': '2317', 'stock_name': '鴻海', 'stock_buy_in_price': 10.0},
		{'stock_code': '0050', 'stock_name': '0050', 'stock_buy_in_price': 10.0},
		{'stock_code': '2330', 'stock_name': 'TSMC', 'stock_buy_in_price': 10.0},
		{'stock_code': '2454', 'stock_name': '聯發科', 'stock_buy_in_price': 10.0}
	]

	for _ in monitored_stocks:
		try:
			monitored_stocks_with_price = {}
			# call twstock to get stock info
			stock = twstock.realtime.get(_['stock_code'])
			
			monitored_stocks_with_price['stock_name'] = stock['info']['name']
			monitored_stocks_with_price['stock_code'] = stock['info']['code']
			monitored_stocks_with_price['stock_open_price'] = stock['realtime']['open']
			monitored_stocks_with_price['stock_latest_price'] = stock['realtime']['latest_trade_price']
			monitored_stocks_with_price['percentage'] = round((float(stock['realtime']['latest_trade_price']) - float(stock['realtime']['open']))/float(stock['realtime']['open'])*100, 3)

			stock = twstock.Stock(_['stock_code'])

			monitored_stocks_with_price['stock_price'] = ', '.join(map(str,stock.high[-5:]))
			monitored_stocks_with_price['stock_buy_in_price'] = _['stock_buy_in_price']

			result.append(monitored_stocks_with_price)

			time.sleep(3)
		except TypeError:
			print("latest_trade_price: %f", stock['realtime']['latest_trade_price'])
			print("open: %f", stock['realtime']['open'])
		except requests.exceptions.ConnectionError as e:
			print(e)

	return render_template('stock_monitor.html', stocks=result)
