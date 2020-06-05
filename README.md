# 🦠 COVID19 tracker
## 🧑‍💻 Installation
Download covid19.py, place in project folder and import:
```python
import sys
sys.path.insert(0, path)
import covid19
```
## 🚀 Start
To start, run this code:
```
python covid19.py
```
### ⚙️ Options
#### `world`
Print world stats in your terminal
#### `country`
Print countries stats in your terminal
#### `api`
Enable new api
## 🤖 Functions
### 🌎 getWorld
Send parsed json from https://data.nepalcorona.info/api/v1/world
#### 📥 Input
```python
covid19.getWorld()
```
#### 📤 Output
```json
{
    "updated": 1590040302542,
    "cases": 5090157,
    "todayCases": 6746,
    "deaths": 329739,
    "todayDeaths": 500,
    "recovered": 2024329,
    "active": 2736089,
    "critical": 45796,
    "casesPerOneMillion": 653,
    "deathsPerOneMillion": 42.3,
    "tests": 65816543,
    "testsPerOneMillion": 8493.37,
    "population": 7749165314,
    "activePerOneMillion": 353.08,
    "recoveredPerOneMillion": 261.23,
    "criticalPerOneMillion": 5.91,
    "affectedCountries": 215
}
```
### 🗺 getCountries
Send parsed json from https://nepalcorona.info/api/v1/data/world
#### 📥 Input
```python
covid19.getCountries()
```
#### 📤 Output
```json
[{
    "_id": "5ec618e5878b4a2adea22577",
    "country": "USA",
    "countryCode": "US",
    "totalCases": 1593039,
    "newCases": 316,
    "totalDeaths": 94941,
    "newDeaths": 5,
    "activeCases": 1127286,
    "totalRecovered": 370812,
    "criticalCases": 17815,
    "casesPerOneMillion": 4816,
    "deathsPerOneMillion": 287,
    "tests": 14173807,
    "testsPerOneMillion": 42849,
    "continent": "North America",
    "countryInfo": {
        "_id": 840,
        "iso2": "US",
        "iso3": "USA",
        "lat": 38,
        "long": -97,
        "flag": "https://disease.sh/assets/img/flags/us.png"
    },
    "updated": "2020-05-21T05:51:42.546Z",
    "__v": 0
}]
```
