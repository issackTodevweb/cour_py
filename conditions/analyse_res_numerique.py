# Analyse de résultats numériques
# Cet exercice se rapproche de la logique de traitement de données.
# Sujet
# Un programme reçoit la moyenne d'un étudiant et doit :
# - rejeter toute moyenne inférieure à 0 ou supérieure à 20 ;
# - afficher Non admis si la moyenne est inférieure à 10 ;
# - afficher Admis si elle est comprise entre 10 inclus et 12 exclu ;
# - afficher Bien si elle est comprise entre 12 inclus et 16 exclu ;
# - afficher Très bien si elle est comprise entre 16 et 20 inclus.
# Il doit également indiquer si l'étudiant a une mention, définie ici par une moyenne supérieure ou égale à 12.


try:
    moyenne = float(input("moyenne sur 20: "))

    if not (0 <= moyenne <= 20):
        print("moyenne invalide!")
    else:
        if moyenne < 10:
            resultat = "Non admis"
        elif moyenne < 12:
            resultat = "Admis"
        elif moyenne < 16:
            resultat = "Bien"
        else:
            resultat = "Tres bien"

        print(f"Resultat : {resultat}")

        if moyenne >= 12:
            print("Mention obtenue")
        else:
            print("Pas de mension")

except ValueError:
    print("Erreur : veuillez saisir une valeur numérique.")
