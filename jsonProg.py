import json
d='{"id":"09", "name": "Nitin", "department":"Finance"}'

print("JSON FILE TYPE ",type(d))

de=json.loads(d)
print("After conversion TYPE of : ",de," is : ",type(de))

d=json.dumps(de)
de=json.loads(d)
print("After conversion TYPE of : ",d," is : ",type(d))
