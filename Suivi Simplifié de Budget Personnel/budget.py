budget = {
    "2025-08": {
        "alimentation": 150,
        "transport": 50,
        "loisirs": 75
    }
}

def ajouter_dépense(budget, mois, catégorie, montant):
    if mois not in budget:
        budget[mois] = {}
    if catégorie not in budget[mois]:
        budget[mois][catégorie] = 0
    budget[mois][catégorie] += montant

def total_par_catégorie(budget, mois):
    if mois not in budget:
        print(f"Aucune donnée pour le mois {mois}.")
        return
    for catégorie, montant in budget[mois].items():
        print(f"{catégorie} : {montant} €")

def afficher_recapitulatif(budget, mois):
    if mois not in budget:
        print(f"Aucune dépense enregistrée pour {mois}.")
        return
    total = 0
    print(f"--- Récapitulatif pour {mois} ---")
    for catégorie, montant in budget[mois].items():
        print(f"{catégorie.capitalize()} : {montant} €")
        total += montant
    print(f"Total : {total} €")

import json

def sauvegarder_budget(budget, fichier="budget.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(budget, f, indent=4)


import os

def charger_budget(fichier="budget.json"):
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}
