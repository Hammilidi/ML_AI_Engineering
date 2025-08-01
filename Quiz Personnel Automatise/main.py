from quiz import charger_questions, évaluer_reponses, afficher_score

def main():
    print("🧠 Bienvenue dans le quiz personnel !\n")
    questions = charger_questions()
    score = évaluer_reponses(questions)
    afficher_score(score, len(questions))

if __name__ == "__main__":
    main()
