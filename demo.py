# Python program to read
# json file
 
 
import json
 
# Opening JSON file
f_test = open('data.json',)
 
# returns JSON object as
# a dictionary
data_test = json.load(f_test)
 
# Iterating through the json
# list
for i in data_test['eBooks']:
    print(i)
 
# Closing file
f_test.close()