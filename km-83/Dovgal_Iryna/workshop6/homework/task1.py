import re
import plotly
import plotly.graph_objs as go

with open("/Users/iradovgal/PycharmProjects/data/data/mini_gun.csv", mode="r", encoding="utf-8")as file:
    dataset = dict()
    file.readline()

    for line in file:
        columns = line.split(",")

        date = columns[1]
        n_killed = columns[5]

        if date not in dataset:
            dataset[date] = list()

        if n_killed not in dataset[date]:
            dataset[date].append(n_killed)



print(dataset)
diagram = [go.Bar(x = list(dataset.keys()),
                  y = list(dataset.values()))]
plotly.offline.plot(diagram)

