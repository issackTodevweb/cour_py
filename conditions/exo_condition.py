# age = 22
# compte_actif = True
# autorisation = False
# administrateur = True

# if age < 18:
#     print("âge insuffisant")
# else:
#     if not compte_actif:
#         print("compte inactif")
#     else:
#         if autorisation or administrateur:
#             print("Accès autorisé")
#         else:
#             print("Accès refusé : autorisation manquante")


# ==============================================Opérateurs logiques complexes=====================================

age = 21
moyenne = 14
diplome_informatique = False
experience = 3
suspendu = False

conditions_remplies = (
    age >= 18
    and moyenne >= 12
    and (diplome_informatique or experience >= 2)
    and not suspendu
)

if conditions_remplies:
    print("Candidat accepté")
else:
    print("Candidat refusé")



        
    
    
    
