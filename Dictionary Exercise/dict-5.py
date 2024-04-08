sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

res = dict()
for k in keys:
    res.update({k:sampleDict[k]})
print(res)

asn = {i: sampleDict[i] for i in keys}
print(asn)
