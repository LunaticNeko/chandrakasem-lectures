def discount_percent(price, percent):
    discounted_price = price * (100 - percent) / 100
    return discounted_price

def promotion(price):
    if price >= 10000:
        price = discount_percent(price, 20)
    elif price >= 5000:
        price = discount_percent(price, 15)
    elif price >= 3000:
        price = discount_percent(price, 10)
    elif price >= 1000:
        price = discount_percent(price, 5)
    return price

price = float(input())
price = promotion(price)
print(price)