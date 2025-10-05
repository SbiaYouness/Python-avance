class Voiture:
    def __init__(self,cd,mrq,pu,km):
        self.code=cd
        self.marque=mrq
        self.puissance = pu
        self.kilometrage = km

    def mod_puiss(self,pui):
        self.puissance=pui

    def mod_kilo(self, kilo):
        self.kilometrage=kilo

    def afficher(self):
        print(f"La voiture du code {self.code} et de marque {self.marque} a une puissance de {self.puissance}J et a rouler {self.kilometrage}km")

car1=Voiture(5,"audi", 433, 2344443)
car2=Voiture(3,"volswagen", 7493, 8262341)
car3=Voiture(2,"bmw", 7353, 7445194)

car1.mod_puiss(2)
car2.afficher()
car3.mod_kilo(0)
car1.afficher()
car3.afficher()

