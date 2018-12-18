# Створити dataset та працювати з ним
file = open('orders.csv')

info = file.read()

lines = info.splitlines()

clients = []
for client in lines[1:]:
    clients.append(client.split(','))

dataset = dict()

for client in clients:
    name = client[0]
    date = client[1]
    product = client[2]
    quantity = client[3]
    price = client[4]
    if name in dataset:
        if date in dataset[name]:
            if product in dataset[name][date]:
                dataset[name][date][product]['quantity'] += quantity
                dataset[name][date][product]['price'] += price
            else:
                dataset[name][date][product] = {'quantity': quantity,
                                                'price': price}
        else:
            dataset[name][date] = {product: {'quantity': quantity,
                                             'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity,
                                          'price': price}}}


# Які продукти купляли усі покупці?
all_what_bought = {pos[2] for pos in clients}
print(dataset)

for product in all_what_bought:
    counter = 0
    for name in dataset:
        for date in dataset[name]:
            if product in dataset[name][date]:
                counter += 1
                break
    if counter == len(dataset.keys()):
        print('Everyone bought', product)




data = dict()


# Як змінювалась ціна на яблука? (графік)
import plotly
import plotly.graph_objs as go
dates = []
prices = []

n = 1
while n < len(dates):
    for i in range(len(dates)-1):
        if dates[i] > dates[i+1]:
            dates[i], dates[i+1] = dates[i+1], dates[i]
            prices[i], prices[i+1] = prices[i+1], prices[i]
    n += 1

print(dates, prices)

diagram = [go.Scatter(x=dates,
                      y=prices)]
plotly.offline.plot(diagram, filename='change_of_price.html')



for date in dataset['John']:
    if 'apple' in dataset['John'][date]:
        dates.append(date)
        quant, price = dataset['John'][date]['apple'].values()
        prices.append(float(price)/float(quant))

for date in dataset['Jane']:
    if 'apple' in dataset['Jane'][date]:
        dates.append(date)
        quant, price = dataset['Jane'][date]['apple'].values()
        prices.append(float(price)/float(quant))
