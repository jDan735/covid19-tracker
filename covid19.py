import requests

def getWorld(myApi=False):
    request = requests.get("https://data.nepalcorona.info/api/v1/world").json()
    if myApi:
        return {
            "countries": request["affectedCountries"],
            "population": request["population"],
            "updated": request["updated"],

            "cases": {
                "all": request["cases"],
                "new": request["todayCases"],
                "stats": request["casesPerOneMillion"]
            },

            "deaths": {
                "all": request["deaths"],
                "new": request["todayDeaths"],
                "stats": request["deathsPerOneMillion"]
            },

            "recovered": {
                "all": request["recovered"],
                "new": request["todayRecovered"],
                "stats": request["recoveredPerOneMillion"]
            },

            "active": {
                "all": request["active"],
                "new": request["todayCases"],
                "stats": request["activePerOneMillion"],
                "critical": {
                    "all": request["critical"],
                    "new": 0,
                    "stats": request["criticalPerOneMillion"]
                }
            },

            "tests": {
                "all": request["tests"],
                "new": 0,
                "stats": request["testsPerOneMillion"]
            }
        }
    else:
        return request

def getCountries(myApi=False, moreData=True):
    request = requests.get("https://nepalcorona.info/api/v1/data/world").json()
    if myApi:
        json = []
        for key in request:
            data = {
                "updated": key["updated"],

                "cases": {
                    "all": key["totalCases"],
                    "new": key["newCases"],
                    "stats": key["casesPerOneMillion"]
                },

                "deaths": {
                    "all": key["totalDeaths"],
                    "new": key["newDeaths"],
                    "stats": key["deathsPerOneMillion"]
                },

                "recovered": {
                    "all": key["totalRecovered"],
                },

                "active": {
                    "all": key["activeCases"],
                    "new": key["newCases"],
                    "stats": 0,
                    "critical": {
                        "all": key["criticalCases"],
                        "new": 0,
                        "stats": 0
                    }
                },

                "tests": {
                    "all": key["tests"],
                    "new": 0,
                    "stats": key["testsPerOneMillion"]
                }
            }
            if request.index(key) != 0 and request.index(key) != 1:
                data["country"] = {
                    "name": key["country"],
                    "flag": key["countryInfo"]["flag"],
                    "codes": {
                        "iso2": key["countryInfo"]["iso2"],
                        "iso3": key["countryInfo"]["iso3"]
                    },
                    "location": {
                        "continent": key["continent"],
                        "lat": key["countryInfo"]["lat"],
                        "long": key["countryInfo"]["long"]
                    }
                }
                # data["recovered"]["new"] = key["newRecovered"]
                # data["recovered"]["stats"] = key["recoveredPerOneMillion"]
            json.append(data)
        return json
    else:
        return request

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--world", action="store_true")
    parser.add_argument("-c", "--country", action="store_true")
    parser.add_argument("-a", "--api", action="store_true")

    args = parser.parse_args()

    if args.world:
        print(getWorld(args.api))

    if args.country:
        print(getCountries(args.api))
