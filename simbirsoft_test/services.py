from .dto import QuizDTO,  AnswersDTO


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto


    def get_result(self):
        i = 0
        for x in range(5):
            for y in range(4):
                if  self.answers_dto.answers['list_answers'][x]  == self.quiz_dto.questions[x].choices[y].uuid:
                    if self.quiz_dto.questions[x].choices[y].is_correct is True:
                        i += 1

        i = round((i / 5), 2)
        return i
