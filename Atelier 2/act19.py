# # q1
# def f1(n):
#     for i in range (n):
#         print("bonjour")
#
# n=int(input("entrez combien de fois afficher: "))
# f1(n)

# # q2
# def f2(n):
#     if n%10==0:
#         return True
#     else:
#         return False
# n=int(input("entrez le nombre: "))
# print(f2(n))

# #q3
# def f4(n):
#     # if n==0:
#     #     return 1
#     # return n*f4(n-1)
#     fac = 1
#     for i in range(1,n+1):
#         fac*=i
#     return fac
# n=int(input("entrez le nombre: "))
# print(f4(n))

# #q4
# def f3(chaine):
#     v = 0
#     for c in chaine:
#         if c in ["e","i","o","u","y","a"] :
#             v+=1
#     print(v)
#
# chaine=input("entrez le string: ")
# f3(chaine)

# # q5
# def f5(chif):
#     print(f"Le tableau de multiplication de {chif} est: ")
#     for i in range(1,11):
#         print(f"{chif} x {i} = {chif*i}")
#
# chif=int(input("entrez le chiffre: "))
# f5(chif)

# #q6
# def f6(mot):
#     count = 0
#     for c in mot:
#         count+=1
#     return count
#
# mot=input("entrez le mot: ")
# print(f6(mot))

#q7
def f7(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return f7(n-1)+f7(n-2)
n=int(input("entrez le nombre: "))
print(f7(n))