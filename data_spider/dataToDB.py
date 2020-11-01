#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import os
import pymysql
import traceback


def getFileJson(file):
    with open(file, 'r') as f:
        proviceJson = json.load(f)
    return proviceJson

# def loadProviceFile(path):
#     files = os.listdir(path)
#     # print(files)
#     return files

def worldDataToDB():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="Lww.520.",
        database='covid_19',
        charset='utf8'
    )

    sql = """                     
        insert into worldData(confirmedCount,confirmedIncr,curedCount,curedIncr,curConfirmedCount,curConfirmedIncr,dateID,deadCount,deadIncr,suspectedCount,suspectedIncr,countryName,countryShortCode,continent,countryFullName) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

    countryjson = getFileJson("./json/WorldCountryName.json")
    for key in countryjson:
        countryName = countryjson[key]["provinceName"]
        countryShortCode = countryjson[key]["countryShortCode"]
        continent = countryjson[key]["continents"]
        countryFullName = countryjson[key]["countryFullName"]
        filepath = "./json/world/" + countryName + ".json"
        dataJson = getFileJson(filepath)
        data = dataJson['data']

        datalist = []
        for i in range(len(data)):
            confirmedCount = data[i]["confirmedCount"]
            confirmedIncr = data[i]["confirmedIncr"]
            curedCount = data[i]["curedCount"]
            curedIncr = data[i]["curedIncr"]
            curConfirmedCount = data[i]["currentConfirmedCount"]
            curConfirmedIncr = data[i]["currentConfirmedIncr"]
            dateID = data[i]["dateId"]
            deadCount = data[i]["deadCount"]
            deadIncr = data[i]["deadIncr"]
            suspectedCount = data[i]["suspectedCount"]
            suspectedIncr = data[i]["suspectedCountIncr"]
            temp_tuple = (confirmedCount, confirmedIncr, curedCount, curedIncr, curConfirmedCount, curConfirmedIncr,
                          dateID, deadCount, deadIncr, suspectedCount, suspectedIncr, countryName, countryShortCode,
                          continent, countryFullName)
            datalist.append(temp_tuple)

        try:
            with conn.cursor() as cursor:
                cursor.executemany(sql, datalist)
            conn.commit()
            print("insert data succeed: ", countryShortCode)
        except:
            conn.rollback()
            traceback.print_exc()
            print("insert data failed: ", countryShortCode)

    conn.close()


def chinaDataToDB():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="Lww.520.",
        database='covid_19',
        charset='utf8'
    )

    sql = """                     
        insert into chinaData(confirmedCount,confirmedIncr,curedCount,curedIncr,curConfirmedCount,curConfirmedIncr,dateID,deadCount,deadIncr,suspectedCount,suspectedIncr,provinceName,provinceShortName) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  
        """

    provincejson = getFileJson("./json/ChineseProvinceName.json")
    for key in provincejson:
        provinceName = provincejson[key]['provinceName']
        provinceShortName = provincejson[key]['provinceShortName']
        filepath = './json/china/'+provinceName + ".json"
        dataJson = getFileJson(filepath)
        data = dataJson['data']

        datalist = []
        for i in range(len(data)):
            confirmedCount = data[i]["confirmedCount"]
            confirmedIncr = data[i]["confirmedIncr"]
            curedCount = data[i]["curedCount"]
            curedIncr = data[i]["curedIncr"]
            curConfirmedCount = data[i]["currentConfirmedCount"]
            curConfirmedIncr = data[i]["currentConfirmedIncr"]
            dateID = data[i]["dateId"]
            deadCount = data[i]["deadCount"]
            deadIncr = data[i]["deadIncr"]
            suspectedCount = data[i]["suspectedCount"]
            suspectedIncr = data[i]["suspectedCountIncr"]
            temp_tuple = (confirmedCount, confirmedIncr, curedCount, curedIncr, curConfirmedCount, curConfirmedIncr,
             dateID, deadCount, deadIncr, suspectedCount, suspectedIncr, provinceName, provinceShortName)
            datalist.append(temp_tuple)

        try:
            with conn.cursor() as cursor:
                cursor.executemany(sql, datalist)
            conn.commit()
            print("insert data succeed.")
        except:
            conn.rollback()
            traceback.print_exc()
            print("insert data failed: ", provinceName)

    conn.close()

if __name__ == "__main__":
    # chinaDataToDB()
    worldDataToDB()














