from urllib.request import urlopen
import requests
import json
def getCovid():
    html = urlopen("http://coronavirusapi.com/getTimeSeries/CA")
    stuff = html.read()
    # print (stuff.split("\n")[-12:])
    encoding = 'utf-8'
    stuff = stuff.decode('utf-8')
    print (type(stuff))
    ls = []
    niranjan = str(stuff).replace("\\n","break").replace(",","break")
    for x in niranjan.split("break")[-4:]:
        try:
            ls.append(int(x))
        except ValueError:
            pass
    print(ls[0])
    print(ls[1])
    print(ls[2])
getCovid()

def getStatePopulation(state):
    url = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"
    res = requests.get(url)
    data = res.json()
