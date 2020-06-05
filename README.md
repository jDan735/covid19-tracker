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
#### 📤 Output `cson`
```cson
countries: 215
population: 7752910421
updated: 1591356479526
cases:
	all: 6727231
	new: 34537
	stats: 863
deaths:
	all: 393617
	new: 1319
	stats: 50.5
recovered:
	all: 3269829
	new: 27718
	stats: 421.76
active:
	all: 3063785
	new: 34537
	stats: 395.18
	critical:
		all: 55463
		new: 0
		stats: 7.15
tests:
	all: 92588077
	new: 0
	stats: 11942.36
```
### 🗺 getCountries
Send parsed json from https://nepalcorona.info/api/v1/data/world
#### 📥 Input
```python
covid19.getCountries()
```
#### 📤 Output `cson`
```cson
[{
    updated: "2020-06-05T11:27:59.529Z"
    cases:
    	all: 1924428
    	new: 377
    	stats: 5816
    deaths:
    	all: 110180
    	new: 7
    	stats: 333
    recovered:
    	all: 712252
    active:
    	all: 1101996
    	new: 377
    	stats: 0
    	critical:
    		all: 17083
    		new: 0
    		stats: 0
    tests:
    	all: 19568069
    	new: 0
    	stats: 59142
    country:
    	name: "USA"
    	flag: "https://disease.sh/assets/img/flags/us.png"
    	codes:
    		iso2: "US"
    		iso3: "USA"
    	location:
    		continent: "North America"
    		lat: 38
    		long: -97
}]
```
