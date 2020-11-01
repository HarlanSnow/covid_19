#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json


def loadFileJson(file):
    with open(file, "r") as f:
        dataJson = json.load(f)
    return dataJson


def provinceMatch():
    file = './json/chinaData.json'
    provinceDataJson = loadFileJson(file)

    nameDict = {}
    for i in range(len(provinceDataJson)):
        provinceName = provinceDataJson[i]['provinceName']
        dic = {'provinceName': provinceDataJson[i]['provinceName'], 'provinceShortName': provinceDataJson[i]['provinceShortName']}
        nameDict[provinceName] = dic

    with open('./json/ChineseProvinceName.json', 'w') as f:
        json.dump(nameDict, f, ensure_ascii=False)
        print("file saved...")


def countryMatch():
    file = './json/worldData.json'
    countryDataJson = loadFileJson(file)

    nameDict = {}
    for i in range(len(countryDataJson)):
        provinceName = countryDataJson[i]['provinceName']
        dic = {"continents": countryDataJson[i]["continents"], "provinceName": countryDataJson[i]['provinceName'],
               "countryShortCode": countryDataJson[i]["countryShortCode"], "countryFullName": countryDataJson[i]["countryFullName"]}
        nameDict[provinceName] = dic

    with open('./json/WorldCountryName.json', 'w') as f:
        json.dump(nameDict, f, ensure_ascii=False)
        print("file saved...")


if __name__ == "__main__":
    provinceMatch()
    # countryMatch()

