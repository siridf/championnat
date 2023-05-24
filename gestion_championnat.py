from typing import List
from operator import itemgetter

class Equipe: 
    id = 0
    nom = ''
    date_creation = ''
    stade = ''
    entraineur = ''
    president = ''
    point_gagne = 0
    point_nul = 0
    point_perdu = 0

    def __init__(self, id, nom, date_creation, stade, entraineur, president, point_gagne, point_perdu, point_nul,) -> None:
        self.id = id 
        self.nom = nom
        self.date_creation = date_creation
        self.stade = stade
        self.entraineur = entraineur
        self.president = president
        self.point_gagne = point_gagne
        self.point_nul = point_nul
        self.point_perdu = point_perdu

    def afficher(self):
        print(self.id)
        print(self.nom)
        print(self.date_creation)
        print(self.stade)
        print(self.entraineur)
        print(self.president)
        print(self.point_gagne)
        print(self.point_nul)
        print(self.point_perdu)

class Match():
    def __init__(self, score_equipe1, score_equipe2, numero_journee, equipe1, equipe2) -> None:
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2
        self.numero_journee = numero_journee
        self.equipe1 = equipe1
        self.equipe2 = equipe2

class Championnat(): 
    id = 0
    nom = ''
    date_debut = ''
    date_fin = ''
    type_classement = ''
    equipes:List[Equipe] = []
    matchs:List[Match] = []

    def __init__(self, id, nom, date_debut, date_fin, type_classement, equipes, matchs):
        self.id = id
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.type_classement = type_classement
        self.equipes = equipes 
        self.matchs = matchs
    
    def afficher(self):
        print(self.id)
        print(self.nom)
        print(self.date_debut)
        print(self.date_fin)
        print(self.type_classement)
        for equipe in self.equipes:
            print(equipe.nom)
        for match in self.matchs: 
            print(match.equipe1 + " vs " + match.equipe2)
    
    def ajouterEquipe(self, equipe : Equipe):
        self.equipes.append(equipe)
        
    def ajouterMatch(self, match : Match):
        self.matchs.append(match)
        
    def calculer_point(self, equipe : Equipe): 
        total = equipe.point_gagne + equipe.point_nul - equipe.point_perdu
        return total
    
    def get_classement(self): 
        for match in self.matchs: 
            if match.score_equipe1 > match.score_equipe2 :
                self.equipes[match.equipe1.id - 1].point_gagne += 1
                self.equipes[match.equipe2.id - 1].point_perdu += 1
            elif match.score_equipe1 == match.score_equipe2 :
                self.equipes[match.equipe1.id - 1].point_nul += 1
                self.equipes[match.equipe2.id - 1].point_nul += 1
            else : 
                self.equipes[match.equipe1.id - 1].point_perdu += 1
                self.equipes[match.equipe2.id - 1].point_gagne += 1

        scores = []
        for equipe in self.equipes : 
            scores.append([equipe, self.calculer_point(equipe)])
        classement = sorted(scores,key=itemgetter(1), reverse=True)
        return classement
    

class GestionChampionnat(): 
    championnats:List[Championnat] = []
    def __init__(self):
        self.championnats = []

    def ajouter_championnat(self, championnat):
        self.championnats.append(championnat)

    def ajouter_equipe(self, id, equipe):
        self.championnats[id - 1].ajouterEquipe(equipe)

    def ajouter_match(self, id, match):
        self.championnats[id - 1].ajouterMatch(match)
    
    def afficher_equipes(self, id):
        for equipe in self.championnats[id - 1].equipes :
            print(equipe.nom)

    def afficher_classement(self, id):
        classements = self.championnats[id - 1].get_classement()
        i = 1
        print("place equipe T G P N ")
        for classement in classements : 
            print(str(i) + " " + classement[0].nom + " " + str(classement[1]) + " " + str(classement[0].point_gagne) + " " + str(classement[0].point_perdu) + " " + str(classement[0].point_nul))
            i += 1



def afficher_menu():
    print("1. Ajouter un championnat")
    print("2. Ajouter une equipe")
    print("3. Saisir le resultat d'un match")
    print("4. Afficher les championnats")
    print("5. Afficher la liste des equipes d'un championnat")
    print("6. Afficher le classement d'un championnat")
    print("7. Quitter l'application")


