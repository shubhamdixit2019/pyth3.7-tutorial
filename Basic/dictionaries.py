''' 
Used in a situation  when information needs to be stored as a key value pair,
and key is expected to be unique
'''
customers = {
    "name" : "Jon Snow",
    "age" : 32,
    "is_verified" : True
}
customers["birthdate"]= "27 Jan 2019"
customers["name"]="Lord Varys"
print(customers["name"])