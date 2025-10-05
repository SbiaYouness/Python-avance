machines= {
    "m1":"192.168.0.1",
    "m2":"192.168.0.2",
    "m3":"192.168.0.3",
    "m4":"192.168.0.4",
    "m5":"192.168.0.5"
}
# indice customizable

print(machines["m2"])
print(len(machines))
machines["m6"]="192.168.0.6"
print("apres ajout",machines)
del machines["m4"]
# machines.pop("m4")
print("apres suppression",machines)
mach=input("entrez le nom de machine: ")
if mach in machines.keys():
    print(f"{mach} exist est sa valeur est: {machines['m5']}")
else:
    print(f"{mach} doesnt exist")