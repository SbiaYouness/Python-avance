adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
# Q1
print("la premiere adresse est:", adresses_ip[0])
# Q2
print("la derniere adresse est:", adresses_ip[-1])
# Q3
print("la troisieme adresse est:", adresses_ip[2])
# Q4
adresses_ip.append("172.31.0.1")

# iter=0
# for ad in adresses_ip:
#     if "200.100.50.1" in ad:
#         adresses_ip.pop(iter)
#     iter+=1
# Q5
adresses_ip.remove("200.100.50.1")
print("apres la suppression:", adresses_ip)
# Q6
print("les adresses qui restent sont:", len(adresses_ip))
# Q7
if "192.168.0.1" in adresses_ip :
    print("oui elle existe")
else :
    print("non elle n'existe pas")

# adresses_dict= {"192.168.0.1" : "classe C",
# "10.0.0.1" : "classe A",
# "172.16.0.1" : "classe B",
# "200.100.50.1" : "adresse IP publique",
# "169.254.0.1":"adresse IP de lien local (APIPA)"}
# print("classe ip de 10.0.0.1 est:", adresses_dict["10.0.0.1"])

# Q8
adsep="10.0.0.1".split('.')
if int(adsep[0])>0 and int(adsep[0])<128:
    print("classe ip de 10.0.0.1 est la classe A")
else :
    print("10.0.0.1 n'est pas de la classe A")
# Q9
adresses_ip.sort()
print("apres le trie:", adresses_ip)

# Q10
count8=0
for adr8 in adresses_ip :
    adsep2 = adr8.split('.')
    if int(adsep2[0]) >= 192 and int(adsep2[0]) <= 223:
        count8+=1
if count8==len(adresses_ip):
    print("toutes les adresses sont de la classe C")
else :
    print("ce n'est pas vrai que toutes les adresses sont de la classe C")

# Q11
count9=0
for adr9 in adresses_ip :
    adsep3 = adr9.split('.')
    if int(adsep3[0]) == 10 or (int(adsep3[0]) == 172 and int(adsep3[1]) >= 16) or (int(adsep3[0]) == 172 and int(adsep3[1]) <= 31) or (int(adsep3[0]) == 192 and int(adsep3[1]) == 168):
        count9+=1

print("le nombre des classes publiques est:", count9)

