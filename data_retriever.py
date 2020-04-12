from bs4 import BeautifulSoup
# coding: utf-8
import os
import string
import requests
import util

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class DataRetriever:

    def __init__(self):
        self.filePath = CURRENT_DIRECTORY + '/data/allBands.json'
        self.baseUrl = "https://www.metal-archives.com/browse/ajax-letter/l/" #{letter}/json/".format(letter=letter)

    def apiCall(self, letter, displayStart):
        """
        Api call to retrieve 500 entries for a letter, given offset
        :param letter: letter from alphabet, to retrieve
        :param displayStart: index to get data (each page of data contains 500 entries)
        :return: data as a list of lists, size of records for letter
        """
        url = self.baseUrl + '{letter}/json/'.format(letter=letter)
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0'},
                           params={"iDisplayStart": displayStart, "iSortCol_0": 0, "sEcho": 1}).json()

        totalRecords = req['iTotalRecords']
        data = req['aaData']

        print('Successfully got data from {}, displayStart {}, out of {}'.format(letter, displayStart, totalRecords))

        return data, totalRecords

    def retrieveDataForLetter(self, letter):
        """
        Retrieve all pages for a specific letter of the alphabet
        :param letter: letter from alphabet, to retrieve
        :return: list of dictionaries
        """
        fullData = []
        displayStart = 0

        while True:
            data, totalRecords = self.apiCall(letter, displayStart)

            # Convert list of lists to list of dictionaries
            convertedBandList = [self.bandListToDict(band) for band in data]

            print('Extended dataset to [{}/{}]'.format(len(fullData), totalRecords))

            if len(convertedBandList) == 0:
                return fullData
            else:
                fullData.extend(convertedBandList)
                displayStart += 500

    def bandListToDict(self, band):
        """
        Converts list which contains band info to dictionary
        :param band:list
        :return: dictionary
        """
        band_tag = BeautifulSoup(band[0], "lxml").a
        band_url = band_tag.attrs.get("href")
        band_name = band_tag.string
        country = band[1]
        genre = band[2]
        status = BeautifulSoup(band[3], "lxml").span.string
        return { "band_name": band_name, "band_url": band_url, "country": country, "genre": genre, "status": status }

    def retrieveData(self):
        """
        Retrieve all metal bands from metal archives
        :return: None - writes json file to file path
        """
        fullData = []
        for i in string.ascii_uppercase:
            data = self.retrieveDataForLetter(i)
            fullData.extend(data)

        util.writeJsonToFile(fullData, self.filePath)

a = DataRetriever()
a.retrieveData()