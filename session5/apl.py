from urllib.request import urlopen
import json

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4&fbclid=IwAR2y2Zo1AW7PKNa_DbpeGYyhFZzCkfpL1-dPPZz__tSBmRmS-3Y9nZZE_oU"

#1. open connection
conn = urlopen(url)

#2. read data
raw_data = conn.read()

#3. Decode data
text = raw_data.decode("utf-8")
print(text)
data = json.loads(text)
print(type(data))
print(data)
results = data["results"]
results = 0
print(results["s"],["a"])
print()