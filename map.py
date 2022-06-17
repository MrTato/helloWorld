store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

store_euros = map(lambda data: (data[0], data[1] * 0.82), store)
store_dollars = map(lambda data: (data[0], data[1] / 0.82), store)

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)