from datetime import date

class Employe:
    def __init__(self,identifiant,nom, prenom, dateNaissance, dateEmbauche, salaire):
        self.identifiant=identifiant
        self.nom=nom
        self.prenom=prenom
        self.dateNaissance=dateNaissance
        self.dateEmbauche=dateEmbauche
        self.salaire=salaire

    def get_id(self):
        return self.identifiant
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_datenaissance(self):
        return self.dateNaissance
    def get_dateembauche(self):
        return self.dateEmbauche
    def get_salaire(self):
        return self.salaire

    def set_id(self, id):
        self.id=id
    def set_nom(self,nom):
        self.nom=nom
    def set_prenom(self,prenom):
        self.prenom=prenom
    def set_datenaissance(self,datenaissance):
        self.dateNaissance=datenaissance
    def set_dateembauche(self,dateembauche):
        self.dateEmbauche=dateembauche
    def set_salaire(self,salaire):
        self.salaire=salaire

    def age(self):
        return (date.today()-self.dateNaissance)/365


emp1 = Employe(4342,"nom", "prenom", date(2002,10,19), date(2022,11,29), 342223)
print(emp1.age())