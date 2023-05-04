class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(
            f"Q.{self.question_number}: {current_question.q_text} (True/False): ")
        self.check_answer(current_question.q_answer)

    def check_answer(self, correct_answer):
        if self.user_answer.lower() == correct_answer.lower():
            print("you got right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

        print("\n")
