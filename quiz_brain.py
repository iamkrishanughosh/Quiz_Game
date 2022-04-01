class QuizBrain:

    def __init__(self, q_obj):
        self.question_number = 0
        self.question_list = q_obj

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} "
                           f"{current_question.text} (True/False) : ")
        if user_input in ["True", "T", "t"] and current_question.answer == "True":
            print("Correct answer.")
            return "C"
        elif user_input in ["False", "F", "f"] and current_question.answer == "False":
            print("Correct answer.")
            return "C"
        else:
            print("Wrong answer.")
            return "W"
