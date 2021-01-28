# while

item = 0
money = 21
cost = 3

while money >= cost:  # <==== do you want to use ">" or ">="
    money = money - cost
    item = item + 1
    print("Items", item, "Money", money)

print("----- Results -----")
print("Items carried", item)
print("Money remaining", money)
