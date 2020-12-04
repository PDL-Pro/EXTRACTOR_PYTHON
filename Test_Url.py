# -*- coding: utf-8 -*-
"""
# -*- test tout type de lien avec le module urlparse


"""

import unittest
import URL_Function

class URL_Test_Gle (unittest.TestCase):
    
    def test(self):
             
        lien1= 'http://www.cwi.nl:80/%7Eguido/Python.html'
        lien2 = '/data/Python.html'
        lien3  = 532
        URL_Validator.uri_validator(lien1)#return True
        URL_Validator.uri_validator(lien2)#return False
        URL_Validator.uri_validator(lien3)#return False

