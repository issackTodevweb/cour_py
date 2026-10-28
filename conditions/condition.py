# nom= input("saisissez votre nom : ")
# try:
#     moyenne= float(input("saisissez votre moyenne : "))

#     if not (0<= moyenne <=20):
#         print("Saisie un moyenne valide")
#     else:
#         if moyenne<10:
#             print("Non admis")
#         elif 10<= moyenne <12:
#             print("Admis")
#         elif 12<= moyenne <16:
#             print("Bien")
#         else:
#             print("Tres bien")       

# except ValueError:
#     print("erreur !!!: saisissez un nombre valide")

# try:
#     age = int(input("Quel est votre âge ? "))

#     if not (age > 0):
#         print("l'age ne peut etre negatif")
#     else:
#         if age < 6:
#             print("Le prix du billet: gratuit")
#         elif age <=17:
#             print("Le prix du billet: 2000 Ar")
#         elif age <=59:
#             print("Le prix du billet: 5000 Ar")
#         else:
#             print("Le prix du billet: 3000 Ar")

# except:
#     print("saisissez un age valide")


# age = 20
# moyenne = 13
# diplome = False
# experience = 3

# if age>=18 and moyenne >=12 and (diplome or experience >=2):
#     print ("Candidat admis")
# else:
#     print("Candidat non admis")
    
nom_utilisateur= input(" saisissez votre nom d'utilisateur: ")
mot_de_passe = input("Votre mot de passe: ")
compte_actif = True

if nom_utilisateur == "admin" and mot_de_passe == "python123" and compte_actif:
    print("Connexion autorisée")
else:
    print("Connexion non autorisée")