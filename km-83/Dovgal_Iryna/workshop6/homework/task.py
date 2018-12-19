import re
import plotly
import plotly.graph_objs as go
from plotly import tools


# 461105
def get_incident_id(line):
    result = re.split(",", line, maxsplit=1)
    return result[0], result[1]


def get_date(line):
    result = re.split(",", line, maxsplit=2)
    return result[0], result[2]


def get_state(line):
    result = re.split(",", line, maxsplit=3)
    return result[0], result[3]


def get_n_killed(line):
    result = re.split(",", line, maxsplit=4)
    return result[0], result[4][1:]


def get_n_injured(line):
    result = re.split(",", line, maxsplit=5)
    return result[0], result[5][1:]


dataset = dict()
current_line = 0
try:
    with open("/Users/iradovgal/PycharmProjects/data/data/mini_gun.csv", mode="r", encoding="utf-8")as file:

        first = file.readline().rstrip()

        header = [column.strip().lower() for column in first.split(',')]

        data_index = header.index('date')

        for line in file:
            id, new_line = get_incident_id(line)
            date, new_line = get_date(new_line)
            state, new_line = get_state(new_line)
            n_killed, new_line = get_n_killed(new_line)
            n_injured, new_line = get_n_injured(new_line)
            # print(data_index)
            dataset[id] = {"date": date,
                           "state": state,
                           'n_killed': n_killed,
                           'n_injured': n_injured}
        print(dataset)



except IOError as io_error:
    print("error with file", io_error.errno, io_error.strerror)
except ValueError as v_error:
    print("error in line", current_line, v_error)

dates = dict()
for key in dataset:
    if dataset[key]['date'] in dates:
        dates[dataset[key]['date']] += 1
    else:
        dates[dataset[key]['date']] = 1
bar_diag = go.Bar(x=list(dates.keys()),
                  y=list(dates.values()))

cities = dict()
for key in dataset:
    if dataset[key]['n_injured'] in cities:
        cities[dataset[key]['n_injured']] += 1
    else:
        cities[dataset[key]['n_injured']] = 1
diag = go.Bar(x=list(cities.keys()),
              y=list(cities.values()))

fig = tools.make_subplots(rows=2, cols=2)

fig.append_trace(bar_diag, 1, 1)

fig.append_trace(diag, 1, 2)

plotly.offline.plot(fig)
