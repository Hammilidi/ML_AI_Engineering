def charger_questions():
    return {
        "Quelle est la capitale de la France ?": "Paris",
        "Combien font 2 + 2 ?": "4",
        "Quel est le langage utilisé dans ce projet ?": "Python",
        "Qui a peint La Joconde ?": "Leonard de Vinci",
        "Quel est le plus grand océan du monde ?": "Pacifique",
        "Combien y a-t-il de continents ?": "7",
        "Qui a écrit Les Misérables ?": "Victor Hugo",
        "Quelle est la racine carrée de 81 ?": "9",
        "En quelle année a eu lieu la Révolution française ?": "1789",
        "Quel est le symbole chimique de l’eau ?": "H2O",
        "Quel est le plus petit nombre premier ?": "2",
        "Qui a développé la théorie de la relativité ?": "Einstein",
        "Quel est le pays d’origine des sushis ?": "Japon",
        "Combien de bits y a-t-il dans un octet ?": "8",
        "Quel est le navigateur web développé par Google ?": "Chrome",
        "Quelle planète est la plus proche du Soleil ?": "Mercure",
        "Combien de jours y a-t-il dans une année bissextile ?": "366",
        "Quel organe pompe le sang dans le corps humain ?": "Cœur",
        "Quelle est la capitale du Canada ?": "Ottawa",
        "Combien de lettres contient l’alphabet français ?": "26"
    }


def poser_question(question, bonne_reponse):
    reponse = input(question + "\n> ")
    return reponse.strip().lower() == bonne_reponse.strip().lower()


def évaluer_reponses(questions):
    score = 0
    for question, bonne_reponse in questions.items():
        if poser_question(question, bonne_reponse):
            print("✅ Bonne réponse !\n")
            score += 1
        else:
            print(f"❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}\n")
    return score

def afficher_score(score, total):
    print(f"🎉 Vous avez obtenu {score} bonne(s) réponse(s) sur {total} !")
    if score == total:
        print("Excellent, bravo !")
    elif score >= total / 2:
        print("Pas mal, continuez à vous entraîner !")
    else:
        print("Il faut réviser un peu plus 😉")
