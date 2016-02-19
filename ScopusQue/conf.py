# -*- coding: utf-8 -*-

### GLOBAL VARIABLES ###
class Static:
    version = '0.1'
    APP_NAME = 'Scopus Que Assistant'
    WORKUNITS = ["Faculty RA", "BSI IS I", "BSI IS II", "BSI IS Lead", "Biostats SPA", "Biostats MS"]
    ## This API is registered to:  http://bioinformaticstools.mayo.edu/
    API_KEY = 'cd09a4ac6f3441da7d13d2dc37f7b9a3'
    ELSEVIER = 'http://api.elsevier.com:80/content'


class Author:
    scopus_id = 0
    workunit = ''
    url = ''
