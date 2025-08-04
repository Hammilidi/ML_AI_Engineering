def creer_aventurier(nom, classe):
    stats_base = {
        "guerrier": (8, 3),
        "mage": (3, 8),
        "voleur": (5, 6)
    }
    force, chance = stats_base.get(classe, (5, 5))
    return {
        "nom": nom,
        "classe": classe,
        "force": force,
        "chance": chance,
        "objets": set(),
        "journal": []
    }

def afficher_profil(av):
    print(f"\n👤 {av['nom']} le {av['classe'].capitalize()}")
    print(f"Force : {av['force']} | Chance : {av['chance']}")
    print(f"Objets : {', '.join(av['objets']) if av['objets'] else 'Aucun'}")
