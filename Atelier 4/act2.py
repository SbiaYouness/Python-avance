class Voiture :
    def __init__(self,code, marque, kilometrage):
        self.code = code
        self.marque = marque
        self.kilometrage = kilometrage
    def mod_kilo(self,val):
        self.kilometrage+=val
    def afficher(self):
        print("le code de voiture est: ", self.code)
        print("la marque de voiture est: ", self.marque)
        print("le kilometrage de voiture est: ", self.kilometrage)

v1 = Voiture(23213,"chevy",200304)
v2 = Voiture(13894,"audi",152000)
v3 = Voiture(75983,"mercedes",16000)
v1.mod_kilo(1000)
v1.afficher()