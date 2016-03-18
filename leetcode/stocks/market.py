# stock marketplace

class Order:
  def __init__(self, order_id, order_type, symbol, shares, price):
    self.order_id = order_id
    self.order_type = order_type
    self.symbol = symbol
    self.shares = shares
    self.available_shares = self.shares
    self.price = price
    self.status = 'PENDING'
    self.clear_price = None
    self.transactions = []

  def __str__(self):
    s = '==============================================\n'
    s += 'order=%d type=%s symbol=%s share=%d available_shares=%d price=%.2f status=%s clear_price=%.2f\n' % \
         (self.order_id, self.order_type, self.symbol, self.shares, self.available_shares, self.price, self.status, (-1 if self.clear_price is None else self.clear_price))
    s += 'Transactions count=%d\n' % len(self.transactions)
    for tran in self.transactions:
      s += '  order=%d share=%d price=%.2f\n' % (tran.order.order_id, tran.share, tran.price)
    return s

  def brief_str(self):
    return 'order=%d type=%s symbol=%s share=%d available_shares=%d price=%.2f status=%s clear_price=%.2f' % \
           (self.order_id, self.order_type, self.symbol, self.shares, self.available_shares, self.price, self.status, (-1 if self.clear_price is None else self.clear_price))

class Transaction:
  def __init__(self, order, share, price):
    self.order = order
    self.share = share
    self.price = price

class SymbolTrade:
  def __init__(self):
    self.buy_order = []
    self.sell_order = []
    self.complete_trade = []

class Market:
  def __init__(self):
    self.symbol_trade = {}
    self.orders = []
    self.init_symbol_trade()

  def init_symbol_trade(self):
    self.symbol_trade['IBM'] = SymbolTrade()
    self.symbol_trade['GOOG'] = SymbolTrade()
    self.symbol_trade['YHOO'] = SymbolTrade()
    self.symbol_trade['VZ'] = SymbolTrade()
    self.symbol_trade['AAPL'] = SymbolTrade()

  def buy_request(self, symbol, shares, bid):
    if symbol not in self.symbol_trade: # unknown stock symbol
      raise RuntimeError('symbol=%s not in the market' % symbol)
    new_orderid = len(self.orders)
    new_order = Order(new_orderid, 'BUY', symbol, shares, bid)
    self.symbol_trade[symbol].buy_order.append(new_order)
    self.orders.append(new_order)
    return new_orderid

  def sell_request(self, symbol, shares, ask):
    if symbol not in self.symbol_trade: # unknown stock symbol
      raise RuntimeError('symbol=%s not in the market' % symbol)
    new_orderid = len(self.orders)
    new_order = Order(new_orderid, 'SELL', symbol, shares, ask)
    self.symbol_trade[symbol].sell_order.append(new_order)
    self.orders.append(new_order)
    return new_orderid

  # run the buyer-seller match procedure.
  def match(self, symbol):
    table = self.symbol_trade[symbol]
    for buy_order in table.buy_order:
      if buy_order.status == 'EXECUTED':
        continue
      
      sell_candidates = [sell_order for sell_order in table.sell_order if sell_order.status != 'EXECUTED' and buy_order.price >= sell_order.price]
      sell_candidates = sorted(sell_candidates, key=lambda e: e.price)
      candidates = []
      remain_share = buy_order.shares
      for sell_order in sell_candidates:
        deal_share = min(sell_order.available_shares, remain_share)
        candidates.append((sell_order, deal_share))
        remain_share -= deal_share
        if remain_share == 0:
          break

      if remain_share == 0: # match, start to process the transaction.
        clear_price = max([e[0].price for e in candidates]) # maximal price among all sell orders.
        # update buy order
        buy_order.status = 'EXECUTED'
        buy_order.available_shares = 0
        buy_order.clear_price = clear_price
        buy_order.transactions = [Transaction(e[0], e[1], clear_price) for e in candidates] # (sell_order, sell_share, price)
        # update sell orders
        for (sell_order, sell_share) in candidates:
          sell_order.transactions.append(Transaction(buy_order, sell_share, clear_price))
          sell_order.available_shares -= sell_share
          if sell_order.available_shares == 0:
            sell_order.status = 'EXECUTED'
            total_share = sum([e.share for e in sell_order.transactions])
            total_price = sum([e.share*e.price for e in sell_order.transactions])
            sell_order.clear_price = total_price * 1.0 / total_share
        table.complete_trade.append(Transaction(buy_order, buy_order.shares, buy_order.clear_price))

  def get_order(self, orderid):
    if (orderid >= 0) and (orderid <= len(self.orders)-1):
      return self.orders[orderid]
    else:
      raise RuntimeError('invalid order number order=%d', orderid)

  def get_symbol_info(self, symbol):
    if symbol not in self.symbol_trade:
      raise RuntimeError('symbol=%s not in the market' % symbol)
    table = self.symbol_trade[symbol]
    if len(table.complete_trade) == 0:
      return None
    last10 = table.complete_trade[-10:]
    total_share = sum([e.share for e in last10])
    total_price = sum([e.share*e.price for e in last10])
    mean_price = total_price * 1.0 / total_share
    transactions = []
    for i in range(len(last10)-1, -1, -1):
      transactions.append((last10[i].share, last10[i].price))
    return (mean_price, transactions)

  def get_symbol(self, symbol):
    if symbol not in self.symbol_trade:
      raise RuntimeError('symbol=%s not in the market' % symbol)
    return self.symbol_trade[symbol]

def test1(): # simple.
  market = Market()
  market.buy_request('GOOG', 10, 10.0)
  market.sell_request('GOOG', 10, 10.0)
  market.match('GOOG')
  for buy in market.symbol_trade['GOOG'].buy_order:
    print buy
  for sell in market.symbol_trade['GOOG'].sell_order:
    print sell

def test2(): # sell at the maximal price among selected sell orders.
  market = Market()
  market.buy_request('GOOG', 10, 15.0)
  market.sell_request('GOOG', 3, 10.0)
  market.sell_request('GOOG', 7, 12.0)
  market.match('GOOG')
  for buy in market.symbol_trade['GOOG'].buy_order:
    print buy
  for sell in market.symbol_trade['GOOG'].sell_order:
    print sell

def test3(): # partial sell.
  market = Market()
  market.buy_request('GOOG', 10, 15.0)
  market.sell_request('GOOG', 3, 10.0)
  market.sell_request('GOOG', 8, 12.0)
  market.match('GOOG')
  for buy in market.symbol_trade['GOOG'].buy_order:
    print buy
  for sell in market.symbol_trade['GOOG'].sell_order:
    print sell

def test4(): # test the minimize at the buyer perspective.
  market = Market()
  market.buy_request('GOOG', 10, 15.0)
  market.sell_request('GOOG', 3, 10.0)
  market.sell_request('GOOG', 8, 12.0)
  market.sell_request('GOOG', 10, 2.0)
  market.match('GOOG')
  for buy in market.symbol_trade['GOOG'].buy_order:
    print buy
  for sell in market.symbol_trade['GOOG'].sell_order:
    print sell
  market.get_order(0)
  market.get_symbol_info('GOOG')

if __name__ == '__main__':
  #test1()
  #test2()
  #test3()
  test4()

