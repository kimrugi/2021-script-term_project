import urllib.request
import urllib
from xml.dom.minidom import parse, parseString
save_data_list = ["SIGUN_NM", "LIBRRY_NM", "CLOSE_DE_INFO", "OPERT_BEGIN_TM", "OPERT_END_TM"]

docs = None

def search(to_search):
    global docs
    sigun = urllib.parse.quote(to_search)
    key = '961adfdf5c574548bf2e9352dde74c19'
    url = "https://openapi.gg.go.kr/Library?" + "KEY=" + key + "&SIGUN_NM=" + sigun
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    docs = parseString(resp.read().decode('utf-8'))

    pass





