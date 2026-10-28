# nombre = 7

# for i in range(1, 11):
#     table = nombre * i
#     print (f"{nombre} X {i} = {table}")



# compteur = 0

# for i in range(11):
#     compteur += 1

# print(compteur)



# somme = 0

# for note in [12, 15, 10, 17]:
#     somme = somme + note
# moyenne = somme / 4
# print(f"la moyenne est {moyenne}")



# notes = [12, 15, 17, 10]
# somme = 0
# nombre_diviseur = 0

# for note in notes: 
#     somme += note
#     nombre_diviseur += 1

# if nombre_diviseur > 0:
#     moyenne = somme / nombre_diviseur
#     print(f"la moyenne est {moyenne}")


# ======================PACOURIR UNE LISTE AVEC FOR =====================================

# temperatures = [20, 10, 15, 28, 24]

# compteur = 0 
# for temperature in temperatures:
#     if temperature > 20:
#         compteur += 1 
# print(f"le nombre des temperatures supérieur à 20 : {compteur}")



valeurs = [10, -3, 7, -2, 5]

# boucle for valeur in valeurs: if positif ; calcule somme 
somme = 0
for valeur in valeurs:
    if valeur >= 0: 
        somme = somme + valeur
print(f"somme valeur positif: {somme}")