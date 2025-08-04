from aventuriers import *
from lieux import *

def boucle_jeu():
    print("🎉 Bienvenue au Village des Aventuriers 🎉")

    nom = input("Quel est le nom de ton aventurier ? > ")
    classe = input("Quelle est sa classe ? [guerrier / mage / voleur] > ")
    aventurier = creer_aventurier(nom, classe)

    while True:
        print("\n============================")
        afficher_profil(aventurier)
        print("============================")
        action = input("Que veux-tu faire ? [explorer / inventaire / journal / quitter] > ").lower()

        if action == "explorer":
            lieu = input("Quel lieu veux-tu explorer ? forêt / montagne / taverne > ").lower()
            explorer_lieu(aventurier, lieu)

        elif action == "inventaire":
            print(f"🎒 Inventaire : {', '.join(aventurier['objets']) if aventurier['objets'] else 'vide'}")

        elif action == "journal":
            print("📜 Journal d’aventure :")
            if aventurier["journal"]:
                for log in aventurier["journal"]:
                    print(f"→ À la {log[0]} : {log[1]}")
            else:
                print("Aucune entrée pour le moment.")

        elif action == "quitter":
            print("\n👋 Merci d’avoir joué ! À bientôt !")
            break

        else:
            print("Commande inconnue. Essaie à nouveau.")

if __name__ == "__main__":
    boucle_jeu()
