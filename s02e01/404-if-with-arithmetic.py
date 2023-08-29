price = float(input())

# ซื้อครบ 3000 ลด 10%
if price >= 3000:
    price = price * 90 / 100
# ซื้อครบ 1000 ลด 5%
elif price >= 1000:
    price = price * 95 / 100
    
print(price)