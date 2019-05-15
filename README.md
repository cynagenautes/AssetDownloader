# AssetDownloader

## なにこれ

魔女兵器のAssetをCDNから落っことしてくるツール  
その他メンテナンス用のツールも含みます  
Pythonが理解できる人向けにしか作ってないのでソース見て挙動は確認してください

## 使い方

* 入ってるAssetDownloader.pyを実行する
  * assets_list.txt dir_path_list.txt filename_list.txtが同じディレクトリに存在しないと動きません

* 環境はPython 3.7.3 64bit Windows10でのみ確認

* モジュールとしてrequestsが必要です

## その他ツール

* `Versionchecker.py`  
実行するとバージョンチェックを行い最新のAssetlistをカレントディレクトリにダウンロードします

## クレジット

* fork元の [AssetDownloader
](https://github.com/MayaYamato/AssetDownloader) @MayaYamato様