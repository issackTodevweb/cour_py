# Défi algorithmique : année bissextile
# Sujet
# Une année est bissextile :
# - si elle est divisible par 400 ; ou
# - si elle est divisible par 4, mais pas par 100.
# Quelques exemples :
# - 2024 est bissextile.
# - 1900 n'est pas bissextile.
# - 2000 est bissextile.
# - 2025 n'est pas bissextile.

# Étape 1 — Comprendre le modulo %
# Le modulo % donne le reste d'une division entière.
# print(10 % 2)  # 0   print(10 % 3)  # 1   print(12 % 4)  # 0



# Si annee % 4 == 0, cela signifie que l'année est divisible par 4 sans reste.
# Étape 2 — Traduire la règle en logique
# Une année est bissextile si :
# annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)



# Décomposons cette expression :
# - annee % 400 == 0 : divisible par 400.
# - annee % 4 == 0 : divisible par 4.
# - annee % 100 != 0 : non divisible par 100.
# - and exige que les deux dernières conditions soient vraies ensemble.
# - or accepte la première règle ou la deuxième.


try:
    annee = int(input("Ecrivez l'année: "))

    if annee <= 0 :
        print("entrer une année positif!")
    elif annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print(f"{annee} est une année Bissextile")
    else:
        print(f"{annee} n'est pas une année bissextile")

except ValueError:
    print("Erreur : saisissez une année entière.")