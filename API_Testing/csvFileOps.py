import csv

with open("utilities/IPL.csv") as csvFile:
    lst = list(csv.reader(csvFile))
    print(lst)
    name = []
    team = []
    for i in lst:
        name.append(i[0])
        team.append(i[1])

    print("'Name:'{},'Team:'{}".format(name, team))

with open("utilities/IPL.csv", 'a') as csvFileWrite:
    csv.writer(csvFileWrite).writerow(['Bhuvi','SRH'])

