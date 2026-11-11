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
        "description": "The Castle of Cagliostro follows gentleman thief Lupin III..."
        }

     post_response = requests.post(
        f"{base.api_url}/movies/",
        json=movie
    )
     pk= json.loads(post_response.content.decode("UTF-8"))['id']


     self.assertEqual(201, post_response.status_code)

     get_response = requests.get(f"{base.api_url}/movies/")
     self.assertEqual(200, get_response.status_code)
     movie_list = get_response.json()
     self.assertIn(movie['title'], [film['title'] for film in movie_list])
     self.assertIn(movie['director'], [film['director'] for film in movie_list])
     self.assertIn(movie['description'], [film['description'] for film in movie_list])

     delete_response = requests.delete(f"{base.api_url}/movies/{pk}/")
     self.assertEqual(204, delete_response.status_code)

if __name__ == '__main__':
    unittest.main()