# -*- coding: utf-8 -*-

### GLOBAL VARIABLES ###
class Static:
    version = '0.1'
    APP_NAME = 'Scopus Que Assistant'
    WORKUNITS = ["Faculty RA", "BSI IS I", "BSI IS II", "BSI IS Lead", "Biostats SPA", "Biostats MS"]
    ## This API is registered to:  http://bioinformaticstools.mayo.edu/
    API_KEY = 'cd09a4ac6f3441da7d13d2dc37f7b9a3'
    #  API_KEY = '6492f9c867ddf3e84baa10b5971e3e3d'
    ELSEVIER = 'http://api.elsevier.com:80/content'


class Author:
    def __init__(self, id, w, m, p):
        self.scopus_id = id
        self.workunit_id = w
        self.metrics = m
        self.profile = p

    def scopusId(self):
        return self.scopus_id

    def group(self):
        return self.workunit_id

    def fullName(self):
        print "--"

    def hIdx(self):
        return self.metrics['author-retrieval-response'][0]['h-index']
