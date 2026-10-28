# Exercice 3 — Algorithme de facturation
# Sujet
# Tu développes un petit programme de vente.

# Le programme doit demander :
# - le prix unitaire d'un produit ;
# - la quantité achetée ;
# - si le client est membre premium.
# Règles commerciales :
# 1. Le prix doit être strictement positif.
# 2. La quantité doit être strictement positive.
# 3. Si le montant avant réduction atteint 100 000 Ar, le client reçoit 10 % de réduction.
# 4. Sinon, si le client est premium, il reçoit 5 % de réduction.
# 5. Les deux réductions ne sont pas cumulables.
# 6. La livraison coûte 5 000 Ar si le montant après réduction est inférieur à 50 000 Ar ; sinon, elle est gratuite.

try:
    prix_unitaire = float(input("Prix unitaire: "))
    quantite = int(input("quantité: "))
    reponse_premium = input("Client premium ? (oui/non) : ")
    if prix_unitaire <= 0:
        print("Erreur: Le prix doit être strictement positif")
    elif quantite <= 0:
        print("Erreur : la quantité doit être positive")
    elif reponse_premium not in ("oui", "non"):
        print("Erreur : répondez par oui ou non")
    else:
        premium = reponse_premium == "oui"
        montant_initial = prix_unitaire * quantite

        if montant_initial >= 100000:
            taux_reduction = 0.10
        elif premium:
            taux_reduction = 0.05
        else:
            taux_reduction = 0

        reduction = montant_initial * taux_reduction
        montant_apres_reduction = montant_initial - reduction

        if montant_apres_reduction < 50000:
            frais_livraison = 5000 
        else:
            frais_livraison = 0

        montant_final = montant_apres_reduction + frais_livraison

        print(f"Montant initial : {montant_initial:.2f} Ar")
        print(f"Réduction : {reduction:.2f} Ar")
        print(f"Frais de livraison : {frais_livraison:.2f} Ar")
        print(f"Montant final : {montant_final:.2f} Ar")



except ValueError:
    print("Erreur : saisissez un prix et une quantité valides.")
