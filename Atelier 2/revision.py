capitals = {"usa":"washington d.c.",
            "india":"new delhi",
            "china":"beijing",
            "russia":"moscow"}

# print(capitals.get("china"))
# capitals.update({"china":"chiners"})
# print(capitals.get("china"))
# capitals.update({"germany":"berlin"}) #append
# print(capitals)
# print(capitals.get("germany"))
# capitals.pop("china")
# print(capitals)
# capitals.popitem()
# print(capitals)
# capitals.clear()
# print(capitals)
# keys = capitals.keys()
# for key in capitals.keys() :
#     print(key)

values = capitals.values()
for value in capitals.values() :
    print(value)
print(capitals.values())

items = capitals.items()
print(items)

for key, value in capitals.items() :
    print(key, ",", value )
