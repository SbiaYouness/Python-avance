t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

for i in range (12):
    t2.insert((i*2)+1, t1[i])
# print(t2[::])
print(t2)