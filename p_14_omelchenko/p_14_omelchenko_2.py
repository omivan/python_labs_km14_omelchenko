import json
with open('image_info_test-dev2017.json') as f:
    data = json.load(f)

print("1) " + str(len(data["images"])))
print("2) " + str(len(data["categories"])))
print('3)', end='')
first = list()
for x in data['images']:
    if x['file_name'] == "000000000001.jpg":
        print("coco_url = " + str(x["coco_url"]) + " | height = " + str(x["height"]) + " | width = " + str(x["width"]) + " | id = " + str(x['id']))
max_id = 0
name_max_id = ""
for x in data["images"]:
    if(int(x['id']) > max_id): 
        max_id = x['id'] 
        name_max_id = x['file_name']
print('4)Max id has ' + name_max_id)




