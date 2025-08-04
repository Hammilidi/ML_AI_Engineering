# Dictionnaire de produits avec leurs prix
catalogue = {
    "pomme": 0.5,
    "banane": 0.3,
    "lait": 1.2,
    "pain": 1.0
}

# Fonction pour ajouter un produit au panier
def ajouter_au_panier(panier, produit):
    if produit in catalogue:
        panier.append(produit)  # On ajoute le produit à la liste
        print(f"{produit} ajouté au panier.")
    else:
        print(f"Produit inconnu : {produit}")

# Fonction pour afficher le total du panier
def afficher_total(panier):
    total = 0
    for produit in panier:
        total = total + catalogue[produit]  # On récupère le prix depuis le dictionnaire
    print(f"Total à payer : {total} €")

# Simulation d'utilisation
mon_panier = []
ajouter_au_panier(mon_panier, "pomme")
ajouter_au_panier(mon_panier, "lait")
ajouter_au_panier(mon_panier, "chocolat")  # Produit inconnu
ajouter_au_panier(mon_panier, "pain")

print("\nPanier final :", mon_panier)
afficher_total(mon_panier)
