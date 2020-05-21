# 👑 COVID19 tracker
Этот пакет добавляет в python api https://data.nepalcorona.info/api
## 🚀 Установка
Скачать covid19.py, разместить в папке с Вашим проектом и импортировать его:
```python
import sys
sys.path.insert(0, path)
import covid19
```
## 🤖 Функции
### 🌎 getWorld
Присылает распарсенный json c сайта https://data.nepalcorona.ino/api/v1/world
#### 📥 Ввод
```python
covid19.getWorld()
```
#### 📤 Вывод
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
Присылает распарсенный json c сайта https://nepalcorona.info/api/v1/data/world
#### 📥 Ввод
```python
covid19.getCountries()
```
#### 📤 Вывод
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
