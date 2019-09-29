## ASR Serverを使う

### Webサーバのインストール
1. CherryPyのインストール

```
$ cd ~/Downloads
$ wget https://pypi.python.org/packages/source/C/CherryPy/CherryPy-3.8.1.tar.gz#md5=919301731c9835cf7941f8bdc1aee9aa
$ tar zxvf CherryPy-3.8.1.tar.gz
$ cd CherryPy-3.8.1
$ sudo python setup.py install
```

2. ASRサーバ起動

```
python ASRServer.py
```

### Webサーバの起動

1. サーバ起動方法
```
python ~/Software/julius/ASRServer.py
```

- バックグランドで動作させたい場合

```
sudo nohup python ~/Software/julius/ASRServer.py  &
```


2.waveデータを，サーバに対してPOST送信すればよいです。
```
http://サーバ先:8000/asr_julius
```


*) リンク先やポート番号は、ASRServer.py内の設定を変更すること



