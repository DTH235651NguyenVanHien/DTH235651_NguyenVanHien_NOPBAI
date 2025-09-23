import json
jsonString = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

dataObject = json.loads(jsonString)
print(dataObject)
print("Ma ", dataObject["ma"])
print("Tuoi ", dataObject["age"])
print("Ten ", dataObject["ten"])