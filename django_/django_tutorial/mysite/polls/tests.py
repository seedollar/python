import datetime
from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
from django.urls import reverse


# Define a helper method to create new questions and persist them
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionMethodTests(TestCase):
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for pubished dates in the future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose pub_date is older than 1 day.
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexDetailsTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text="Future question", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        past_question = create_question(question_text='Past Question', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionVotingTests(TestCase):
    def test_question_voting_incremented_successfully(self):
        mock_question = create_question(question_text="Mock Question?", days=0)
        mock_question.choice_set.create(choice_text="option1", votes=0)
        mock_question.choice_set.create(choice_text="option2", votes=0)
        mock_question.choice_set.create(choice_text="option3", votes=0)
        mock_question.save()

        url = reverse('polls:vote', args=(mock_question.id,))
        response = self.client.post(url, {'choice': '2'})

        voted_choice = Choice.objects.get(choice_text='option2')
        self.assertEqual(voted_choice.votes, 1)

    def test_question_voting_no_choice_made(self):
        mock_question = create_question(question_text="Mock Question no choices", days=0)
        url = reverse('polls:vote', args=(mock_question.id,))
        response = self.client.post(url, {})
        result_error_message = response.context['error_message']
        self.assertTrue(result_error_message is not None)
        self.assertEqual(result_error_message, "You didn't select a choice!")
