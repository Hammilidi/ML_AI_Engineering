# Dictionnaire contenant les étudiants et leurs listes de notes
etudiants = {
    "Arnaud": [15, 14, 13],
    "Kaleb": [10, 12, 9],
    "Noé": [18, 17, 16],
    "Amandine": [18, 17, 16]
}

# Fonction pour calculer la moyenne d'une liste
def moyenne(notes):
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

# Fonction pour afficher les bulletins
def afficher_bulletins(etudiants):
    for nom, notes in etudiants.items():
        moy = moyenne(notes)
        print(f"{nom} : moyenne = {moy:.2f}")

        # Commentaire selon la moyenne
        if moy >= 15:
            print("🟢 Très bien")
        elif moy >= 10:
            print("🟡 Peut mieux faire")
        else:
            print("🔴 En difficulté")
        print("-" * 30)

# Appel de la fonction
afficher_bulletins(etudiants)
