import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print(random.choice(string.ascii_letters))




# Fonction pour générer un mot de passe selon les critères
def generer_mot_de_passe(longueur, utiliser_chiffres=True, utiliser_symboles=False):
    if longueur < 4:
        return "Erreur : longueur trop courte (min. 4)"

    caracteres = list(string.ascii_letters)  # Lettres minuscules et majuscules

    if utiliser_chiffres:
        caracteres += list(string.digits)

    if utiliser_symboles:
        caracteres += list(string.punctuation)

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

# # Exemples d’utilisation
# print("Mot de passe simple :", generer_mot_de_passe(10))
# print("Mot de passe avec chiffres :", generer_mot_de_passe(12, utiliser_chiffres=True))
# print("Mot de passe complexe :", generer_mot_de_passe(16, utiliser_chiffres=True, utiliser_symboles=True))
