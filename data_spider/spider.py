#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json

def getOriHtmlText(url,code='utf-8'):
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return "There are some errors when get the original html!"


url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
if __name__ == "__main__":
    html = getOriHtmlText(url)
    soup = BeautifulSoup(html, 'html.parser')
    htmlBody = soup.body

    worldDataText = htmlBody.find(id="getListByCountryTypeService2true").text
    worldDataStr = worldDataText[worldDataText.find('['): worldDataText.find(']')+1]
    # print(worldDataStr)
    worldDataJson = json.loads(worldDataStr)
    with open("./json/worldData.json", "w", encoding='utf-8') as f:
        json.dump(worldDataJson, f, ensure_ascii=False)
        print("save succeed")

    areaDataText = htmlBody.find(id="getAreaStat").text
    areaDataStr = areaDataText[areaDataText.find('['):areaDataText.rfind(']')+1]
    # print(areaDataStr)
    areaDataJson = json.loads(areaDataStr)
    with open("./json/chinaData.json", "w", encoding='utf-8') as f:
        json.dump(areaDataJson, f, ensure_ascii=False)
        print("save succeed")









