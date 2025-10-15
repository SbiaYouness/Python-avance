class Personne:
    def __init__(self,nom,adresse):
        self.nom=nom
        self.adresse=adresse
    def afficher(self):
        print(f"le nom: {self.nom}, l'adresse: {self.adresse}", end="")

class Employe(Personne) :
    def __init__(self,nom,adresse,cnss):
        self.cnss=cnss
        Personne.__init__(self,nom,adresse)
    def afficher(self):
        super().afficher()
        print(f", la CNSS: {self.cnss}")

class Enseignant(Personne) :
    def __init__(self,nom,adresse,cnops):
        self.cnops=cnops
        Personne.__init__(self,nom,adresse)
    def afficher(self):
        print(f"le nom: {self.nom}, l'adresse: {self.adresse}, la CNOPS: {self.cnops}")

class Etudiant(Personne) :
    def __init__(self,nom,adresse,cne):
        self.cne=cne
        Personne.__init__(self,nom,adresse)
    def afficher(self):
        print(f"le nom: {self.nom}, l'adresse: {self.adresse}, le CNE: {self.cne}")

etud1=Etudiant("sbia","fes","n145344")
ense1=Enseignant("asap","rocks","cnops3")
emp1=Employe("waterson","usa","c3w34343")

etud1.afficher()
emp1.afficher()
ense1.afficher()