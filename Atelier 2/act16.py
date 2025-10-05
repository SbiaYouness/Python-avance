l3=[1,2,3,4,5]
for i in range (5):
    print(l3[i])

s=0
for i in range (5):
    s+=l3[i]
print("la somme est:",s)

for i in range (2,5):
    s*=l3[i]
    print(l3[i])

print("le produit est:",s)
