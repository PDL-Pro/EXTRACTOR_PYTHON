# -*- coding: utf-8 -*-
"""
# -*- Urlparse Module pour les fonctions d'analyse d'URL

@author: Kevin
"""
        
from urllib.parse import urlparse
class URL_Gle:
    
    def _init_(self,url):
        self.url = url 


def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False
    
    

