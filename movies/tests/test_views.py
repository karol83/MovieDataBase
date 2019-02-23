import factory
import json

from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser

from movies.models import Movie
from movies.views import home
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

    def test_home_page(self):
        request = self.factory.get(reverse('home'))
        request.user = self.user
        request.user = AnonymousUser()

        response = home(request)
        self.assertEqual(response.status_code, 200)
