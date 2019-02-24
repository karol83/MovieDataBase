import factory
import json

from django.test import TestCase, Client
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser

from movies.models import Movie
from movies.views import home
from movies.forms import SearchMovieForm
from movie_database.users.models import User


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = Movie
        django_get_or_create = ('title',)

    title = 'Spiderman'
    # data = json.dumps({'Year': '2001'})


class FavouriteTests(TestCase):

    def setUp(self):
        self.movie = MovieFactory()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob',
            email='jacob@gmail.com',
            password='topsecret'
        )
        self.client = Client()

    def test_home_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], SearchMovieForm)
        self.assertTemplateUsed(response, template_name="pages/home.html")

    def test_home_page_form(self):
        data = {'title': 'Spiderman'}
        form = SearchMovieForm(data=data)
        self.assertTrue(form.is_valid())
