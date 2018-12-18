file = open('gun_mini.csv')
info = file.read()
lines = info.splitlines()
size = len(lines)
list = []
for x in range(1, size):
    l = lines[x].split(",")
    list.append(l)
print(list)
dataset = dict()

for info in list:
    incident_id = info[0]
    date = info[1]
    state = info[2]
    city_or_county = info[3]
    address = info[4]
    n_killed = info[5]
    n_injured = info[6]
    if incident_id in dataset:
        if date in dataset[incident_id]:
            if state in dataset[incident_id][date]:
                if city_or_county in dataset[incident_id][date][state]:
                    if address in dataset[incident_id][date][state][city_or_county]:
                        dataset[incident_id][date][state][city_or_county][address]={"n_killed":n_killed, "n_injured":n_injured}
                    else:
                        dataset[incident_id][date][state][city_or_county]={address:{"n_killed":n_killed, "n_injured":n_injured}}
                else:
                    dataset[incident_id][date][state]={city_or_county:{address:{"n_killed":n_killed, "n_injured":n_injured}}}
            else:
                dataset[incident_id][date]={state:{city_or_county:{address:{"n_killed":n_killed, "n_injured":n_injured}}}}
        else:
            dataset[incident_id]={date:{state:{city_or_county:{address:{"n_killed":n_killed, "n_injured":n_injured}}}}}
    else:
        dataset={incident_id:{date:{state:{city_or_county:{address:{"n_killed":n_killed, "n_injured":n_injured}}}}}}

    print(dataset)