def creerUnChampionnat(id) : 
    nom = input("Entrez le nom du championnat : ")
    date_debut = input("Entrez la date de debut du championnat : ")
    date_fin = input("Entrez la date de fin du championnat : ")
    type_classement = input("Entrez le type de classement du championnat : ")
    newChamp = Championnat(id, nom, date_debut, date_fin, type_classement, [], [])
    return newChamp; 


def creerUneEquipe(id) :
    nom = input("Entrez le nom de l'equipe: ")
    date_creation = input("Entrez la date de creation de l'equipe : ")
    stade = input("Entrez le stade de l'equipe : ")
    entraineur = input("Entrez l'entraineur de l'equipe : ")
    president = input("Entrez le président de l'equipe : ")
    return Equipe(id, nom, date_creation, stade, entraineur, president, 0, 0, 0)


def creerUnMatch(championnat : Championnat):
    id_equipe1 = 0
    id_equipe2 = 0
    if len(championnat.equipes) < 2 :
        print("Ajouter des equipes a votre championnat")
        return
    else : 
        print("Equipes disponibles : ")
        for equipe in championnat.equipes :
            print(str(equipe.id) + " : " + equipe.nom)
            
        while(id_equipe1 == 0):
            try:
                choix = int(input("Entrez l'equipe 1 : "))
                if choix > len(championnat.equipes) or choix < 1 : 
                    print("Veuillez entrer une valeur valide")
                else: id_equipe1 = choix
            except ValueError as err:
                print("Veuillez saisir une valeur correcte !")

        while(id_equipe2 == 0):
            try : 
                choix2 = int(input("Entrez l'equipe 2 : "))
                if choix2 > len(championnat.equipes) or choix2 < 1 : 
                    print("Veuillez entrer une valeur valide")
                else: id_equipe2 = choix2
            except ValueError as err:
                print("Veuillez saisir une valeur correcte !")


        score_equipe1 = int(input("Entrez le score de l'equipe 1 :"))
        score_equipe2 = int(input("Entrez le score de l'equipe 2 :"))
        numero_journee = int(input("Entrez le numero de la journee :"))
        return Match(score_equipe1, score_equipe2, numero_journee, championnat.equipes[id_equipe1 - 1], championnat.equipes[id_equipe2 - 1])
    
def getIdChamp(gestionChamp : GestionChampionnat) :
        id_champ_choisi = 0
        if len(gestionChamp.championnats) < 1 :
            print("Ajouter un championnat!!")
            return
        else : 
            print("Championnats disponibles : ")
            for championnat in gestionChamp.championnats :
                print(str(championnat.id) + " : " + championnat.nom)
                
            while(id_champ_choisi == 0):
                try : 
                    choix = int(input("Entrez le championnat : "))
                    if choix > len(gestionChamp.championnats) or choix < 1 : 
                        print("Veuillez entrer une valeur valide")
                    else: id_champ_choisi = choix
                except ValueError as err:
                    print("Veuillez saisir une valeur correcte !")
            return id_champ_choisi


gestionChampionnat = GestionChampionnat()
choix = 0
id_championnat = 1
id_equipe = 1


while choix != 7:
    try :
        afficher_menu()
        choix = int(input("Choix : "))

        if choix == 1:
            gestionChampionnat.ajouter_championnat(creerUnChampionnat(id_championnat))
            id_championnat += 1

        elif choix == 2:
            id_champ_choisi = getIdChamp(gestionChampionnat)
            gestionChampionnat.ajouter_equipe(id_champ_choisi, creerUneEquipe(id_equipe))
            id_equipe += 1

        elif choix == 3:
            id_champ_choisi = getIdChamp(gestionChampionnat)
            gestionChampionnat.ajouter_match(id_champ_choisi, creerUnMatch(gestionChampionnat.championnats[id_champ_choisi - 1]))
            
        elif choix == 4:
            for championnat in gestionChampionnat.championnats :
                print(championnat.nom)

        elif choix == 5:
            id_champ_choisi = getIdChamp(gestionChampionnat)
            gestionChampionnat.afficher_equipes(id_champ_choisi)
            
        elif choix == 6:
            id_champ_choisi = getIdChamp(gestionChampionnat)
            gestionChampionnat.afficher_classement(id_champ_choisi)
        
        elif choix == 7:
            print("au revoir!")
        
        else :
            print("entrez une valeur valide!")
    except ValueError as err:
                print("Veuillez saisir une valeur correcte !")

    