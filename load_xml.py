import urllib.request
import urllib
from xml.dom.minidom import parse, parseString
'''save_data_list = ["SIGUN_NM", "LIBRRY_NM", "CLOSE_DE_INFO", "OPERT_BEGIN_TM", "OPERT_END_TM",
                  "LIBRRY_TELNO", "REFINE_ROADNM_ADDR", "REFINE_WGS84_LOGT", "REFINE_WGS84_LAT",
                  "TMP01", "TMP02", "TMP03", "TEMP", "BOOK_DATA_CNT"]
rename_data_list = ["SIGUN_NM", "LIBRRY_NM", "CLOSE_DE_INFO", "BEGIN_TM", "END_TM",
                  "LIBRRY_TELNO", "ADDRESS", "LONGI", "LAT",
                  "SAT_BEGIN_TM", "SAT_END_TM", "HOLI_BEGIN_TM", "HOLI_END_TM", "BOOK_NUM"]'''

save_data_dict = {'SIGUN_NM': 'SIGUN_NM', 'LIBRRY_NM': 'LIBRRY_NM',
                  'CLOSE_DE_INFO': 'CLOSE_DE_INFO', 'OPERT_BEGIN_TM': 'BEGIN_TM',
                  'OPERT_END_TM': 'END_TM', 'LIBRRY_TELNO': 'LIBRRY_TELNO',
                  'REFINE_ROADNM_ADDR': 'ROAD_ADDRESS', 'REFINE_WGS84_LOGT': 'LONGI',
                  'REFINE_WGS84_LAT': 'LAT', 'TMP01': 'SAT_BEGIN_TM', 'TMP02': 'SAT_END_TM',
                  'TMP03': 'HOLI_BEGIN_TM', 'TEMP': 'HOLI_END_TM', 'BOOK_DATA_CNT': 'BOOK_NUM', "REFINE_LOTNO_ADDR" : "ADDRESS"}


library_list = []


def search_name(name, lib_list=None):
    if lib_list is None:
        global library_list
        lib_list = library_list
    result = []
    for lib in lib_list:
        if lib["LIBRRY_NM"].find(name) != -1:
            result.append(lib)
        elif lib["ADDRESS"].find(name) != -1:
            result.append(lib)
        elif lib["ROAD_ADDRESS"].find(name) != -1:
            result.append(lib)
    return result


def search_and_register(to_search):
    global library_list
    library_list = search(to_search)

def search(to_search):
    #검색
    sigun = urllib.parse.quote(to_search)
    key = '961adfdf5c574548bf2e9352dde74c19'
    url = "https://openapi.gg.go.kr/Library?" + "KEY=" + key + "&SIGUN_NM=" + sigun
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    docs = parseString(resp.read().decode('utf-8'))

    #저장
    library_list = []
    library = docs.childNodes[0].childNodes
    # head = library[1].childNodes
    # num_of_library = head[1].childNodes[0].nodeValue
    for row in library:
        if row.nodeName == "row":
            library_data = {}
            for comp in row.childNodes:
                if comp.nodeName in save_data_dict.keys():
                    library_data[save_data_dict[comp.nodeName]] = comp.childNodes[0].nodeValue
            library_list.append(library_data)
    return library_list








