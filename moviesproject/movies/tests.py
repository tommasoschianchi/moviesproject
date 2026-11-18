

from django.test import TestCase
import json
import unittest

import requests
from moviesproject import base
class NewVisitorTest(unittest.TestCase):
    def test_can_add_a_fil_and_retrieve_it_later_then_delete(self):
    # Frank has heard about a new cool RESTful Web Application on
    # which you can save your favourite Film and Tv series.
    # He thinks
    # for a while, then remember the wonderful Tv series called
    # "Lupin", he watched on Netflix.
    # Create a new movie
     movie = {
        "title": "Lupin III"
        ,
        "subtitle": "Il castello di Cagliostro"
        ,
        "director": "Hayao Miyazaki"
        ,
        "description": "The Castle of Cagliostro follows gentleman thief Lupin III...",

        }
     movie_string= str(movie)
     movie['movie_hash'] = hash(movie_string)
     
     login_data = {
            "username": "tommaso5",
            "password": "mypass123"
        }

     login_response = requests.post(
        f"{base.api_url}/dj-rest-auth/login/",
        json=login_data
     )

     if login_response.status_code != 200:
        registration_data = {
            "username": "tommaso5",
            "password1": "mypass123",
            "password2": "mypass123"
        }
        reg_response = requests.post(
            f"{base.api_url}/dj-rest-auth/registration/",
            json=registration_data
        )
        self.assertEqual(204, reg_response.status_code)
        login_response = requests.post(
            f"{base.api_url}/dj-rest-auth/login/",
            json=login_data
        )

     self.assertEqual(200, login_response.status_code)
     token = login_response.json()['key']
     headers = {"Authorization": f"Token {token}"}

     post_response = requests.post(
        f"{base.api_url}/movies/",
        json=movie,
        headers=headers
     )
     self.assertEqual(201, post_response.status_code)
     pk = post_response.json()['id']

     get_response = requests.get(f"{base.api_url}/movies/", headers=headers)
     self.assertEqual(200, get_response.status_code)
     movie_list = get_response.json()
     self.assertIn(movie['movie_hash'], [film['movie_hash'] for film in movie_list])

     delete_response = requests.delete(f"{base.api_url}/movies/{pk}/", headers=headers)
     self.assertEqual(204, delete_response.status_code)
    

""" class AuthenticationTest(unittest.TestCase):
    def test_registration_and_login(self):
    # Talking with her friends,
    # Debora gets to know a new Website
    # that allows users to save their favourite films.
    # Going to check out its homepage
    # she notices it is necessary to
    # create a new account.
        registration_data = {
            "username": "tommaso4",
            "password1": "mypass123",
            "password2": "mypass123"
        }
        post_response = requests.post(
            f"{base.api_url}/dj-rest-auth/registration/",
            json=registration_data
        )
        # She hits enter and the account has been created.
        self.assertEqual(post_response.status_code, 201)

        login_data = {
            "username": "tommaso4",
            "password": "mypass123"
        }
        post_response = requests.post(
            f"{base.api_url}/dj-rest-auth/login/", json=login_data
        )
        self.assertEqual(post_response.status_code, 200)
 """


if __name__ == '__main__':
    unittest.main()
