# KOTONOHA
---

## リンク先
|リンク先の概要|URL|
|:---:|:---|
|公式サイト|https://julius.osdn.jp/|
|参考にしたサイト 1|https://qiita.com/sayonari/items/65a5aea83d1fadac7d5c|
|参考にしたサイト 2|https://julius.osdn.jp/juliusbook/ja/desc_module.html|

---

## テスト環境情報
### 導入バージョン
- julius 4.3.1
- dictation-kit-4.5

### テストサーバー
- Windows 10
- ubuntu (Windows Subsystem for Linux)

---
## インストール

### コンパイルに必要なライブラリをインストール


### コンパイルに必要なライブラリをインストール

### apt-getが使える場合
```bash
$ apt-get install build-essential zlib1g-dev libsdl2-dev libasound2-dev
```

### yumが使える場合
- build-essential
```bash
$ yum groupinstall "Development Tools"
$ yum groupupdate  "Development Tools"
$ yum install kernel-devel kernel-headers
```

- zlib1g-dev
```bash
$ yum install openssl-devel zlib-devel readline-devel
```

- libsdl2-dev
```bash
$ yum install SDL2-devel
```

- libasound2-dev
```bash
# yum install alsa-lib-devel
```


### Juliusインストール
1. Juliusインストール

- 圧縮ファイルからのインストール
```
$ cd ~/Downloads
wget --trust-server-names "http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60273%2Fjulius-4.3.1.tar.gz"

$ tar zxvf julius-4.3.1.tar.gz
$ cd julius-4.3.1
$ ./configure
$ make -j4
$ cp /home/Downloads/julius-4.3.1/julius/julius ~/Software/julius/.
```

- GitHubからのインストール
```
$ cd ~/Software
git clone https://github.com/julius-speech/julius.git
cd julius
./configure --enable-words-int
make -j4
ls -l julius
```


2. 音声認識用モデルをダウンロード

```
$ mkdir -p ~/Software/julius
$ cd ~/Software/julius
$ wget --trust-server-names 'http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60416%2Fdictation-kit-v4.3.1-linux.tgz'
$ tar xvzf dictation-kit-v4.3.1-linux.tgz
```


---

## 動作テスト
### サーバの動作テスト
1. juliusを起動
```
$ ~/Software/julius/julius -C ~/Software/julius/dictation-kit-4.5/am-gmm.jconf -C ~/Software/julius/dictation-kit-4.5/main.jconf -input rawfile
```

2. 解析ファイルの指定
起動後の[enter filename->]にて

```
$ ~/Software/julius/test_wav/test.wav
```
* ) test.wavは用意したwave fileを指定してください。




---

## ポートオープン
- 開けたいポートを許可する
```
$ sudo iptables -A INPUT -p tcp -dport 8000 -j ACCEPT
$ sudo iptables -A INPUT -p tcp -dport 10500 -j ACCEPT
$ sudo iptables -A INPUT -p tcp -dport 22 -j ACCEPT

$ iptables-restore < /etc/iptables/iptables.rule
```

- FORWARDは使用しない
```
$ iptables -P FORWARD DROP　
```

- 一度、全て許可にする
```
$ iptables -P INPUT ACCEPT　
```

- デフォルト設定を全て削除
```
$ iptables -F　
```

- 自らのパケットは全て許可
```
$ iptables -A INPUT -i lo -j ACCEPT　
```

- SSH許可
```
$ iptables -A INPUT -p tcp -dport 22 -j ACCEPT　
$ iptables -A INPUT -p tcp -dport 1111 -j ACCEPT　
```

- FTP接続許可
```
$ iptables -A INPUT -p tcp -dport 20:21 -j ACCEPT　
```

- http/https接続許可
```
$ iptables -A INPUT -p tcp -dport 80 -j ACCEPT　
$ iptables -A INPUT -p tcp -dport 443 -j ACCEPT　
```

- POP受信メール / SMTP送信メール許可
```
$ iptables -A INPUT -p tcp -dport 110 -j ACCEPT　
$ iptables -A INPUT -p tcp -dport 25 -j ACCEPT　
```

- SUBMISSIONポート / PostgreSQLポート開放
```
$ iptables -A INPUT -p tcp -dport 587 -j ACCEPT　
$ iptables -A INPUT -p tcp -dport 5432 -j ACCEPT　
```

- DNS関連
```
$ iptables -A INPUT -p tcp -dport 53 -j ACCEPT　
$ iptables -A INPUT -p udp -dport 53 -j ACCEPT　
```

- PING許可
```
$ iptables -A INPUT -p icmp -j ACCEPT　
```

- TCP接続開始と応答、FTPデータ等許可
```
$ iptables -A INPUT -m state ESTABLISHED,RELATED -j ACCEPT　
```

- 設定以外のパケット拒否
```
$ iptables -P INPUT DROP　
```
