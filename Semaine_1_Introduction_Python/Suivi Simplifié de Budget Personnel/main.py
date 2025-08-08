from budget import (
    ajouter_dépense, total_par_catégorie,
    afficher_recapitulatif, sauvegarder_budget,
    charger_budget
)
from datetime import datetime

def main():
    budget = charger_budget()
    mois_actuel = datetime.now().strftime("%Y-%m")

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1 - Ajouter une dépense")
        print("2 - Voir le récapitulatif du mois")
        print("3 - Sauvegarder et quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            catégorie = input("Catégorie : ")
            montant = float(input("Montant (€) : "))
            ajouter_dépense(budget, mois_actuel, catégorie, montant)
        elif choix == "2":
            afficher_recapitulatif(budget, mois_actuel)
        elif choix == "3":
            sauvegarder_budget(budget)
            print("Budget sauvegardé. À bientôt !")
            break
        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
