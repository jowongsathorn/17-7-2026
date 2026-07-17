coin = 0
store = int(input("กี่ร้าน"))
while store > 0:
    money = int(input("เท่าไร"))
    coin += money
    store -= 1
print(coin)

