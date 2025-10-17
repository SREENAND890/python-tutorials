# d={
#     "name":"unaiskaa",
#     "age":"31",
#     "place":"palakad"
# }
# print(d["name"])


# d={
#     "name":"unaiskaa",
#     "age":"31",
#     "place":"palakkad"
# }
# print(d.get("age"))

# a=dict(name="unaiskaa",age="30",place="palakkad")
# print(a)


# d={
#     "name":"unaiskaa",
#     "age":"31",
#     "place":"palakad"
# }
# d["place"]="valanchery"
# d["cuntry"]="india"
# print(d)




# # nested dict
# nested={
#     "d":{"name":"unaiskaa","age":"31","place":"palakad"},
#     "e":{"name":"unais","age":"22","place":"valanchery"}
# }
# print(nested["e"]["age"])


data={"name":"john","age":"28","city":"malappuram"}
ndata=data.setdefault("city","palakkad")
print(data)
print(ndata)

data={"name":"john","age":"28","city":"malappuram"}
data.update({"city":"palakkad","age":"30"})
print(data)








