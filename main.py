import json
from pathlib import Path


QUESTIONS_FILE = Path(__file__).parent / "data" / "questions.json"


def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions


def show_question(question_data):
    print()
    print(question_data["question"])

    for number, option in enumerate(question_data["options"], start=1):
        print(f"{number}. {option}")


def get_user_answer(total_options):
    while True:
        try:
            answer = int(input("Digite o número da resposta: "))

            if 1 <= answer <= total_options:
                return answer

            print(f"Digite um número entre 1 e {total_options}.")

        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def is_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def run_quiz():
    questions = load_questions()
    score = 0

    for question_data in questions:
        show_question(question_data)

        total_options = len(question_data["options"])
        user_answer = get_user_answer(total_options)

        if is_correct(user_answer, question_data["correct_answer"]):
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta errada.")

    print()
    print("Quiz finalizado!")
    print(f"Pontuação final: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()