__author__ = 'm088378'

import requests
from conf import *
import json

import pprint


# from lxml import etree, html
#from ConfigParser import SafeConfigParser


# pp = pprint.PrettyPrinter(indent=4)
# print json.dumps(t, sort_keys=True, indent=4, separators=(',', ': '))


def getAuthorProfile(id):
    url = "{}/author?author_id={}".format(Static.ELSEVIER, id)
    resp = requests.get(url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})
    return resp.json()

def getAuthorMetrics(id):
    #    url = "{}/author/author_id/{}?apiKey={}".format(Static.ELSEVIER, id, Static.API_KEY)
    url = "{}/author/author_id/{}?view=metrics".format(Static.ELSEVIER, id)
    resp = requests.get(url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})
    return resp.json()


if __name__ == '__main__':
    ## auto get my author when run as standalone script
    # getAuthorMetrics(56007630200)
    print "\n"
    t = getAuthorProfile(56007630200)
    print json.dumps(t, sort_keys=True, indent=4, separators=(',', ': '))
