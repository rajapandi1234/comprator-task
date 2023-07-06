import json
with open("identity_mapping.json", "r") as f1:
    file1 = json.loads(f1.read())
with open("id_schema_latest.json", "r") as f2:
    file2 = json.loads(f2.read())

#FOR GETTING THE KEYS IN ID_SCHEMA
def get_all_keys(dictionary):
   keys=[]
   if isinstance(dictionary, dict):
      for key,value in dictionary.items():
         keys.append(key)
         keys.extend(get_all_keys(value))
   return keys

all_keys=get_all_keys(file2)

#FOR GETTING THE VALUES IN IDENTITY_MAPPING
def get_values(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from get_values(v)     
    else:
      yield v

values_of_id_mapping=(list(get_values(file1)))

#FOR SPLITTING UP THE WORDS IN VALUES WHICH ARE SEPERATED BY COMMA AND COMPARING IT WITH THE ID SCHEMA
for x in values_of_id_mapping:
      if "," in x in values_of_id_mapping:
         splited=x.split(",")
         for item in splited:
            if item not in all_keys:
               print(f"\n {item} present in fullAddress field in identity mapping but not in id schema")




        
#FOR COMPARING ITEMS VALUES WITH ALL KEYS EXCEPT THE ITEMS SEPERATED WITH COMMA
for item in values_of_id_mapping:
    if "," in item in values_of_id_mapping:
       continue
    if item not in all_keys:
      print(f"\n {item} field present in identity mapping but not in id schema")
      
