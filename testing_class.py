import unittest
from eleven_chapter_class import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = 'What languages did you learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = 'What languages did you learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['Uzbek', 'Russian', 'English']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()