# -*- coding: utf-8 -*-
import json

### GLOBAL VARIABLES ###
class Static:
    version = '0.1'
    APP_NAME = 'Scopus Que Assistant'
    WORKUNITS = ["Faculty RA", "BSI IS I", "BSI IS II", "BSI IS Lead", "Biostats SPA", "Biostats MS"]
    ## This API is registered to:  http://bioinformaticstools.mayo.edu/
    API_KEY = 'cd09a4ac6f3441da7d13d2dc37f7b9a3'
    #  API_KEY = '6492f9c867ddf3e84baa10b5971e3e3d'
    ELSEVIER = 'http://api.elsevier.com:80/content'


def raw2json(arr):
    simplifiedArr = []
    for au in arr:
        tmpObj = {'id': au.scopus_id, 'group': au.workunit_id, 'metrics': au.metrics, 'profile': au.profile}
        simplifiedArr.append(json.dumps(tmpObj, default=lambda o: o.__dict__))
    return simplifiedArr

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
        try:
            nameObj = self.profile['author-retrieval-response'][0]['author-profile']['preferred-name']
            return "{} {}".format(nameObj['given-name'], nameObj['surname'])
        except:
            return '- ! -'

    def hIdx(self):
        try:
            return self.metrics['author-retrieval-response'][0]['h-index']
        except:
            return '-1'

    def coauthorNx(self):
        try:
            return self.metrics['author-retrieval-response'][0]['coauthor-count']
        except:
            return '-1'

    def citationNx(self):
        try:
            return self.metrics['author-retrieval-response'][0]['coredata']['citation-count']
        except:
            return '-1'

    def citedByNx(self):
        try:
            return self.metrics['author-retrieval-response'][0]['coredata']['cited-by-count']
        except:
            return '-1'

    def totalPubNx(self):
        try:
            return self.metrics['author-retrieval-response'][0]['coredata']['document-count']
        except:
            return '-1'

    def url(self):
        try:
            return self.metrics['author-retrieval-response'][0]['coredata']['prism:url']
        except:
            return 'http://api.elsevier.com/'

    def affiliationNx(self):
        try:
            return len(self.profile['author-retrieval-response'][0]['affiliation-history']['affiliation'])
        except:
            return '0'



    def __str__(self):
        str = "\nID: {}\nName: {}\nGroup: {}\nMetrics: {}\n".format(
            self.scopus_id,
            self.fullName(),
            self.group(),
            json.dumps(self.metrics, sort_keys=True, indent=4, separators=(',', ': ')))
        return str
