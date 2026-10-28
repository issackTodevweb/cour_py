# nom= input(" Quel est votre nom \n")

# note1= float(input("ecriver votre note 1\n"))
# note2= float(input("ecriver votre note 2\n"))
# moyenne= (note1 + note2) / 2

# print(f"{nom} votre moyenne est {moyenne:.2f}/20")


article = input ("Quel article souhaiter vous acheter?\n")

prix = float(input("eciver ici votre estimation de prix\n"))
quantite =  int(input("la quantité?\n"))

montant_total = prix * quantite

print(f"vous avez commander {quantite} {article}, Le montant total est de {montant_total:.2f} $")

