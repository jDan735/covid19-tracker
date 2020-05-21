import requests
url = "https://data.nepalcorona.info/api"

def getWorld():
    return requests.get(url + "/v1/world").json()

def getCountries():
    return requests.get(url + "/v1/data/world").json()