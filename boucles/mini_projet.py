
# 7. Mini-projet : analyser les notes d'une classe
# Nous allons construire un programme qui analyse plusieurs notes, calcule leur moyenne et compte le nombre d'étudiants admis.
# Cahier des charges
# Le programme doit :
# 1. demander combien de notes seront saisies ;
# 2. demander chaque note ;
# 3. vérifier que chaque note est comprise entre 0 et 20 ;
# 4. calculer la moyenne de la classe ;
# 5. compter le nombre de notes supérieures ou égales à 10 ;
# 6. afficher le résultat.



# < >
#
# 
try:

    nombre_notes = int(input("combient de notes seront saisies: "))

    if nombre_notes <= 0:
        print("les nombres des notes doivent être positif")
    else:
        compteur = 0
        somme = 0
        admis = 0

        while compteur < nombre_notes:
            try:
                note = float(input(f"Note {compteur + 1} : "))

                if not (0 <= note <= 20):
                    print("Entre une note est comprise entre 0 et 20 ")
                    continue

                somme = somme + note

                if note >= 10:
                    admis += 1

                compteur = compteur + 1
            except ValueError:
                print("Erreur: entrez un nombre")


    moyenne = somme / nombre_notes
    print("============Resultat buletin===========")
    print(f"Nombre de notes : {nombre_notes}")
    print(f"Moyenne de la classe : {moyenne:.2f}/20")
    print(f"Nombre d'étudiants admis : {admis}")
    print(f"Nombre d'étudiants non admis : {nombre_notes - admis}")
    

except ValueError:
    print("entrer un nombre entier pour le nombre de note")
