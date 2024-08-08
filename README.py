# Python Project 1
# To build a quiz game
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question["text"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        answer = input("Enter your answer (1, 2, 3, or 4): ")
        try:
            answer = int(answer)
            if answer < 1 or answer > 4:
                print("Invalid input. Please enter a number between 1 and 4.")
                return self.ask_question(question)
            answer -= 1
            if question["options"][answer] == question["correct"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is {question['correct']}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.ask_question(question)

    def run_quiz(self):
        for question in self.questions:
            self.ask_question(question)
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

# Example questions
questions = [
    {
        "text": "Which of the following Himalayan regions is called Shivalik's?",
        "options": ["Upper Himalayas", "Outer Himalayas", "Inner Himalayas", "Lower Himalayas"],
        "correct": "Outer Himalayas"
    },
    {
        "text": "Which of the given devices is used for counting blood cells?",
        "options": ["Hmelethometer", "Spyscometer", "Hemocytometer", "Hamosytometer"],
        "correct": "Hemocytometer"
    },
    {
        "text": "What is the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
        "correct": "Vatican City"
    }
]

quiz = Quiz(questions)
quiz.run_quiz()

