# from serpapi import GoogleSearch
import serpapi
import inspect
print(inspect.getsource(serpapi.serp_api_client))

import inspect
# print(inspect.getsource(GoogleSearch))
# print(inspect.getsource(GoogleSearch.))
#
# print(inspect.getsource(serpapi.serp_api_client))

import src.gc
from src.resources.test.serpapi import GoogleSearch
# print(inspect.getsource(serpapi.serp_api_client))
key = 'a553fbab28db696394e944a38b85de297c7f2b5b044e0a4ab69c785c91900cbc'
GoogleSearch({
    "q": "coffee",
    "location": "Austin,Texas",
    "api_key": key
  })
x = GoogleSearch({
    "q": "coffee",
    "location": "Austin,Texas",
    "api_key": key
  })

x.get_dict()

result = search.get_dict()



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
miles.speak()