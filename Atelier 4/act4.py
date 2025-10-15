class Etudiant :
    sum_notes=0
    count_etudiant=0
    def __init__(self,matricule, nom, prenom, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.note = note
        Etudiant.sum_notes+=note
        Etudiant.count_etudiant+=1
    def afficher(self):
        print("le matricule est: ", self.matricule, ", le nom est: ", self.nom, self.prenom,", la note est: ", self.note)

ALI = Etudiant(23213,"ATIQ","ALI", 18)
SAAD = Etudiant(54516,"TESTn","TESTp", 2)

print("la somme des notes de tout les etudiants est:", Etudiant.sum_notes)
print("la moyenne des notes de tout les etudiants est:", Etudiant.sum_notes/Etudiant.count_etudiant)
