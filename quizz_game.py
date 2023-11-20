#sanket suryavanshi
#Quiz Game

import random

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus"],
        "answer": "Mars",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7"],
        "answer": "7",
    },
]

def load_question():
    return random.choice(quiz_data)

def display_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

def evaluate_answer(question_data, user_answer):
    correct_answer = question_data["answer"]
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return 0

def display_final_score(score, total_questions):
    print(f"You scored {score} out of {total_questions}.")

def main():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice questions.")
    print("Please enter the number of your answer.")

    total_questions = 5
    score = 0

    for _ in range(total_questions):
        question_data = load_question()
        display_question(question_data)
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(question_data["options"]):
                user_answer = question_data["options"][user_answer - 1]
                score += evaluate_answer(question_data, user_answer)
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    display_final_score(score, total_questions)

if __name__ == "__main__":
    main()