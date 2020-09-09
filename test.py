from random import randrange
from math import ceil

continu = True
banque = 500


while continu:

    num_choisi = -1

    while num_choisi < 0 or num_choisi > 3:

        num_choisi = input("Choisissez un numéro compris entre 0 et 3:" )
        num_choisi = int(num_choisi)
        if num_choisi < 0 or num_choisi > 3:
            print("Vous devez choisir un numéro entre 0 et 3")


    mise = 0

    while mise <= 0 or mise > banque:
        print("Vous avez:", banque, "pièces")
        mise = input("Montant de la mise:")
        mise = int(mise)

        if mise <= 0:
            print("Vous devez miser au moins 1 pièce")
        
        if mise > banque:
            print("Vous n'avez pas assez d'argent, il vous reste", banque)


    num_gagnant = randrange(4)
    
    if num_choisi != num_gagnant:
        print("Perdu! vous avez choisi :", num_choisi, "le numéro tiré est le", num_gagnant, "rejouez!")
        banque -= mise
        continu = True
        
    else:
        print("Félicitations! vous avez tiré le bon numéro!", num_gagnant)
        banque += mise*3
        continu = True

    if banque <= 0:
        print("Vous n'avez plus d'argent!")   
        continu = False
    else:
        print("Il vous reste:", banque)
        arreter = input("Vous voulez arrêter? tapez Y pour oui ou N pour non:")
        arreter = str(arreter)
            
        if arreter == "n" or arreter == "N":
            print("On continu!")
            continu = True
        elif arreter =="Y" or arreter == "y":
            print("Merci d'avoir joué!")
            continu = False
        else:
            print("Votre choix n'est pas valide!")