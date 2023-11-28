#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        if (name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

    def get_name(self):
        return self._name

