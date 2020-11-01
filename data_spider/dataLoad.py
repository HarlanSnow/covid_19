#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import json
import time

def loadWorldDataJson():
    with open("./json/worldData.json", "r") as f:
        worldDataJson = json.load(f)
        # print(worldJson)
    return worldDataJson

def getWorldData():
    worldDataJson = loadWorldDataJson()
    err_times = 0
    errList = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    for i in range(0, len(worldDataJson)):
        provinceName = worldDataJson[i]['provinceName']
        url = worldDataJson[i]['statisticsData']
        # print(url)
        try:
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            r.encoding = 'utf-8'
            savePath = './json/world/' + provinceName + ".json"
            countryDataJson = json.loads(r.text)
            with open(savePath, "w") as f:
                json.dump(countryDataJson, f, ensure_ascii=False)
            time.sleep(1)

        except:
            err_times += 1
            errList.append(provinceName)
            print(provinceName + "数据获取失败")

    print("completed..")
    print("失败请求次数：", err_times)
    print(errList)

def loadChinaDataJson():
    with open("./json/chinaData.json", "r") as f:
        chinaDataJson = json.load(f)
    return chinaDataJson

def getChinaData():
    chinaDataJson = loadChinaDataJson()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    err_times = 0
    for i in range(len(chinaDataJson)):
        provinceName = chinaDataJson[i]['provinceName']
        url = chinaDataJson[i]['statisticsData']
        savePath = './json/china/' + provinceName + '.json'

        try:
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            r.encoding = 'utf-8'
            dataJson = json.loads(r.text)
            with open(savePath, 'w') as f:
                json.dump(dataJson, f, ensure_ascii=False)
            time.sleep(1)
        except:
            err_times += 1
            print(provinceName + "  数据获取失败")

    print("failed times: ", err_times)

if __name__ == "__main__":
    getChinaData()
    getWorldData()


