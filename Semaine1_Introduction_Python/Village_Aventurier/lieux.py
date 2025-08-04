import random

lieux = {
    "forêt": {
        "objet": "plume magique",
        "danger": "loup sauvage",
        "difficulté": 4
    },
    "montagne": {
        "objet": "pierre d’endurance",
        "danger": "troll des glaces",
        "difficulté": 6
    },
    "taverne": {
        "objet": "rumeur ancienne",
        "danger": None,
        "difficulté": 1
    }
}

def explorer_lieu(aventurier, nom_lieu):
    if nom_lieu not in lieux:
        print("⛔ Ce lieu n'existe pas.")
        return

    lieu = lieux[nom_lieu]
    difficulté = lieu["difficulté"]
    danger = lieu["danger"]
    chance_du_jour = random.randint(1, 10)

    print(f"\n🌍 {aventurier['nom']} explore la {nom_lieu}...")

    if chance_du_jour + aventurier["chance"] >= difficulté:
        objet = lieu["objet"]
        aventurier["objets"].add(objet)
        aventurier["journal"].append((nom_lieu, f"a trouvé {objet}"))
        print(f"🎁 Tu as trouvé : {objet} !")
    else:
        if danger:
            aventurier["journal"].append((nom_lieu, f"a été attaqué par {danger}"))
            print(f"⚠️ Tu es tombé sur un danger : {danger} !")
        else:
            aventurier["journal"].append((nom_lieu, "n’a rien trouvé..."))
            print("🤷‍♂️ Rien trouvé cette fois.")
