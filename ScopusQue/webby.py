__author__ = 'm088378'

from lxml import etree, html
import requests
import pprint
from conf import Static
import json

pp = pprint.PrettyPrinter(indent=4)

def getAuthorBasic(id):
    mt_url = "{}/author?author_id={}&view=metrics".format(Static.ELSEVIER, id)
    au_url = "{}/author?author_id={}&field=author-profile".format(Static.ELSEVIER, id)
    respAU = requests.get(au_url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})
    respMT = requests.get(mt_url, headers={'Accept': 'application/json', 'X-ELS-APIKey': Static.API_KEY})

    return {'Profile': respAU.json(), 'Metrics': respMT.json()}


#    print json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': '))





if __name__ == '__main__':
    getAuthorBasic(56007630200)
