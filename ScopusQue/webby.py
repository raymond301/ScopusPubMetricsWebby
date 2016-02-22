__author__ = 'm088378'

from lxml import etree, html
import requests
import pprint
from conf import *
import json
from ConfigParser import SafeConfigParser


pp = pprint.PrettyPrinter(indent=4)


# def getAuthorProfile(id):
#     url = "{}/author?author_id={}".format(Static.ELSEVIER, id)
#     print url
#     resp = requests.get(url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})
#
#     t = resp.json()
#     print json.dumps(t, sort_keys=True, indent=4, separators=(',', ': '))
#     #return respAU.json()
#


def getAuthorMetrics(id):
    url = "{}/author/author_id/{}?view=metrics".format(Static.ELSEVIER, id)
    #    url = "{}/author/author_id/{}?apiKey={}".format(Static.ELSEVIER, id, Static.API_KEY)
    print url
    resp = requests.get(url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})
    #    resp = requests.get(url, headers={'Accept': 'application/json'})

    t = resp.json()
    # print json.dumps(t, sort_keys=True, indent=4, separators=(',', ': '))

    au = Author(id, 'grp', t, None)
    print au.hIdx()

    # return resp.json()
    # jdata = json.load(t)
    #print t['author-retrieval-response'][0]['h-index']

if __name__ == '__main__':
    getAuthorMetrics(56007630200)
    print "\n"
    #getAuthorProfile(56007630200)
