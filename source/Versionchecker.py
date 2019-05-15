import os
import requests

#現在のバージョン取得
vercheck = "http://mnbqjp-version.witchs-weapon.com:9091/getversion"
html = requests.get(vercheck)
version = html.text

print(version)

#assetlistを取得しに行く
url = "http://cdnjp-android-release.witchs-weapon.com/m.assets_list_" + version + ".txt"

#ダウンロード処理
response = requests.get(url)
savefilename = "m.assets_list_" + version + ".txt"

with open(savefilename, mode="wb") as savefile:
    savefile.write(response.content)

print("Success!")