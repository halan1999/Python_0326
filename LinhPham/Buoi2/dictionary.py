employees = {   "name": "linh", 
                "age": 25,
                "phoneNo": "0432398423",
                "note": "N/A"
            }

#Them gia tri
employees["address"] = "DN"

#Cap nhat gia tri
employees.update({"age": 26})
#or
employees["name"] = "Hoai Linh"

#Delete
del employees ["phoneNo"]
#0r
employees.pop("note")

print(employees)