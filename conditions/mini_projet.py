# Mini-projet final — Système d'admission à une formation Data
# Nous allons maintenant combiner ce que tu viens d'apprendre dans un programme plus complet.
# Cahier des charges
# Le programme doit demander :
# - le nom du candidat ;
# - son âge ;
# - sa moyenne sur 20 ;
# - ses années d'expérience en programmation ;
# - s'il possède un diplôme informatique.
# Règles :
# 1. L'âge doit être positif ou nul et la moyenne doit être entre 0 et 20.
# 2. Le candidat doit avoir au moins 18 ans.
# 3. Sa moyenne doit être au moins égale à 12.
# 4. Il doit avoir un diplôme informatique ou au moins deux ans d'expérience.
# 5. Le programme doit afficher un message de refus ou d'acceptation.

nom = input("Votre nom: ")
try:
    age = int(input("votre âge: "))
    moyenne = float(input("moyenne /20 : "))
    experience = int(input("votre exepérience en programmation: "))
    reponse_diplome = input("Diplome informatique? (oui/non): ").strip().lower()
    if age < 0 or experience < 0:
        print("age ou experience invalide")
    elif not (0 <= moyenne <= 20):
        print("la moyenne doit être entre 0 et 20.")
    elif reponse_diplome not in ("oui", "non"):
        print("Erreur : répondez par oui ou non.")
    else:
        diplome = reponse_diplome == "oui"
        if age >= 18 and moyenne >= 12 and (diplome or experience >= 2):
            print(f"{nom} vous êtes admis")
        else:
            print(f"Desolé {nom} vous n'êtes pas admis")
except ValueError:
    print("Erreur: vérifier les valeurs numériques saisies")