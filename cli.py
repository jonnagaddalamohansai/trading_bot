from bot import place_order

symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
side = input("Buy or Sell? (buy/sell): ").strip().lower()
order_type = input("Order type (market/limit): ").strip().lower()
quantity = float(input("Enter quantity: ").strip())

price = None
if order_type == "limit":
    price = float(input("Enter price: ").strip())

place_order(symbol, side, order_type, quantity, price)
