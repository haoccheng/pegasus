import market
from flask import Flask, jsonify

app = Flask(__name__)
market = market.Market()

@app.route('/buy/<symbol>/<share>/<bid>')
def buy_request(symbol, share, bid):
  try:
    symbol = str(symbol)
    share = int(share)
    bid = float(bid)
    if share > 0 and bid > 0.0:
      orderid = market.buy_request(symbol, share, bid)
      market.match(symbol)
      return jsonify({'status':'BUY OK', 'order_id':orderid})
  except:
    return jsonify({'status':'BUY FAILED'})

@app.route('/sell/<symbol>/<share>/<ask>')
def sell_request(symbol, share, ask):
  try:
    symbol = str(symbol)
    share = int(share)
    ask = float(ask)
    if share > 0 and ask > 0.0:
      orderid = market.sell_request(symbol, share, ask)
      market.match(symbol)
      return jsonify({'status':'SELL OK', 'order_id':orderid})
  except:
    return jsonify({'status':'SELL FAILED'})

@app.route('/status/<ordernum>')
def order_status(ordernum):
  try:
    ordernum = int(ordernum)
    order = market.get_order(ordernum)
    ret = {}
    ret['status'] = 'STATUS OK'
    ret['order_id'] = order.order_id
    ret['order_type'] = order.order_type
    ret['order_symbol'] = order.symbol
    ret['order_shares'] = order.shares
    ret['order_available_shares'] = order.available_shares
    ret['order_bid_or_ask'] = order.price
    ret['order_status'] = order.status
    ret['order_clear_price'] = order.clear_price
    tran_ret = []
    for tran in order.transactions:
      tran_ret.append({'order_id':tran.order.order_id, 'order_type':tran.order.order_type, 'share':tran.share, 'price':tran.price})
    ret['transactions'] = tran_ret
    return jsonify(ret)
  except:
    return jsonify({'status':'FAILED: Order does not exist.'})

@app.route('/info/<symbol>')
def get_symbol_info(symbol):
  try:
    symbol = str(symbol)
    info = market.get_symbol_info(symbol)
    if info is None:
      return jsonify({'status':'NoTransactions'})
    else:
      (mean_price, transactions) = info
      ret = []
      for (share, price) in transactions:
        ret.append({'share':share, 'price':price})
      return jsonify({'status':'INFO OK', 'symbol':symbol, 'mean_price':mean_price, 'last10_transactions':ret})
  except:
    return jsonify({'status':'INFO FAILED'})

@app.route('/dump/<symbol>')
def dump_symbol(symbol):
  try:
    symbol = str(symbol)
    trades = market.get_symbol(symbol)
    ret = {}
    ret['status'] = 'DUMP OK'
    ret['buy_order'] = []
    ret['sell_order'] = []
    for buy_order in trades.buy_order:
      ret['buy_order'].append(buy_order.brief_str())
    for sell_order in trades.sell_order:
      ret['sell_order'].append(sell_order.brief_str())
    return jsonify(ret)
  except:
    return jsonify({'status':'DUMP FAILED'})

if __name__ == '__main__':
  app.run()
