class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        for response in self.responses:
            print('- ' + response)


# question = 'What language did you learn first to speak?'
# my_survey = AnonymousSurvey(question)
#
# my_survey.show_question()
#
# print('Enter "quit" to quit at any time.\n')
# while True:
#     response = input('Langauage: ')
#     if response == 'quit':
#         break
#
#     my_survey.store_response(response)
#
# print('\nThank you everyone who participated in the survey!')
# my_survey.show_results()
#
