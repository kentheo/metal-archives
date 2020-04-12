from bs4 import BeautifulSoup
# coding: utf-8
import urllib.request, json, requests
import string
# url1 = "https://www.metal-archives.com/browse/ajax-letter/l/A/json/1?sEcho=1&iColumns=4&sColumns=&iDisplayStart=1600&iDisplayLength=1&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1586383264333"
# url_raw = "https://www.metal-archives.com/browse/ajax-letter/l/A/json/"
# req = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
#
# webpage = urllib.request.urlopen(req).read()
# fff = json.loads(webpage)
# print(fff)
def bandListToDict(band):
    """
    Converts list which contains band info to dictionary
    :param band:list
    :return: dictionary
    """
    band_tag = BeautifulSoup(band[0],"lxml").a
    band_url = band_tag.attrs.get("href")
    band_name = band_tag.string
    country = band[1]
    genre = band[2]
    status = BeautifulSoup(band[3],"lxml").span.string
    return {"band_name":band_name,"band_url":band_url,"country":country,"genre":genre,"status":status}



url_template = "https://www.metal-archives.com/browse/ajax-letter/l/{}/json/"
data = []
for i in string.ascii_uppercase:
    req = requests.get(url_template.format(i),headers={'user-agent': 'Mozilla/5.0'},params={"iDisplayStart":0,"iSortCol_0":0,"sEcho":1})
    list_of_letter = req.json()["aaData"]
    list_of_letter = [bandListToDict(band) for band in list_of_letter]
    data = [*data,*list_of_letter]
