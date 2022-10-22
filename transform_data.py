import json

# Opening JSON file
f = open('my_export.json','r')
w= open("training.txt", "w")
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['conversations']:
    w.write("{0} \n".format(i[0]))
    w.write("{0} \n".format(i[1]))
   
# Closing file
f.close()
w.close()
