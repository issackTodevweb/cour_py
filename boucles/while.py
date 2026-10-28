# compteur = 1 

# while compteur <= 5:
#     print(compteur) 
#     compteur += 1



# try:
#     note = float(input("entrer une note entre 0 à 20: "))
#     while note < 0 or note >20:
#         print("note invalide")
#         note = float(input("entrer une note entre 0 à 20: "))
#     if note >= 10:
#             print("admis")
#     else:
#             print("non admis")
#     print(f"note enregistré: {note}")
# except ValueError:
#     print("Ereur: Entrer une note valide")
      
while True:
    try:
        note = float(input("Saisissez une note entre 0 et 20 : "))

        if 0 <= note <= 20:
            break

        print("Erreur : la note doit être entre 0 et 20.")

    except ValueError:
        print("Erreur : veuillez saisir un nombre.")

print(f"Note enregistrée : {note}")
