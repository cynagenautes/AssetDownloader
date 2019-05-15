import os
import requests
import urllib.error
import urllib.request

#ダウンロードディレクトリの設定
with open('dir_path_list.txt') as dir_paths:
    for tmp_path in dir_paths:
        dir_path = tmp_path.rstrip('\r\n')
        if dir_path != "0":
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)

#ダウンロード時の関数
def download_asset(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

print('Loading file')

with open('assets_list.txt') as lines, open('filename_list.txt') as filenames, open('dir_path_list.txt') as dir_paths:
    for (line, tmp_name, tmp_path) in zip(lines, filenames, dir_paths):
        
        url = line.rstrip('\r\n')
        filename = tmp_name.rstrip('\r\n')
        dir_path = tmp_path.rstrip('\r\n')
        
        if dir_path == "0":
            print(filename)
            if os.path.exists(filename):
                #10000回までfor同一ファイル保存を回避できる
                for n in range (1, 10000):
                    #保存名をfilename+(n)に変更
                    new_filename = str(filename)  + '(' + str(n) + ')'
                    #dst_pathの再設定(ファイルネームの変更)
                    if not os.path.exists(new_filename):
                        download_asset(url, new_filename)
                        break
                    else:
                        #既に重複ファイル回避がされていた場合さらにforを回す必要がある
                        continue
            else:
                download_asset(url, filename)
        else:
            #pathの結合 asset/+filename
            dst_path = os.path.join(dir_path, filename)
            print(dst_path)
            if os.path.exists(dst_path):
                #10000回までfor同一ファイル保存を回避できる
                for n in range (1, 10000):
                    #保存名をfilename+(n)に変更
                    new_filename = str(filename)  + '(' + str(n) + ')'
                    #dst_pathの再設定(ファイルネームの変更)
                    dst_path = os.path.join(dir_path, new_filename)

                    if not os.path.exists(dst_path):
                        download_asset(url, dst_path)
                        break
                    else:
                    #既に重複ファイル回避がされていた場合さらにforを回す必要がある
                        continue
            else:
                download_asset(url, dst_path)